import cv2
from ultralytics import YOLO

# Cargar modelo YOLO
modelo = YOLO("yolo11n.pt")

# Abrir cámara
camara = cv2.VideoCapture(0)

if not camara.isOpened():
    print("Error: No se pudo abrir la cámara.")
    exit()

print("======================================")
print("     VISION SOLIDARIA - SPRINT 2")
print("       DETECCION DE OBJETOS CON IA")
print("======================================")
print()
print("Presiona Q para salir.")
print()

while True:

    # Capturar imagen
    ret, frame = camara.read()

    if not ret:
        print("Error al obtener imagen de la cámara.")
        break

    # Ejecutar detección
    resultados = modelo(frame)

    # Dibujar las detecciones
    imagen = resultados[0].plot()

    # Mostrar resultado
    cv2.imshow("Vision Solidaria - Deteccion IA", imagen)

    # Salir con Q
    tecla = cv2.waitKey(1) & 0xFF

    if tecla == ord("q"):
        break

# Liberar cámara
camara.release()

# Cerrar ventanas
cv2.destroyAllWindows()

print("Programa finalizado.")
