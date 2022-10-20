#Punto E

#Importamos las librerias. 
import numpy as np
import cv2
import matplotlib as plt


img = cv2.imread('papa.jpg',0)  # Cargamos la imagen
height, width = img.shape[:2]  # Tomamos las dimensiones de la imagen cargada
ret1, imgotsu = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow('Imagen original',img)
cv2.imshow('Umbralizacion otsu', imgotsu)
cv2.waitKey(0)
cv2.destroyAllWindows()