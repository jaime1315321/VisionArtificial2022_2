import numpy as np
import cv2
from numpy.lib.npyio import fromregex

img1 = cv2.imread('/mnt/Documents/images/lena.jpg', 0)  # Leemos la imagen
height, width = img1 .shape[:2]  # Obtenemos sus dimensiones
imgFpa  = np.zeros((height, width), np.uint8)  # Creamos una imagen nueva
kern =  np.array([[1, -2, 1], [-2, 4, -2], [1, -2, 1]])
imgFpa = cv2.filter2D(img1, ddepth=-1, kernel=kern, anchor=(-1, -1))  # Aplicamos el kernel a la imagen con la funcion filter2D
cv2.imshow('Imagen original                               Imagen filtrada', np.hstack([img1, imgFpa]))  # Mostramos las imagenes
cv2.waitKey(0)  # Se espera a pulsar cualquier tecla para cerrar la imagen
cv2.destroyAllWindows()  # Cierre de ventanas

# Fuente: Documentación OpenCV
