import cv2
import numpy as np

# Crear un lienzo negro
lienzo = np.zeros((600, 800, 3), dtype=np.uint8)

# Dibujar una línea
cv2.line(lienzo, (100, 100), (400, 100), (0, 255, 0), 3)  # Línea verde

# Dibujar un rectángulo
cv2.rectangle(lienzo, (100, 150), (400, 250), (0, 0, 255), 2)  # Rectángulo rojo
cv2.rectangle(lienzo, (450, 150), (700, 250), (255, 0, 0), -1)  # Rectángulo azul relleno

# Dibujar un círculo
cv2.circle(lienzo, (250, 350), 75, (255, 255, 0), 2)  # Círculo amarillo
cv2.circle(lienzo, (550, 350), 50, (0, 255, 255), -1)  # Círculo cian relleno

# Dibujar una elipse
cv2.ellipse(lienzo, (250, 450), (100, 50), 0, 0, 360, (255, 0, 255), 2)  # Elipse magenta

# Dibujar un polígono
puntos = np.array([[550, 450], [650, 450], [600, 550]], np.int32)
puntos = puntos.reshape((-1, 1, 2))
cv2.polylines(lienzo, [puntos], True, (255, 255, 255), 3)  # Triángulo blanco

# Agregar texto
fuente = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(lienzo, 'OpenCV Drawing Functions', (200, 50), fuente, 1, (255, 255, 255), 2)

# Mostrar la imagen
cv2.imshow('Funciones de Dibujo en OpenCV', lienzo)

# Esperar hasta que se presione una tecla
cv2.waitKey(0)

# Cerrar todas las ventanas
cv2.destroyAllWindows()