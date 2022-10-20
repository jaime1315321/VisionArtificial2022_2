import numpy as np
import cv2

img1 = cv2.imread('a.png', 0)  # Leemos la imagen deseada
height, width = img1.shape  # Obtenemos las dimensiones


noise = np.zeros((height, width), np.uint8)  # Creamos una imagen para almacenar el ruido
cv2.randu(noise, 255, 200)  # Creamos ruido 
imgNoise = img1 + noise
imgb = np.zeros((height, width), np.float16)  # Creamos una imagen nueva
#imgb = cv2.GaussianBlur(imgNoise, (35, 35), sigmaX=10, sigmaY=0)  # Aplicamos el kernel a la imagen con la funcion filter2D
imgb = cv2.GaussianBlur(img1, (35, 35), sigmaX=10, sigmaY=0)  # Aplicamos el kernel a la imagen con la funcion filter2D

imgc = cv2.addWeighted (img1, 0.3, imgb, 0.7, -34.0) # Creamos la imagen c teniendo en cuenta las anteriores imágenes
#cv2.imshow('Imagen original  Imagen Ruido', np.hstack([img1, noise, imgNoise]))  # Mostramos las imagenes Original y con ruido
cv2.imshow('Imagen original  Imagen Ruido', np.hstack([img1]))  # Mostramos las imagenes Original y con ruido
cv2.waitKey(0)                            #Se espera a pulsar cualquier tecla para cerrar la imagen
cv2.destroyAllWindows()                   #Cierre de ventana

cv2.imshow('Imagen con filtro Gaussiano',np.hstack([imgb])) #Mostramos la imágen con el filtro Gaussiano
cv2.waitKey(0)                            # Se espera a pulsar cualquier tecla para cerrar la imagen
cv2.destroyAllWindows()                   # Cierre de ventana


cv2.imshow('Imagen c', np.hstack([imgc])) #Mostramos la imágen con la aplicación de la ecuación dada
cv2.waitKey(0)                            #Se espera a pulsar cualquier tecla para cerrar la imagen
cv2.destroyAllWindows()                   #Cierre de ventana

