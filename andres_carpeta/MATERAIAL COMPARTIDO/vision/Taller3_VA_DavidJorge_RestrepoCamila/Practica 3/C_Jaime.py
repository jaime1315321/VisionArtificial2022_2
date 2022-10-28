import cv2
import numpy as np

cap=cv2.VideoCapture(0)


while 1:
    _,frame=cap.read()

    imgray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    imgray = cv2.GaussianBlur(imgray, (7, 7), 3) # Se aplica un filtro gausiano para reducir el ruido en la imagen de salida
    t, img_umbral = cv2.threshold(imgray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_TRIANGLE) # Umbralizacion con operador binario inverso




    contornos,_=cv2.findContours(img_umbral, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    

    cv2.drawContours(frame,contornos,-1,(125,125,0),2,cv2.LINE_AA) # Dibujamos los contornos
    cv2.imshow('Imagen con contornos',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows
