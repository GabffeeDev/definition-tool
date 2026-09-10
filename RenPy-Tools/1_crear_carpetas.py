"""
Crear estructura de carpetas para un proyecto de Ren'Py
--------------------------------------------------------
Este script te pide que selecciones la carpeta "game" de tu proyecto
y crea automáticamente las subcarpetas típicas de imágenes y audio.

No necesitas saber programación para usarlo: solo haz doble clic
sobre el archivo (o ejecútalo como se indica en la guía) y sigue
las ventanas que aparecen.
"""

from pathlib import Path
from tkinter import Tk, filedialog, messagebox

# Carpetas que se crearán dentro de "game"
FOLDERS = [
    "images/bg",
    "images/cg",
    "audio/sfx",
    "audio/bgm",
]


def elegir_carpeta_game() -> str:
    root = Tk()
    root.withdraw()  # Oculta la ventana principal de Tkinter, solo mostramos el diálogo
    carpeta = filedialog.askdirectory(
        title="Selecciona la carpeta 'game' de tu proyecto de Ren'Py"
    )
    root.destroy()
    return carpeta


def main():
    carpeta_elegida = elegir_carpeta_game()

    if not carpeta_elegida:
        messagebox.showinfo("Operación cancelada", "No se seleccionó ninguna carpeta.\nNo se hicieron cambios.")
        return

    project_dir = Path(carpeta_elegida)

    if project_dir.name != "game":
        messagebox.showerror(
            "Carpeta incorrecta",
            "Debes seleccionar la carpeta llamada 'game' dentro de tu proyecto de Ren'Py.\n\n"
            f"Seleccionaste: {project_dir.name}"
        )
        return

    for folder in FOLDERS:
        (project_dir / folder).mkdir(parents=True, exist_ok=True)

    messagebox.showinfo(
        "¡Listo!",
        "Se creó la siguiente estructura dentro de tu carpeta 'game':\n\n"
        + "\n".join(f"• {f}" for f in FOLDERS)
    )


if __name__ == "__main__":
    main()
