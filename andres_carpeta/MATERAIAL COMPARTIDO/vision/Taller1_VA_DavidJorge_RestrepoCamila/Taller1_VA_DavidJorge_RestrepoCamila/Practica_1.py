import cv2
import numpy as np
import math

img = cv2.imread('lena.jpg') #Leemos la imagen a la que se le realizarán los procedimientos
height, width = img.shape[:2] #Asignamos las dimensiones

#imagen centrada

imgCentrada=np.zeros([height*2, width*2, 3], np.uint8)
origenMat = np.array([[1, 0, 115], [0, 1, 115], [0, 0, 1]])
for i in range(0, height):
    for j in range(0, width):
        pos = np.array([[i], [j], [1]])
        traslacion = np.dot(origenMat, pos)
        imgCentrada[traslacion[0], traslacion[1]] = img[i, j]
        
        
cv2.imshow('imagen centrada', imgCentrada)
cv2.waitKey(0)
cv2.destroyAllWindows

#imagen rotada


imgrotada = np.zeros((height*2, width*2, 3), np.uint8)  # Creamos una imagen nueva para rotrar apaartir de la anterior
rotMat = np.array([[math.cos(np.pi/2), -math.sin(np.pi/2), 0], [math.sin(np.pi/2), math.cos(np.pi/2), 0], [0, 0, 1]])  # Se crea la matriz de transformacion
for i in range(0, height*2):
    for j in range(0, width*2):
        pos = np.array([[i], [j], [1]])  # Creamos la matriz de posiciones
        rotation = np.dot(rotMat, pos)  # Realizamos el producto punto entre las martices
        imgrotada[int(rotation[0]), int(rotation[1])] = imgCentrada[i, j]  # Aplicamos las nuevas posiciones para asignar los valores de la imagen

cv2.imshow('imagen rotada', imgrotada)
cv2.waitKey(0)
cv2.destroyAllWindows




#reparación intepolacion

imgReparada=np.zeros([height*2, width*2, 3], np.uint8)
imgReparada[:,:,0]=imgrotada[:,:,0]
imgReparada[:,:,1]=imgrotada[:,:,1]
imgReparada[:,:,2]=imgrotada[:,:,2]

for i in range(0, height*2-1):
    for j in range(0, width*2):

        if imgrotada[i,j,0]==0:
            imgReparada[i,j,0]= (imgrotada[i-1,j,0]/2+imgrotada[i+1,j,0]/2) #reparar errores en la matriz de azules
            
        if imgrotada[i,j,1]==0:
            imgReparada[i,j,1]= (imgrotada[i-1,j,1]/2+imgrotada[i+1,j,1]/2) #reparar errores en la matriz de verdes
        
        if imgrotada[i,j,2]==0:
            imgReparada[i,j,2]= (imgrotada[i-1,j,2]/2+imgrotada[i+1,j,2]/2) #reparar errores en la matriz de rojos
            
cv2.imshow('imagen reparada', imgReparada)
cv2.waitKey(0)
cv2.destroyAllWindows




# imagen cizallada (shearing)



imgCizallada=np.zeros([height*2, width*2, 3], np.uint8)
shearMat = np.array([[1, -math.tan(0.3), 0], [0, 1, 0], [0, 0, 1]])
for i in range(0, height*2):
    for j in range(0, width*2):
        pos = np.array([[i], [j], [1]])
        shear = np.dot(shearMat, pos)
        imgCizallada[int(shear[0]), int(shear[1])] = imgReparada[i, j]

cv2.imshow('imagen Cizallada', imgCizallada)
cv2.waitKey(0)
cv2.destroyAllWindows




# imagen trasladada

imgTrasladada=np.zeros([height*2, width*2, 3], np.uint8)
trasMat = np.array([[1, 0, 100], [0, 1, 100], [0, 0, 1]])
for i in range(0, height*2 - trasMat[0,2]):
    for j in range(0, width*2 - trasMat[1,2]):
        pos = np.array([[i], [j], [1]])
        tras = np.dot(trasMat, pos)
        imgTrasladada[tras[0], tras[1]] = imgCizallada[i, j]
        
cv2.imshow('imagen Trasladada', imgTrasladada)
cv2.waitKey(0)
cv2.destroyAllWindows

#PUNTOB
#imagen trasladada inversa

imgTrOpuesta=np.zeros([height*2, width*2, 3], np.uint8)
trasMatO=np.array([[1, 0, -100], [0, 1, -100], [0, 0, 1]])
for i in range(0, height*2):
    for j in range(0, width*2):
        pos = np.array([[i], [j], [1]])
        tras = np.dot(trasMatO, pos)
        imgTrOpuesta[tras[0], tras[1]] = imgTrasladada[i,j]

cv2.imshow('imagen Trasladada inversa', imgTrOpuesta)
cv2.waitKey(0)
cv2.destroyAllWindows


#imagen Cizallada inversa

imgCiOpuesta=np.zeros([height*2+140, width*2, 3], np.uint8)       #correcion de corte de imagen
shearMatO=np.array([[1, math.tan(0.3), 0], [0, 1, 0], [0, 0, 1]])
for i in range(0, height*2):
    for j in range(0, width*2):
        pos = np.array([[i], [j], [1]])
        shear = np.dot(shearMatO, pos)
        imgCiOpuesta[int(shear[0]), int(shear[1])] = imgTrOpuesta[i,j]


