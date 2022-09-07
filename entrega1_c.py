import math 
import numpy as np 
import cv2
import matplotlib
#import pyplot as plt 

imgOriginal = cv2.imread('lena.jpg', 0)
filas, columnas = imgOriginal.shape

cv2.imshow('Imagen Original', imgOriginal)
cv2.waitKey(0)

#Rotacion con OpenCv

rotacionJaime = cv2.getRotationMatrix2D((columnas/2, filas/2), 90, 1)
img_Rotada = cv2.warpAffine(imgOriginal, rotacionJaime, (columnas, filas))
cv2.imshow('Imagen Rotada OpenCv', img_Rotada)
cv2.waitKey(0)

#Shearing

shearingJaime = np.float32( [ [1, 0.2, 0],[0, 1, 0] ] )
img_shearing = cv2.warpAffine(img_Rotada, shearingJaime, (columnas*2, filas*2), cv2.INTER_LINEAR, cv2.BORDER_CONSTANT)
cv2.imshow('Imagen Shearing OpenCv', img_shearing)
cv2.waitKey(0)

#Traslacion

traslacionJaime = np.float32( [ [1, 0, 300],[0, 1, 300] ] )
img_traslacion = cv2.warpAffine(img_shearing, traslacionJaime, (columnas*3, filas*3))
cv2.imshow('Imagen Traslacion OpenCv', img_traslacion)
cv2.waitKey(0)

#Traslacion Inversa

matrizTraslacion = np.array( [ [1, 0, 300],[0, 1, 300],[0, 0, 1] ] )#Formar nuevamente la matriz
matrizInversaTraslacion = np.linalg.inv( matrizTraslacion ) #Obtener la matriz inversa de la anterior

traslacionJaime_Invertida = np.array( [ matrizInversaTraslacion[0], matrizInversaTraslacion[1] ] )
img_traslacion_Inversa = cv2.warpAffine( img_traslacion, traslacionJaime_Invertida, (columnas*2, filas*2))
cv2.imshow('Imagen Anti-Traslacion OpenCv', img_traslacion_Inversa)
cv2.waitKey(0)

#Shearing Inverso

matrizShearing = np.array( [ [1, 0.2, 0],[0, 1, 0],[0, 0, 1] ] )#Formar nuevamente la matriz
matrizInversaShering = np.linalg.inv( matrizShearing ) #Obtener la matriz inversa de la anterior_Inversa

shearingJaime_Invertida = np.array( [ matrizInversaShering[0], matrizInversaShering[1] ] )
img_shearing_Inversa = cv2.warpAffine( img_traslacion_Inversa, shearingJaime_Invertida, (columnas*2, filas*2), cv2.INTER_LINEAR, cv2.BORDER_CONSTANT)
cv2.imshow('Imagen Anti-Shearing OpenCv', img_shearing_Inversa)
cv2.waitKey(0)

#Rotacion Inversa


matrizRotacion = np.array( [ rotacionJaime[0],rotacionJaime[1],[0, 0, 1] ] )#Formar nuevamente la matriz
matrizInversaRotacion = np.linalg.inv( matrizRotacion ) #Obtener la matriz inversa de la anterior

rotacionJaime_Invertida = np.array( [ matrizInversaRotacion[0], matrizInversaRotacion[1] ] )
img_traslacion_Inversa = cv2.warpAffine( img_shearing_Inversa, rotacionJaime_Invertida, (columnas, filas))
cv2.imshow('Imagen Anti-Rotacion OpenCv', img_traslacion_Inversa)
cv2.waitKey(0)

cv2.destroyAllWIndows()



