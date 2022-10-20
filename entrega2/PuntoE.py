import numpy as np
import cv2

img=cv2.imread('figuraE.png',0)
height, width = img.shape[:2]

imgF=np.zeros((height, width), np.uint8)

for i in range(1, height-1):
    for j in range(1, width-1):
        kernel=np.array([[img[i-1,j-1], img[i-1,j], img[i-1,j+1]],
                         [img[i  ,j-1], img[i  ,j], img[i  ,j+1]],
                         [img[i+1,j-1], img[i+1,j], img[i+1,j+1]]])
        mediana=np.median(kernel)
        
        imgF[i,j]=mediana

cv2.imshow('imagen filtrada', np.hstack([img, imgF]))
cv2.waitKey(0)
cv2.destroyAllWindows()