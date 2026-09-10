"""
Generador automático de definiciones de imágenes para Ren'Py
--------------------------------------------------------------
Este script recorre la carpeta "images" de tu proyecto, encuentra
todos los archivos .png / .jpg / .jpeg / .webp, y genera una línea
"image nombre = ruta" para cada uno. Luego inserta ese bloque dentro
de tu archivo definitions.rpy, entre las marcas:

    # AUTO START
    # AUTO END

No necesitas escribir ninguna ruta a mano: el script te pedirá que
selecciones la carpeta "game" de tu proyecto con una ventana.

Si el archivo definitions.rpy no existe todavía dentro de
game/images/, el script lo crea automáticamente con las marcas
necesarias.
"""

import re
from pathlib import Path
from tkinter import Tk, filedialog, messagebox

EXTENSIONES_VALIDAS = [".png", ".jpg", ".jpeg", ".webp"]
MARCA_INICIO = "# AUTO START"
MARCA_FIN = "# AUTO END"


def elegir_carpeta_game() -> str:
    root = Tk()
    root.withdraw()
    carpeta = filedialog.askdirectory(
        title="Selecciona la carpeta 'game' de tu proyecto de Ren'Py"
    )
    root.destroy()
    return carpeta


def generar_lista_de_imagenes(image_folder: Path, game_folder: Path) -> list[str]:
    imagenes = []

    for archivo in image_folder.rglob("*"):
        if archivo.suffix.lower() not in EXTENSIONES_VALIDAS:
            continue

        # Ruta relativa a la carpeta "images" (para armar el nombre)
        relativa = archivo.relative_to(image_folder)

        # Nombre del archivo sin extensión
        nombre_png = archivo.stem

        # Ruta relativa a la carpeta "game" (para el código de Ren'Py)
        ruta_png = archivo.relative_to(game_folder).as_posix()

        # Nombre de la imagen dentro de Ren'Py (incluye subcarpetas)
        carpetas = list(relativa.parts[:-1])
        nombre_imagen = " ".join(carpetas + [nombre_png]) if carpetas else nombre_png

        imagenes.append(f'image {nombre_imagen} = "{ruta_png}"')

    imagenes.sort()
    return imagenes


def main():
    carpeta_elegida = elegir_carpeta_game()

    if not carpeta_elegida:
        messagebox.showinfo("Operación cancelada", "No se seleccionó ninguna carpeta.\nNo se hicieron cambios.")
        return

    game_folder = Path(carpeta_elegida)

    if game_folder.name != "game":
        messagebox.showerror(
            "Carpeta incorrecta",
            "Debes seleccionar la carpeta llamada 'game' dentro de tu proyecto de Ren'Py.\n\n"
            f"Seleccionaste: {game_folder.name}"
        )
        return

    image_folder = game_folder / "images"
    target = image_folder / "definitions.rpy"

    if not image_folder.exists():
        messagebox.showerror(
            "No se encontró la carpeta de imágenes",
            f"No existe esta carpeta:\n{image_folder}\n\n"
            "Crea primero tus carpetas de imágenes (puedes usar el script "
            "'1_crear_carpetas.py') y vuelve a intentarlo."
        )
        return

    # Si definitions.rpy no existe, lo creamos con las marcas necesarias
    if not target.exists():
        target.write_text(f"{MARCA_INICIO}\n{MARCA_FIN}\n", encoding="utf-8")

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
        return

    imagenes = generar_lista_de_imagenes(image_folder, game_folder)
    codigo = "\n".join(imagenes)

    nuevo_texto = patron.sub(lambda m: f"{m.group(1)}{codigo}\n{m.group(3)}", texto)
    target.write_text(nuevo_texto, encoding="utf-8")

    messagebox.showinfo(
        "¡Listo!",
        f"Se generaron {len(imagenes)} definiciones de imágenes.\n\n"
        f"Archivo actualizado:\n{target}"
    )


if __name__ == "__main__":
    main()
