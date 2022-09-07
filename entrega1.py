import numpy as np
import cv2
import math

imgOriginal = cv2.imread('lena.jpg',0)
alto, ancho = imgOriginal.shape[:2]

fondoRotacion = np.zeros( (alto, ancho), np.uint8)
fondoShearing = np.zeros( (alto *2, ancho*2), np.uint8)
img5 = np.zeros( (alto, ancho), np.uint8)

matrizRotacion = np.array( [ [math.cos(np.pi/2), -math.sin(np.pi/2), 0], [math.sin(np.pi/2), math.cos(np.pi/2), 0], [0, 0, 1] ])

matrizShearing = np.array( [ [1, 0.2, 0], [0, 1, 0], [0, 0, 1] ] )

#imagen Rotada

for i in range(0, alto):
    for j in range(0, ancho):
        matrizPosicionRot = np.array( [[i], [j], [1]] )
        vectorRotacion = np.dot(matrizRotacion, matrizPosicionRot)
        fondoRotacion[ int( vectorRotacion[0]), int( vectorRotacion[1])] = imgOriginal[ i, j ]

#Interpolacion o corrección 

for i in range(0,alto):
    for j in range(0, ancho):
        if(fondoRotacion[i, j] == 0):
            fondoRotacion[i, j] = fondoRotacion[ i-1, j-1 ]

#Imagen con shearing

alto2, ancho2 = fondoRotacion.shape[:2]
for i in range(0, alto2):
    for j in range(0, ancho2):
        matrizPosicionShearing = np.array( [[i], [j], [1]] )
        vectorShearing = np.dot(matrizShearing, matrizPosicionShearing)
        fondoShearing[ int(vectorShearing[0]), int(vectorShearing[1])] = fondoRotacion[ i, j ]
        
#Imagen con traslacion despues del shearing
alto3, ancho3 = fondoShearing.shape[:2]
imgFondo3 = np.zeros( (alto3 *2, ancho3*2 ), np.uint8)
matrizTraslacion = np.array( [ [1, 0, 300], [0, 1, 300], [0, 0, 1] ] )


for i in range(0, alto3):
    for j in range(0, ancho3):
        matrizPosicionTras = np.array( [[i], [j], [1]] )
        vectorTraslacion = np.dot(matrizTraslacion , matrizPosicionTras )
        imgFondo3[ int(vectorTraslacion[0]), int(vectorTraslacion[1])] = fondoShearing[ i, j ]
        
#Inversamente1 antitraslacion

altoInverso1, anchoInverso1 = imgFondo3.shape[:2]
fondoInverso1Antitraslacion = np.zeros( (altoInverso1, anchoInverso1 ), np.uint8)
matrizTraslacionInverso1 = np.array( [ [1, 0, -300], [0, 1, -300], [0, 0, 1] ] )

for i in range(0, altoInverso1):
    for j in range(0, anchoInverso1):
        matrisPosicionTrasInver1 = np.array( [[i], [j], [1]] )
        vectorTraslacionInverso1 = np.dot(matrizTraslacionInverso1, matrisPosicionTrasInver1)
        fondoInverso1Antitraslacion[ int(vectorTraslacionInverso1[0]), int(vectorTraslacionInverso1[1])] = imgFondo3[ i, j ]

#Inversamente1 antishearing
altoInverso2, anchoInverso2 = fondoInverso1Antitraslacion.shape[:2]
tmp = int(altoInverso2//2.5)
fondoInverso1AntiShering = np.zeros( (int(altoInverso2), int(anchoInverso2) ), np.uint8)
matrizSheraingInverso2 = np.array( [ [1, -0.2, 0], [0, 1, 0], [0, 0, 1] ] )

for i in range(0, altoInverso2):
    for j in range(0, anchoInverso2):
        matrizPosicionShearingInverso = np.array( [[i], [j], [1]] )
        vectorShearingInverso = np.dot(matrizSheraingInverso2, matrizPosicionShearingInverso)
        fondoInverso1AntiShering[ int(vectorShearingInverso[0]), int(vectorShearingInverso[1])] = fondoInverso1Antitraslacion[ i, j ]


# Inversamente antirotacion

altoInverso3, anchoInverso3 = fondoInverso1AntiShering.shape[:2]
fondoInverso1AntiRotacion = np.zeros( (alto, ancho ), np.uint8)
matrizRotacionInverso2 = np.array( [ [math.cos(-np.pi/2), -math.sin(-np.pi/2), 0], [math.sin(-np.pi/2), math.cos(-np.pi/2), 0], [0, 0, 1] ])

for i in range(0, alto):
    for j in range(0, ancho):
        matrizPosicionRotacionInverso = np.array( [[i], [j], [1]] )
        vectorRotacionInverso = np.dot(matrizRotacionInverso2, matrizPosicionRotacionInverso)
        fondoInverso1AntiRotacion[ int(vectorRotacionInverso[0]), int(vectorRotacionInverso[1])] = fondoInverso1AntiShering[ i, j ]
#Interpolacion o corrección 

for i in range(0,alto ):
    for j in range(0, ancho):
        if(fondoInverso1AntiRotacion[i, j] == 0):
            fondoInverso1AntiRotacion[i, j] = fondoInverso1AntiRotacion[ i-1, j-1 ]

cv2.imshow('imagen original', imgOriginal)
cv2.waitKey(0)
cv2.imshow('imagen Rotada', fondoRotacion)
cv2.waitKey(0)
cv2.imshow('imagen Rotada % Shearing', fondoShearing)
cv2.waitKey(0)
cv2.imshow('imagenfinal', imgFondo3)
cv2.waitKey(0)
cv2.imshow('imagenInvertidaTraslación', fondoInverso1Antitraslacion)
cv2.waitKey(0)
cv2.imshow('imagenInvertidaShearing', fondoInverso1AntiShering)
cv2.waitKey(0)
cv2.imshow('imagenInvertidaRotacion', fondoInverso1AntiRotacion)
cv2.waitKey(0)
cv2.destroyAllWindows()