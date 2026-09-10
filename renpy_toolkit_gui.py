"""
Ren'Py Toolkit - Interfaz gráfica unificada
--------------------------------------------
Esta interfaz reúne dos herramientas para proyectos de Ren'Py:

1) Crear carpetas
   Crea dentro de tu carpeta "game" la estructura típica de subcarpetas
   para imágenes y audio (images/bg, images/cg, audio/sfx, audio/bgm).

2) Generar definiciones
   Recorre la carpeta "game/images", encuentra todos los archivos
   .png / .jpg / .jpeg / .webp y genera automáticamente las líneas
   "image nombre = ruta" dentro de game/images/definitions.rpy,
   entre las marcas "# AUTO START" y "# AUTO END". Si el archivo no
   existe, lo crea con esas marcas.

No hace falta saber programar: eliges la carpeta "game" de tu
proyecto una sola vez y luego usas los botones de cada herramienta.
El registro de actividad (abajo) muestra qué se hizo en cada paso.
"""

import re
import traceback
from pathlib import Path
from tkinter import Tk, filedialog, messagebox, StringVar
from tkinter import ttk

EXTENSIONES_VALIDAS = [".png", ".jpg", ".jpeg", ".webp"]
MARCA_INICIO = "# AUTO START"
MARCA_FIN = "# AUTO END"

FOLDERS = [
    "images/bg",
    "images/cg",
    "audio/sfx",
    "audio/bgm",
]


class RenPyToolkitApp:
    def __init__(self, root: Tk):
        self.root = root
        self.root.title("Ren'Py Toolkit")
        self.root.geometry("640x560")
        self.root.minsize(560, 480)

        self.game_folder: Path | None = None
        self.folder_var = StringVar(value="Ninguna carpeta seleccionada")

        self._build_ui()

    # ---------- Construcción de la interfaz ----------

    def _build_ui(self):
        pad = {"padx": 12, "pady": 8}

        # --- Sección: selección de carpeta ---
        frame_folder = ttk.LabelFrame(self.root, text="Paso 1 · Carpeta del proyecto")
        frame_folder.pack(fill="x", **pad)

        ttk.Label(
            frame_folder,
            text="Selecciona la carpeta llamada 'game' dentro de tu proyecto de Ren'Py.\n"
                 "Las dos herramientas de abajo usarán esta misma carpeta.",
            wraplength=580, justify="left"
        ).pack(anchor="w", padx=10, pady=(8, 4))

        row = ttk.Frame(frame_folder)
        row.pack(fill="x", padx=10, pady=(0, 10))
        ttk.Button(row, text="Elegir carpeta 'game'...", command=self.elegir_carpeta).pack(side="left")
        ttk.Label(row, textvariable=self.folder_var, foreground="#444").pack(side="left", padx=10)

        # --- Sección: Crear carpetas ---
        frame1 = ttk.LabelFrame(self.root, text="Herramienta 1 · Crear carpetas")
        frame1.pack(fill="x", **pad)

        ttk.Label(
            frame1,
            text="Qué hace: crea dentro de 'game' las subcarpetas típicas para "
                 "organizar tus imágenes y audios:\n"
                 "  • images/bg   (fondos)\n"
                 "  • images/cg   (ilustraciones / CGs)\n"
                 "  • audio/sfx   (efectos de sonido)\n"
                 "  • audio/bgm   (música de fondo)\n"
                 "Si alguna carpeta ya existe, no se borra ni se modifica.",
            wraplength=580, justify="left"
        ).pack(anchor="w", padx=10, pady=(8, 4))

        ttk.Button(frame1, text="Crear estructura de carpetas", command=self.crear_carpetas).pack(
            anchor="w", padx=10, pady=(0, 10)
        )

        # --- Sección: Generar definiciones ---
        frame2 = ttk.LabelFrame(self.root, text="Herramienta 2 · Generar definiciones")
        frame2.pack(fill="x", **pad)

        ttk.Label(
            frame2,
            text="Qué hace: busca todas las imágenes (.png, .jpg, .jpeg, .webp) dentro de "
                 "'game/images' (incluyendo subcarpetas) y genera automáticamente una línea "
                 "'image nombre = \"ruta\"' por cada una. Ese bloque se inserta en "
                 "game/images/definitions.rpy, entre las marcas '# AUTO START' y '# AUTO END'. "
                 "Si el archivo no existe, se crea con esas marcas. Úsala cada vez que agregues "
                 "o quites imágenes.",
            wraplength=580, justify="left"
        ).pack(anchor="w", padx=10, pady=(8, 4))

        ttk.Button(frame2, text="Generar definiciones de imágenes", command=self.generar_definiciones).pack(
            anchor="w", padx=10, pady=(0, 10)
        )

        # --- Registro de actividad ---
        frame_log = ttk.LabelFrame(self.root, text="Registro de actividad")
        frame_log.pack(fill="both", expand=True, **pad)

        self.log_text = ttk.Frame(frame_log)
        self.log_text.pack(fill="both", expand=True, padx=10, pady=10)

        from tkinter import Text, Scrollbar
        self.log_widget = Text(self.log_text, height=10, wrap="word", state="disabled")
        scrollbar = Scrollbar(self.log_text, command=self.log_widget.yview)
        self.log_widget.configure(yscrollcommand=scrollbar.set)
        self.log_widget.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    # ---------- Utilidades ----------

    def log(self, mensaje: str):
        self.log_widget.configure(state="normal")
        self.log_widget.insert("end", mensaje + "\n")
        self.log_widget.see("end")
        self.log_widget.configure(state="disabled")

    def elegir_carpeta(self):
        carpeta = filedialog.askdirectory(title="Selecciona la carpeta 'game' de tu proyecto de Ren'Py")
        if not carpeta:
            return

        ruta = Path(carpeta)
        if ruta.name != "game":
            messagebox.showerror(
                "Carpeta incorrecta",
                "Debes seleccionar la carpeta llamada 'game' dentro de tu proyecto de Ren'Py.\n\n"
                f"Seleccionaste: {ruta.name}"
            )
            return

        self.game_folder = ruta
        self.folder_var.set(str(ruta))
        self.log(f"Carpeta seleccionada: {ruta}")

    def _requiere_carpeta(self) -> bool:
        if self.game_folder is None:
            messagebox.showwarning(
                "Falta la carpeta",
                "Primero selecciona la carpeta 'game' de tu proyecto (Paso 1)."
            )
            return False
        return True

    # ---------- Herramienta 1: Crear carpetas ----------

    def crear_carpetas(self):
        if not self._requiere_carpeta():
            return
        try:
            creadas = []
            for folder in FOLDERS:
                destino = self.game_folder / folder
                ya_existia = destino.exists()
                destino.mkdir(parents=True, exist_ok=True)
                if not ya_existia:
                    creadas.append(folder)

            if creadas:
                self.log("Carpetas creadas: " + ", ".join(creadas))
            else:
                self.log("Todas las carpetas ya existían. No se creó nada nuevo.")

            messagebox.showinfo(
                "¡Listo!",
                "Se verificó/creó la siguiente estructura dentro de 'game':\n\n"
                + "\n".join(f"• {f}" for f in FOLDERS)
            )
        except Exception as e:
            self.log(f"Error al crear carpetas: {e}")
            messagebox.showerror("Error", f"Ocurrió un error al crear las carpetas:\n{e}")
            traceback.print_exc()

    # ---------- Herramienta 2: Generar definiciones ----------

    def generar_lista_de_imagenes(self, image_folder: Path, game_folder: Path) -> list[str]:
        imagenes = []
        for archivo in image_folder.rglob("*"):
            if archivo.suffix.lower() not in EXTENSIONES_VALIDAS:
                continue

            relativa = archivo.relative_to(image_folder)
            nombre_png = archivo.stem
            ruta_png = archivo.relative_to(game_folder).as_posix()

            carpetas = list(relativa.parts[:-1])
            nombre_imagen = " ".join(carpetas + [nombre_png]) if carpetas else nombre_png

            imagenes.append(f'image {nombre_imagen} = "{ruta_png}"')

        imagenes.sort()
        return imagenes

    def generar_definiciones(self):
        if not self._requiere_carpeta():
            return

        game_folder = self.game_folder
        image_folder = game_folder / "images"
        target = image_folder / "definitions.rpy"

        if not image_folder.exists():
            messagebox.showerror(
                "No se encontró la carpeta de imágenes",
                f"No existe esta carpeta:\n{image_folder}\n\n"
                "Usa primero la Herramienta 1 (Crear carpetas) y vuelve a intentarlo."
            )
            self.log("Error: no existe game/images.")
            return

        try:
            if not target.exists():
                target.write_text(f"{MARCA_INICIO}\n{MARCA_FIN}\n", encoding="utf-8")
                self.log("definitions.rpy no existía: se creó con las marcas necesarias.")

            texto = target.read_text(encoding="utf-8")

            patron = re.compile(
                rf"({re.escape(MARCA_INICIO)}\n)(.*?)({re.escape(MARCA_FIN)})",
                re.DOTALL,
            )

            if not patron.search(texto):
                messagebox.showerror(
                    "Formato incorrecto",
                    f"El archivo definitions.rpy no contiene las marcas necesarias:\n\n"
                    f"{MARCA_INICIO}\n{MARCA_FIN}\n\n"
                    "Agrégalas manualmente en el archivo y vuelve a intentarlo."
                )
                self.log("Error: definitions.rpy no tiene las marcas AUTO START / AUTO END.")
                return

            imagenes = self.generar_lista_de_imagenes(image_folder, game_folder)
            codigo = "\n".join(imagenes)

            nuevo_texto = patron.sub(lambda m: f"{m.group(1)}{codigo}\n{m.group(3)}", texto)
            target.write_text(nuevo_texto, encoding="utf-8")

            self.log(f"Se generaron {len(imagenes)} definiciones de imágenes en {target}")
            messagebox.showinfo(
                "¡Listo!",
                f"Se generaron {len(imagenes)} definiciones de imágenes.\n\n"
                f"Archivo actualizado:\n{target}"
            )
        except Exception as e:
            self.log(f"Error al generar definiciones: {e}")
            messagebox.showerror("Error", f"Ocurrió un error al generar las definiciones:\n{e}")
            traceback.print_exc()


def main():
    root = Tk()
    try:
        style = ttk.Style()
        if "clam" in style.theme_names():
            style.theme_use("clam")
    except Exception:
        pass
    app = RenPyToolkitApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
