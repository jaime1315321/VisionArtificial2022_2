import numpy as np
import cv2
 
img=cv2.imread('LENA.JPG')
alto, ancho= img.shape[:2]
img1=np.zeros((alto,ancho),np.uint8)
img2=np.zeros((alto,ancho),np.uint8)
img3=np.zeros((alto,ancho),np.uint8)
 
def filtro(img):
 
 k=np.array([[0, 1, 0],[1, 2, 1],[0, 1, 0]])/6
 k1=np.array([[1, -3, 1],[-3, 8, -3],[1, -3, 1]])
 
 img1=cv2.filter2D(img, ddepth=-1,kernel=k,anchor=(-1,-1))
 img2=cv2.filter2D(img1, ddepth=-1,kernel=k1,anchor=(-1,-1))
  
 return img2
 
img3=filtro(img)
 
 
cv2.imshow('Imagen original', img )  # Mostramos las imagenes
cv2.imshow('Imagen Resultado', img3 )  # Mostramos las imagenes
cv2.waitKey(0)  # Se espera a pulsar cualquier tecla para cerrar la imagen
cv2.destroyAllWindows()  # Cierre de ventanas