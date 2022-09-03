from configparser import Interpolation
from gettext import translation
import cv2 
import numpy as np
import matplotlib 
#import pyplot as plt

imgJaime = cv2.imread('lena.jpg',0)
columnas, filas = imgJaime.shape

escalado = cv2.resize(imgJaime, None, fx=0.5, fy=0.5, interpolation = cv2.INTER_AREA)

cv2.imshow('Imagen Original', imgJaime)
cv2.imshow('Imagen con escala', escalado)
cv2.waitKey(0)
cv2.destroyAllWindows()


#or reducir tamaño hagalop or area y si se va a aumentar hagalo por cúbica

alto, ancho = imgJaime.shape[:2]
res = cv2.resize(imgJaime,(1000,1000), interpolation = cv2.INTER_CUBIC)


# cv2.imshow('Imagen Original', imgJaime)
# cv2.imshow('Imagen con escala_CUBICA', res)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
