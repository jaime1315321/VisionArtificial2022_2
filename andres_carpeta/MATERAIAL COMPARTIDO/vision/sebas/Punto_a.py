import numpy as np
import cv2
 
img=cv2.imread('img1.PNG',0)
img1=cv2.imread('img1.PNG',0)
alto, ancho= img.shape[:2]
imgb=np.zeros((alto,ancho),np.uint8)
imgc=np.zeros((alto,ancho),np.uint8)
imgr=np.zeros((alto,ancho),np.uint8)
imgG=np.zeros((alto,ancho),np.uint8)
 
def cambioImagen(imga):
 
   imgG=cv2.GaussianBlur(imga, (35, 35), sigmaX=0, sigmaY=0)
   
   for i in range(0, alto):
            for j in range(0, ancho):
                    imga[i,j]= imga[i,j]*0.3
                    imgb[i,j]= imgG[i,j]*0.7
                    imgc[i,j]= imga[i,j]+imgb[i,j]-34
                    
   return  imgc, imgG
 
imgr,imgf =cambioImagen(img)
 
cv2.imshow('Imagen retornada                                     Imagen leida', np.hstack([imgr,imgf,img1])) 
cv2.waitKey(0)  
cv2.destroyAllWindows() 