import cv2
import numpy as np
import math

x = cv2.imread('gamma.jpg',0)
alto, ancho = x.shape[:2]
imgFondo = np.zeros((alto *2, ancho *2 ),np.uint8)
matrizRotacion = np.array( [ [math.cos(np.pi/2), -math.sin(np.pi/2), 0], [math.sin(np.pi/2), math.cos(np.pi/2), 0], [0, 0, 1]  ] )


for i in range(0, alto):
    for j in range(0, ancho):
        matriz_posicion = np.array([ [ i ], [ j ], [ 1 ] ] )
        vector_rotacion = np.dot( matrizRotacion , matriz_posicion ) # Crea las coordenadas finales de ese pixel
        imgFondo[ int(vector_rotacion[0]), int(vector_rotacion[1]) ] = x[ i, j ] #Almacenar en mi imagen fondo el nuevo vector de traslacion
 

cv2.imshow( 'resultado1', x )   
cv2.imshow( 'resultabbbbbbbbbbbb', imgFondo )
cv2.waitKey(0)
cv2.destroyAllWindows()     


