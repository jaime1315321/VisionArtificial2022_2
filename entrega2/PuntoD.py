import cv2
import numpy as np


#################   figura 1   ################### (ruido gaussiano)
Figura1=cv2.imread('figuras/img1.png', 0)
height, width = Figura1.shape[:2]

# Filtro Pasa bajas


kern1 = np.ones((3, 3),np.float32)/9
Figura1PB=np.zeros((height, width), np.uint8)
Figura1PB=cv2.filter2D(Figura1, ddepth=-1, kernel=kern1, anchor=(-1, -1))

# Filtro pasa altas

kern2 = np.array([[1, -2, 1], [-2, 4, -2], [1, -2, 1]])
Figura1PA=np.zeros((height, width), np.uint8)
Figura1PA=cv2.filter2D(Figura1, ddepth=-1, kernel=kern2, anchor=(-1, -1))

# Filtro sharpen

kern3 = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
Figura1S=np.zeros((height, width), np.uint8)
Figura1S=cv2.filter2D(Figura1, ddepth=-1, kernel=kern3, anchor=(-1, -1))

# Filtro Mediana 

Figura1M = cv2.medianBlur(Figura1, 5)

# Filtro gaussiano 

Figura1G = cv2.GaussianBlur(Figura1, (3, 3), sigmaX=10, sigmaY=0)

# COMPARACION

cv2.imshow(' Figura 1', Figura1)
cv2.imshow('comparacion de filtros Figura 1 (Pasa baja - Pasa alta - Mediana - Guassiana - Sharpen)', np.hstack([Figura1PB, Figura1PA, Figura1M, Figura1G, Figura1S]))
cv2.waitKey(0)
cv2.destroyAllWindows()





#################   figura 2   ################### (ruido de sal)
Figura2=cv2.imread('figuras/img2.png', 0)
height, width = Figura2.shape[:2]

# Filtro Pasa bajas


kern1 = np.ones((3, 3),np.float32)/9
Figura2PB=np.zeros((height, width), np.uint8)
Figura2PB=cv2.filter2D(Figura2, ddepth=-1, kernel=kern1, anchor=(-1, -1))

# Filtro pasa altas

kern2 = np.array([[1, -2, 1], [-2, 4, -2], [1, -2, 1]])
Figura2PA=np.zeros((height, width), np.uint8)
Figura2PA=cv2.filter2D(Figura2, ddepth=-1, kernel=kern2, anchor=(-1, -1))

# Filtro sharpen

kern3 = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
Figura2S=np.zeros((height, width), np.uint8)
Figura2S=cv2.filter2D(Figura2, ddepth=-1, kernel=kern3, anchor=(-1, -1))

# Filtro Mediana 

Figura2M = cv2.medianBlur(Figura2, 5)

# Filtro gaussiano 

Figura2G = cv2.GaussianBlur(Figura2, (3, 3), sigmaX=10, sigmaY=0)

# COMPARACION

cv2.imshow(' Figura 2', Figura2)
cv2.imshow('comparacion de filtros Figura 2 (Pasa baja - Pasa alta - Mediana - Guassiana - Sharpen)', np.hstack([Figura2PB, Figura2PA, Figura2M, Figura2G, Figura2S]))
cv2.waitKey(0)
cv2.destroyAllWindows()





#################   figura 3   ################### (ruido sal y pimienta)
Figura3=cv2.imread('figuras/img3.png', 0)
height, width = Figura3.shape[:2]

# Filtro Pasa bajas


kern1 = np.ones((3, 3),np.float32)/9
Figura3PB=np.zeros((height, width), np.uint8)
Figura3PB=cv2.filter2D(Figura3, ddepth=-1, kernel=kern1, anchor=(-1, -1))

# Filtro pasa altas

kern2 = np.array([[1, -2, 1], [-2, 4, -2], [1, -2, 1]])
Figura3PA=np.zeros((height, width), np.uint8)
Figura3PA=cv2.filter2D(Figura3, ddepth=-1, kernel=kern2, anchor=(-1, -1))

# Filtro sharpen

kern3 = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
Figura3S=np.zeros((height, width), np.uint8)
Figura3S=cv2.filter2D(Figura3, ddepth=-1, kernel=kern3, anchor=(-1, -1))

# Filtro Mediana 

Figura3M = cv2.medianBlur(Figura3, 5)

# Filtro gaussiano 

Figura3G = cv2.GaussianBlur(Figura3, (3, 3), sigmaX=10, sigmaY=0)

# COMPARACION

cv2.imshow(' Figura 3', Figura3)
cv2.imshow('comparacion de filtros Figura 3 (Pasa baja - Pasa alta - Mediana - Guassiana - Sharpen)', np.hstack([Figura3PB, Figura3PA, Figura3M, Figura3G, Figura3S]))
cv2.waitKey(0)
cv2.destroyAllWindows()