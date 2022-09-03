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
       
cv2.imshow('imagen original', imgOriginal)
cv2.waitKey(0)
cv2.imshow('imagen Rotada', fondoRotacion)
cv2.waitKey(0)
cv2.imshow('imagen Rotada % Shearing', fondoShearing)
cv2.waitKey(0)
cv2.imshow('imagenfinal', imgFondo3)
cv2.waitKey(0)
cv2.destroyAllWindows()