import cv2
import numpy as np
import math

imgJaime = cv2.imread('lena.jpg', 0)
alto, ancho = imgJaime.shape[:2]
imgFondo = np.zeros((alto *3, ancho *3, 3),np.uint8)
matrizEscalado = np.array( [ [3, 0, 0], [0, 3, 0], [0, 0, 1] ] )


for i in range(0, alto):
    for j in range(0, ancho):
        matriz_posicion = np.array([ [ i ], [ j ], [ 1 ] ] )
        vector_escalado = np.dot( matrizEscalado , matriz_posicion ) # Crea las coordenadas finales de ese pixel
        imgFondo[ int(vector_escalado[0]), int(vector_escalado[1]) ] = imgJaime[ i, j ] #Almacenar en mi imagen fondo el nuevo vector de traslacion
 

cv2.imshow( 'resultado1', imgJaime )   
cv2.imshow( 'resultado2', imgFondo )
cv2.waitKey(0)
cv2.destroyAllWindows()     
        