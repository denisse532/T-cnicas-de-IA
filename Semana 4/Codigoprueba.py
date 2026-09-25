import cv2
import os
from datetime import datetime

# Crear carpeta para guardar las capturas
carpeta = "capturas"

if not os.path.exists(carpeta):
    os.makedirs(carpeta)

# Abrir la cámara
camara = cv2.VideoCapture(0)

if not camara.isOpened():
    print("Error: No se pudo abrir la cámara.")
    exit()

print("======================================")
print("       VISION SOLIDARIA - MPV 1")
print("======================================")
print()
print("ESPACIO = Capturar imagen")
print("Q       = Salir")
print()

while True:

    # Leer imagen de la cámara
    ret, frame = camara.read()

    if not ret:
        print("Error: No se pudo recibir imagen de la cámara.")
        break

    # Mostrar el video
    cv2.imshow("Vision Solidaria - Camara", frame)

    # Esperar una tecla
    tecla = cv2.waitKey(1) & 0xFF

    # Capturar imagen con ESPACIO
    if tecla == ord(' '):

        fecha = datetime.now().strftime("%Y%m%d_%H%M%S")

        nombre_archivo = os.path.join(
            carpeta,
            f"captura_{fecha}.jpg"
        )

        cv2.imwrite(nombre_archivo, frame)

        print(f"Imagen guardada: {nombre_archivo}")

    # Salir con Q
    elif tecla == ord('q'):

        break

# Liberar la cámara
camara.release()

# Cerrar ventanas
cv2.destroyAllWindows()

print("Programa finalizado.")
