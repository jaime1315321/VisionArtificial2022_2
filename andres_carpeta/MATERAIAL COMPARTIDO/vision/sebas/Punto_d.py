import numpy as np
import cv2
 
img1 = cv2.imread('img1.png')  # Leemos la imagen
alto, ancho=img1.shape[:2]  # Obtenemos sus dimensiones
imgGb = np.zeros((alto, ancho), np.float16)  # Creamos una imagen nueva
 
img2 = cv2.imread('img2.png')  # Leemos la imagen
alto1, ancho1 = img2.shape[:2]  # Obtenemos sus dimensiones
imgFm = np.zeros((alto1, ancho1), np.float16)  # Creamos una imagen nueva
 
img3 = cv2.imread('img3.png')  # Leemos la imagen
alto2, ancho2 = img3.shape[:2]  # Obtenemos sus dimensiones
imgFm1 = np.zeros((alto2, ancho2), np.float16)  # Creamos una imagen nueva
 
imgGb = cv2.GaussianBlur(img1, (5,  5), sigmaX=0, sigmaY=0)  # Aplicamos el kernel a la imagen con la funcion filter2D
cv2.imshow('Filtro Gausiano', np.hstack([img1,imgGb]))  # Mostramos las imagenes
cv2.waitKey(0)  # Se espera a pulsar cualquier tecla para cerrar la imagen
cv2.destroyAllWindows()  # Cierre de ventanas
 
imgFm = cv2.medianBlur(img2, 3)
cv2.imshow('Filtro Mediana', np.hstack([img2, imgFm]))  # Mostramos las imagenes
cv2.waitKey(0)  # Se espera a pulsar cualquier tecla para cerrar la imagen
cv2.destroyAllWindows()  # Cierre de ventanas
 
imgFm1 = cv2.medianBlur(img3, 3)
cv2.imshow('Filtro Mediana1', np.hstack([img3, imgFm1]))  # Mostramos las imagenes
cv2.waitKey(0)  # Se espera a pulsar cualquier tecla para cerrar la imagen
cv2.destroyAllWindows()  # Cierre de ventanas