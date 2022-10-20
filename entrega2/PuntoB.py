import numpy as np
import cv2

imagen=cv2.imread('2.jpg', 0)
height, width = imagen.shape[:2]

imagP_B=np.zeros((height, width), np.uint8)
imagP_A=np.zeros((height, width), np.uint8)

kernP_B=np.array([[  0  ,1/20 ,  0  ],
                  [1/20 , 9/10, 1/20],
                  [  0  , 1/20,  0  ]])

#NOTA: diseñar esta máscara
kernP_B2=np.array([[  0  ,5/10 ,  0  ],
                  [5/10 , 6/10, 5/10],
                  [  0  , 5/10,  0  ]])


kernP_A=np.array([[  1  ,-1.5,  1  ],
                  [ -1.5,  2 , -1.5],
                  [  1  ,-1.5,  1  ]])
#NOTA: diseñar esta máscara
kernP_A2=np.array([[  2  ,-3,  2  ],
                  [ -3,  5 , -3],
                  [  2  ,-3,  2  ]])
#kernP_A =  np.array([[1, -2, 1], [-2, 4, -2], [1, -2, 1]])
#kernP_B = np.ones((3, 3),np.float32)/9

imagP_B=   cv2.filter2D(imagen, ddepth=-1, kernel=kernP_B, anchor=(-1,-1))
imgAndres= cv2.filter2D(imagen, ddepth=-1,kernel=kernP_B2,anchor=(-1,-1))
imagP_A=   cv2.filter2D(imagen, ddepth=-1, kernel=kernP_A, anchor=(-1,-1))
imgStiven= cv2.filter2D(imagen, ddepth=-1, kernel=kernP_A2,anchor=(-1,-1))

cv2.imshow('comparacion      (imagen original - pasa bajas - pasa altas)', np.hstack([imagen, imagP_B,imgAndres, imagP_A,imgStiven]))
cv2.waitKey(0)
cv2.destroyAllWindows()
