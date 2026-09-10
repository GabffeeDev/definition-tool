"""RenPy Tools - Utilidades gráficas para proyectos de Ren'Py."""
from pathlib import Path
import re
import sys
import tkinter as tk
from tkinter import filedialog, messagebox

EXTENSIONES_VALIDAS = {".png", ".jpg", ".jpeg", ".webp"}
MARCA_INICIO = "# AUTO START"
MARCA_FIN = "# AUTO END"
FOLDERS = ("images/bg", "images/cg", "audio/fx", "audio/bgm")


def obtener_ruta_recurso(nombre: str) -> Path:
    """Devuelve la ruta correcta de un recurso en desarrollo o PyInstaller."""
    base = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent))
    return base / nombre


class RenPyTools(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("RenPy Tools")
        self._configurar_icono()
        self.geometry("620x470")
        self.resizable(False, False)
        self.configure(padx=28, pady=24)

        tk.Label(self, text="RenPy Tools", font=("Segoe UI", 26, "bold")).pack()
        tk.Label(
            self,
            text="Herramientas para automatizar tareas repetitivas en tus proyectos de Ren'Py",
            font=("Segoe UI", 10),
            wraplength=540,
            justify="center",
        ).pack(pady=(4, 24))

        self._tool_card(
            "1. Crear estructura de carpetas",
            "Crea automáticamente images/bg, images/cg, audio/sfx y audio/bgm dentro de la carpeta game.",
            self.crear_carpetas,
            "Crear carpetas",
        )

        self._tool_card(
            "2. Generar definiciones de imágenes",
            "Busca imágenes y actualiza automáticamente images/definitions.rpy con sus definiciones de Ren'Py.",
            self.generar_definiciones,
            "Generar definiciones",
        )

        tk.Label(
            self,
            text="Selecciona siempre la carpeta 'game' de tu proyecto.",
            font=("Segoe UI", 9, "italic"),
        ).pack(pady=(16, 0))

    def _configurar_icono(self):
        icono = obtener_ruta_recurso("tool.ico")
        if icono.exists():
            try:
                self.iconbitmap(default=str(icono))
            except tk.TclError:
                pass

    def _tool_card(self, title, description, command, button_text):
        frame = tk.LabelFrame(
            self,
            text=title,
            padx=16,
            pady=12,
            font=("Segoe UI", 10, "bold"),
        )
        frame.pack(fill="x", pady=7)

        tk.Label(
            frame,
            text=description,
            justify="left",
            anchor="w",
            wraplength=500,
        ).pack(fill="x")

        tk.Button(
            frame,
            text=button_text,
            command=command,
            width=24,
        ).pack(pady=(10, 0))

    def elegir_game(self):
        carpeta = filedialog.askdirectory(
            title="Selecciona la carpeta 'game' de tu proyecto de Ren'Py"
        )

        if not carpeta:
            return None

        game = Path(carpeta)

        if game.name.lower() != "game":
            messagebox.showerror(
                "Carpeta incorrecta",
                "Debes seleccionar la carpeta llamada 'game' dentro de tu proyecto de Ren'Py.\n\n"
                f"Seleccionaste: {game.name}",
            )
            return None

        return game

    def crear_carpetas(self):
        game = self.elegir_game()
        if not game:
            return

        creadas = []

        try:
            for folder in FOLDERS:
                destino = game / folder
                if not destino.exists():
                    creadas.append(folder)
                destino.mkdir(parents=True, exist_ok=True)
        except OSError as error:
            messagebox.showerror(
                "Error al crear carpetas",
                f"No se pudieron crear las carpetas.\n\n{error}",
            )
            return

        if creadas:
            texto = (
                "Se creó la siguiente estructura:\n\n"
                + "\n".join(f"• {folder}" for folder in creadas)
            )
        else:
            texto = "La estructura de carpetas ya existía. No fue necesario crear nada."

        messagebox.showinfo("¡Listo!", texto)

    def generar_definiciones(self):
        game = self.elegir_game()
        if not game:
            return

        image_folder = game / "images"

        if not image_folder.exists():
            messagebox.showerror(
                "No se encontró la carpeta de imágenes",
                "No existe la carpeta 'images'.\n\n"
                "Usa primero la herramienta 'Crear estructura de carpetas'.",
            )
            return

        target = image_folder / "definitions.rpy"

        try:
            if not target.exists():
                target.write_text(
                    f"{MARCA_INICIO}\n{MARCA_FIN}\n",
                    encoding="utf-8",
                )

            texto = target.read_text(encoding="utf-8")
        except OSError as error:
            messagebox.showerror(
                "Error al leer el archivo",
                f"No se pudo acceder a definitions.rpy.\n\n{error}",
            )
            return

        patron = re.compile(
            rf"({re.escape(MARCA_INICIO)}\r?\n)(.*?)({re.escape(MARCA_FIN)})",
            re.DOTALL,
        )

        if not patron.search(texto):
            messagebox.showerror(
                "Formato incorrecto",
                "El archivo definitions.rpy no contiene las marcas necesarias:\n\n"
                f"{MARCA_INICIO}\n{MARCA_FIN}",
            )
            return

        imagenes = self._buscar_imagenes(image_folder, game, target)
        codigo = "\n".join(imagenes)

        nuevo_texto = patron.sub(
            lambda match: f"{match.group(1)}{codigo}\n{match.group(3)}",
            texto,
        )

        try:
            target.write_text(nuevo_texto, encoding="utf-8")
        except OSError as error:
            messagebox.showerror(
                "Error al guardar",
                f"No se pudo actualizar definitions.rpy.\n\n{error}",
            )
            return

        messagebox.showinfo(
            "¡Listo!",
            f"Se generaron {len(imagenes)} definiciones de imágenes.\n\n"
            f"Archivo actualizado:\n{target}",
        )

    @staticmethod
    def _buscar_imagenes(
        image_folder: Path,
        game_folder: Path,
        definitions_file: Path,
    ):
        imagenes = []

        for archivo in image_folder.rglob("*"):
            if not archivo.is_file() or archivo == definitions_file:
                continue

            if archivo.suffix.lower() not in EXTENSIONES_VALIDAS:
                continue

            relativa = archivo.relative_to(image_folder)
            nombre_imagen = " ".join(
                list(relativa.parts[:-1]) + [archivo.stem]
            )
            ruta = archivo.relative_to(game_folder).as_posix()

            imagenes.append(f'image {nombre_imagen} = "{ruta}"')

        return sorted(imagenes, key=str.lower)


if __name__ == "__main__":
    RenPyTools().mainloop()