imgCiOpuesta1=np.zeros([height*2, width*2, 3], np.uint8) ########################
for i in range(0, height*2):
    for j in range(0, width*2):                           #correcion de tamaño de imagen
        imgCiOpuesta1[i,j,0]=imgCiOpuesta[i,j,0]
        imgCiOpuesta1[i,j,1]=imgCiOpuesta[i,j,1]
        imgCiOpuesta1[i,j,2]=imgCiOpuesta[i,j,2]          ##########


cv2.imshow('imagen Cizallada inversa0', imgCiOpuesta)
cv2.imshow('imagen Cizallada inversa1', imgCiOpuesta1)
cv2.waitKey(0)
cv2.destroyAllWindows

#imagen Rotada inversa

imgRoOpuesta=np.zeros([height*2, width*2, 3], np.uint8)
rotMatO=np.array([[math.cos(np.pi/2*-1), -math.sin(np.pi/2*-1), 0], [math.sin(np.pi/2*-1), math.cos(np.pi/2*-1), 0], [0, 0, 1]])
for i in range(0, height*2):
    for j in range(0, width*2):
        pos = np.array([[i], [j], [1]])
        rotacion = np.dot(rotMatO, pos)
        imgRoOpuesta[int(rotacion[0]), int(rotacion[1])] = imgCiOpuesta1[i,j]

cv2.imshow('imagen rotada inversa', imgRoOpuesta)
cv2.waitKey(0)
cv2.destroyAllWindows



#interpolacion inversa


imgReparada1 = np.zeros([height*2, width*2, 3], np.uint8)
imgReparada1[:,:,0] = imgRoOpuesta[:,:,0]
imgReparada1[:,:,1] = imgRoOpuesta[:,:,1]
imgReparada1[:,:,2] = imgRoOpuesta[:,:,2]
for i in range(0, height*2):
    for j in range(0, width*2-1):

        if imgReparada1[i,j,0]==0:
            imgReparada1[i,j,0]= (imgRoOpuesta[i,j-1,0]/2+imgRoOpuesta[i,j+1,0]/2) #reparar errores en la matriz de azules
            
        if imgReparada1[i,j,1]==0:
            imgReparada1[i,j,1]= (imgRoOpuesta[i,j-1,1]/2+imgRoOpuesta[i,j+1,1]/2) #reparar errores en la matriz de verdes
        
        if imgReparada1[i,j,2]==0:
            imgReparada1[i,j,2]= (imgRoOpuesta[i,j-1,2]/2+imgRoOpuesta[i,j+1,2]/2)


cv2.imshow('imagen reparada inversa', imgReparada1)
cv2.waitKey(0)
cv2.destroyAllWindows



#####Punto C 
#open cv

#rotacion

RotCV=cv2.getRotationMatrix2D((height, width), 90, 1)
imgRotadaCV=cv2.warpAffine(imgCentrada, RotCV, (height*2, width*2))

cv2.imshow('imagen Rotada CV', imgRotadaCV)
cv2.waitKey(0)
cv2.destroyAllWindows

#Cizallamiento

ShearCV = np.float32([[1, 0, 0], [-math.tan(0.3), 1, 0]])
imgCizalladaCV = cv2.warpAffine(imgRotadaCV, ShearCV, (height*2, width*2))

cv2.imshow('imagen Cizallada CV', imgCizalladaCV)
cv2.waitKey(0)
cv2.destroyAllWindows

#traslacion

trasCV = np.float32([[1, 0, 50], [0, 1, 50]])
imgTrasladadaCV = cv2.warpAffine(imgCizalladaCV, trasCV, (height*2, width*2))

cv2.imshow('imagen Trasladada CV', imgTrasladadaCV)
cv2.waitKey(0)
cv2.destroyAllWindows



#open CV inerso

#Traslacion

trasCVO = np.float32([[1, 0, -50], [0, 1, -50]])
imgTrasladadaCVO = cv2.warpAffine(imgTrasladadaCV, trasCVO, (height*2, width*2))

cv2.imshow('imagen Trasladada CVO', imgTrasladadaCVO)
cv2.waitKey(0)
cv2.destroyAllWindows

#Cizallamiento

shearCVO=np.float32([[1, 0, 0], [math.tan(0.3), 1, 0]])
imgCizalladaCVO=cv2.warpAffine(imgTrasladadaCVO, shearCVO, (height*2, width*2))

cv2.imshow('imagen Cizallda CVO', imgCizalladaCVO)
cv2.waitKey(0)
cv2.destroyAllWindows

#Rotacion

RotCVO=cv2.getRotationMatrix2D((height, width), -90, 1)
imgRotadaCVO=cv2.warpAffine(imgCizalladaCVO, RotCVO, (height*2, width*2))

cv2.imshow('imagen Rotada CVO', imgRotadaCVO)
cv2.waitKey(0)
cv2.destroyAllWindows



#comparacion de resultados

cv2.imshow('Comparacion punto A y C', np.hstack([imgTrasladada, imgTrasladadaCV]))
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Comparacion punto B y C', np.hstack([imgReparada1, imgRotadaCVO]))
cv2.waitKey(0)
cv2.destroyAllWindows()