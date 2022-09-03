import cv2
import numpy as np
import math

imgJaime = cv2.imread('lena.jpg', 0)
alto, ancho = imgJaime.shape[:2]
imgFondo = np.zeros((alto *2, ancho *2), np.uint8)
matrizTraslacion = np.array( [ [1, 0, 100], [0, 1, 100], [0, 0, 1] ] )


for i in range(0, alto):
    for j in range(0, ancho):
        matriz_posicion = np.array([ [ i ], [ j ], [ 1 ] ] )
        vector_translation = np.dot( matrizTraslacion , matriz_posicion ) # Crea las coordenadas finales de ese pixel
        imgFondo[ vector_translation[0], vector_translation[1] ] = imgJaime[ i, j ] #Almacenar en mi imagen fondo el nuevo vector de traslacion
 

# cv2.imshow( 'resultado1', imgJaime )   
# cv2.imshow( 'resultado2', imgFondo )
# cv2.waitKey(0)
# cv2.destroyAllWindows()     
          
        
imgFondo2 = np.zeros( (alto*2, ancho*2), np.uint8)
matriz_shearing = np.array( [ [1, -math.tan(0.17), 0], [0, 1, 0], [0, 0, 1] ] )

for i in range( 0, alto*2 ):
    for j in range( 0, ancho*2 ):
        matriz_posicion2 = np.array([ [ i ], [ j ], [ 1 ] ] )
        vector_shearing = np.dot( matriz_shearing , matriz_posicion2 ) # Crea las coordenadas finales de ese pixel
        imgFondo2[ int(vector_shearing[0]), int(vector_shearing[1]) ] = imgFondo[ i, j ] #Almacenar en mi imagen fondo el nuevo vector de traslacion

#Traslación
imgFondo3 = np.zeros( (alto*2, ancho*2), np.uint8)


cv2.imshow( 'resultadoShearing', imgFondo )
cv2.waitKey(0)
cv2.imshow( 'resultadoShearing', imgFondo2 )
cv2.waitKey(0)
cv2.destroyAllWindows()     


