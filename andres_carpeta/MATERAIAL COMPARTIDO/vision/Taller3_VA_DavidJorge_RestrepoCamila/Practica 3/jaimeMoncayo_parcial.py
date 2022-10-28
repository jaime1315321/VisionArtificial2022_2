import cv2
import numpy as np




img = cv2.imread('parcial.png')  # Leemos la imagen original
cv2.imshow('Imagen',img) # Se aplica filtro y luego se umbraliza la imagen
cv2.waitKey(0)


#######################################FUNCION############################


imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # Se convierte la imagen de color a una imagen en escala de grises. 
imgray = cv2.GaussianBlur(imgray, (1, 1), 3) # Se aplica un filtro gausiano para reducir el ruido en la imagen de salida
t, img_umbral = cv2.threshold(imgray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_TRIANGLE) # Umbralizacion con operador binario inverso

imgc = cv2.medianBlur(img_umbral, 7)

cv2.imshow('Imagen binarizada y sin ruido', imgc)
cv2.waitKey(0)
                ###


contours, hierarchy = cv2.findContours(imgc, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # Obtenemos los contornos


                # cv2.drawContours(img,contours,-1,(125,125,0),2,cv2.LINE_AA) # Dibujamos los contornos
                # cv2.imshow('Imagen original con contornos', img) #Muestra la imagen original con contornos
                # cv2.waitKey(0)

cv2.drawContours(img,contours,-1,(125,125,0),2,cv2.LINE_AA) # Dibujamos los contornos
cv2.imshow('Imagen original con contornos', img) #Muestra la imagen original con contornos
cv2.waitKey(0)
cv2.destroyAllWindows()
        
