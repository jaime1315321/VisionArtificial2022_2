import cv2
import numpy as np

cap = cv2.VideoCapture(0)  # Inicio de captura


while(1):

    #capturas
    _, capturaAnterior = cap.read()  
    grayAnterior=cv2.cvtColor(capturaAnterior, cv2.COLOR_BGR2GRAY)
    _, capturaActual = cap.read()
    grayActual=cv2.cvtColor(capturaActual, cv2.COLOR_BGR2GRAY)

    #imagen restada/binaria 

    imgResta=cv2.subtract(grayAnterior,grayActual)
    _, imgTH=cv2.threshold(imgResta, 70, 255, cv2.THRESH_BINARY)


    MediaimgTH=np.mean(imgTH)
    #print(MediaimgTH)

    if MediaimgTH !=0:
        #intruso=True
        print('intruso')
    else:
        print('0')


    cv2.imshow('imagen anterior', grayAnterior) 
    cv2.imshow('imagen posterior', grayActual) 
    cv2.imshow('imagen diferencial', imgResta)
    #cv2.imshow('imagen binaria', imgTH)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()