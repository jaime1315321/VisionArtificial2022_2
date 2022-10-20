import cv2
import numpy as np

cap = cv2.VideoCapture(0)  # Inicio de captura

while 1:
    _, frame = cap.read()  # Almacenamiento del frame
    height, width = frame.shape[:2]  # Captura de las dimensiones
    segImg1 = np.zeros(frame.shape, np.uint8)  # Creacion de la imagen vacia para la segmentacion 1
    segImg2 = np.zeros((height, width), np.uint8)# Creacion de la imagen vacia para la segmentacion 2
    segImg3 = np.zeros((height, width), np.uint8)# Creacion de la imagen vacia para la segmentacion 3  
    segImg4 = np.zeros((height, width), np.uint8)# Creacion de la imagen vacia para la segmentacion 4
    segImg5 = np.zeros((height, width), np.uint8)# Creacion de la imagen vacia para la segmentacion 5
    segImg6 = np.zeros((height, width), np.uint8)# Creacion de la imagen vacia para la segmentacion 6
    segImg7 = np.zeros((height, width), np.uint8)# Creacion de la imagen vacia para la segmentacion 7 
    conv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)# Creacion de la imagen vacia para la segmentacion 8
    lower = np.array([0, 170, 0])  # Limite inferior color rojo
    upper = np.array([7, 255, 255])  # Limite superior color rojo
    lower1 = np.array([40, 190, 0])  # Limite inferior color verde
    upper1 = np.array([70, 255, 255])  # Limite superior color verde
    lower2 = np.array([100, 200, 0])  # Limite inferior color azul
    upper2 = np.array([110, 255, 255])  # Limite superior color azul 
    lower3 = np.array([20, 210, 0])  # Limite inferior color amarillo
    upper3 = np.array([30, 255, 255])  # Limite superior color amarillo
    lower4 = np.array([110, 100, 0])  # Limite inferior color morado
    upper4 = np.array([130, 255, 255])  # Limite superior color morado
    lower5 = np.array([10, 180, 180])  # Limite inferior color naranja
    upper5 = np.array([20, 255, 255])  # Limite superior color naranja
    lower6 = np.array([130, 150, 0])  # Limite inferior color rosa
    upper6 = np.array([160, 255, 255])  # Limite superior color rosa
    # Creaion de la mascara con los rangos a segmentar
    mask = cv2.inRange(conv, lower, upper)  
    mask2 = cv2.inRange(conv, lower1, upper1)
    mask3 = cv2.inRange(conv, lower2, upper2)
    mask4 = cv2.inRange(conv, lower3, upper3)
    mask5 = cv2.inRange(conv, lower4, upper4)
    mask6 = cv2.inRange(conv, lower5, upper5)
    mask7 = cv2.inRange(conv, lower6, upper6)
    #Segmentación con las mascaras 
    segImg1 = cv2.bitwise_and(conv, conv, mask=mask)  
    segImg2 = cv2.bitwise_and(conv, conv, mask=mask2)
    segImg3 = cv2.bitwise_and(conv, conv, mask=mask3)
    segImg4 = cv2.bitwise_and(conv, conv, mask=mask4)
    segImg5 = cv2.bitwise_and(conv, conv, mask=mask5)
    segImg6 = cv2.bitwise_and(conv, conv, mask=mask6)
    segImg7 = cv2.bitwise_and(conv, conv, mask=mask7)
    #Se muestran las imagenes resultado 
    cv2.imshow('Original', frame)  
    cv2.imshow('rojo', segImg1)  
    cv2.imshow('verde', segImg2)  
    cv2.imshow('azul', segImg3)
    cv2.imshow('amarillo', segImg4)
    cv2.imshow('morado', segImg5)
    cv2.imshow('naranja', segImg6)
    cv2.imshow('rosa', segImg7)
   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()