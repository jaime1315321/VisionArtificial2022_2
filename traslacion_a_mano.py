import cv2
import numpy as np

imgJaime = cv2.imread('gamma.jpg')
alto, ancho = imgJaime.shape[:2]
imgFondo = np.zeros((alto *2, ancho *2, 3),np.uint8)
matrizTraslacion = np.array( [ [1, 0, 200], [0, 1, 0], [0, 0, 1] ] )


for i in range(0, ancho):
    for j in range(0, alto):
        matriz_posicion = np.array([ [ i ], [ j ], [ 1 ] ] )
        vector_translation = np.dot( matrizTraslacion , matriz_posicion ) # Crea las coordenadas finales de ese pixel
        imgFondo[ vector_translation[1], vector_translation[0] ] = imgJaime[ j, i ] #Almacenar en mi imagen fondo el nuevo vector de traslacion
 

cv2.imshow( 'resultado1', imgJaime )   
cv2.imshow( 'resultado2', imgFondo )
cv2.waitKey(0)
cv2.destroyAllWindows()     
        