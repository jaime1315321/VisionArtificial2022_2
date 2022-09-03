from gettext import translation
import cv2 
import numpy as np
import matplotlib 
#import pyplot as plt

imgJaime = cv2.imread('lena.jpg',0)
columnas, filas = imgJaime.shape

trasladoJaime = np.float32([[1, 0, -20],[0, 1, -50]])

fondo = cv2.warpAffine(imgJaime, trasladoJaime, (columnas, filas))

cv2.imshow('Imagen Original', imgJaime)
cv2.imshow('Translacion', fondo)
cv2.waitKey(0)
cv2.destroyAllWindows()
