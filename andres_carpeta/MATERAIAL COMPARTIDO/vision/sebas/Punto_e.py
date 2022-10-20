import numpy as np
import cv2
 
img=cv2.imread('img4.png',0)
alto,ancho=img.shape[:2]
img1=np.zeros([alto, ancho], np.uint8)
img2=np.zeros([alto, ancho], np.uint8)
img3=np.zeros([alto, ancho], np.uint8)
k = np.array([[0, 1, 0], [1, 6, 1], [0, 1, 0]])/10
k1 = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
img1[:,:] = img[:,:]
 
def filtros(img, kern, kern1):
    
    for x in range(1, alto-1 ):
          for y in range(1, ancho-1 ):
           
            v=np.array([[img[x-1,y-1], img[x-1,y], img[x-1,y+1]], [img[x,y-1], img[x,y], img[x,y+1]], [img[x+1,y-1], img[x+1,y], img[x+1,y+1]]])
            mediana = np.median(v)
            img1[x ,y]=int(mediana)
        
    for x in range(1, alto-1 ):
        for y in range(1, ancho-1 ):
            
              v=np.array([[img1[x-1,y-1], img1[x-1,y], img1[x-1,y+1]], [img1[x,y-1], img1[x,y], img1[x,y+1]], [img1[x+1,y-1], img1[x+1,y], img1[x+1,y+1]]])
              mediana = np.median(v)
              img1[x ,y]=int(mediana) 
 
    for x in range(0, alto-2):
          for y in range(0, ancho-1):
            fila1=0
            fila2=0
            fila3=0     
            for k in range(0,2):
                 m1=img1[x,y+k]*kern[0,k]
                 fila1=m1+fila1
                 
                 m2=img1[x+1,y+k]*kern[1,k]
                 fila2=m2+fila2
 
                 m3=img1[x+2,y+k]*kern[2,k]
                 fila3=m3+fila3
 
                 pixel=fila1+fila2+fila3
                 img2[x,y]=pixel
 
    img3= cv2.filter2D(img2, ddepth=-1, kernel=kern1, anchor=(-1, -1)) # Aplicamos el kernel a la imagen con la funcion filter2D 
    
    return img3

img3=filtros(img, k, k1)
               
cv2.imshow('Imagen original                                    Imagen con filtro', np.hstack([img,img1,img2,img3 ]))  # Mostramos las imagenes
cv2.waitKey(0)  # Se espera a pulsar cualquier tecla para cerrar la imagen
cv2.destroyAllWindows()  # Cierre de ventanas