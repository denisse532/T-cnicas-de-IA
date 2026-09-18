import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk


def seleccionar_imagen():
    ruta = filedialog.askopenfilename(
        title="Selecciona una imagen de una hoja",
        filetypes=[
            ("Imágenes", "*.jpg *.jpeg *.png"),
            ("Todos los archivos", "*.*")
        ]
    )

    if ruta:
        try:
            imagen = Image.open(ruta)

            # Redimensionar para mostrarla en la ventana
            imagen.thumbnail((500, 400))

            imagen_tk = ImageTk.PhotoImage(imagen)

            etiqueta_imagen.config(image=imagen_tk)
            etiqueta_imagen.image = imagen_tk

            resultado.config(
                text="Imagen cargada correctamente.\n"
                     "Lista para el análisis de IA."
            )

        except Exception as error:
            messagebox.showerror(
                "Error",
                f"No se pudo abrir la imagen:\n{error}"
            )


# Crear ventana
ventana = tk.Tk()
ventana.title("Detector de Plantas Enfermas - IA")
ventana.geometry("650x600")

# Título
titulo = tk.Label(
    ventana,
    text="Detector de Plantas Enfermas mediante IA",
    font=("Arial", 18, "bold")
)
titulo.pack(pady=20)

# Instrucciones
instruccion = tk.Label(
    ventana,
    text="Selecciona una fotografía de una hoja",
    font=("Arial", 12)
)
instruccion.pack(pady=10)

# Botón
boton = tk.Button(
    ventana,
    text="Seleccionar imagen",
    command=seleccionar_imagen,
    font=("Arial", 12),
    padx=20,
    pady=10
)
boton.pack(pady=10)

# Espacio para la imagen
etiqueta_imagen = tk.Label(ventana)
etiqueta_imagen.pack(pady=20)

# Resultado
resultado = tk.Label(
    ventana,
    text="Esperando una imagen...",
    font=("Arial", 12)
)
resultado.pack(pady=10)

# Ejecutar aplicación
ventana.mainloop()
