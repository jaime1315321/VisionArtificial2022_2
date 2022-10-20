import numpy as np
import cv2
 
camara=cv2.VideoCapture(0)
inicio=1
 
while True:
    # Captura cuadro a cuadro
    _, frame = camara.read()
    alto,ancho=frame.shape[:2]
    
    
    if inicio==1:
      referencia=frame
      hist = cv2.calcHist([referencia], [0], None, [256], [0, 256])
      inicio=0
    
    hist2 = cv2.calcHist([frame], [0], None, [256], [0, 256])
    intruso= cv2.compareHist(hist, hist2, cv2.HISTCMP_CORREL)
                  
    if intruso<=0.7:
        print('Hay un intruso')
        
    
    cv2.imshow('video2', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): # Se esperan 30ms para el cierre de la ventana o hasta que el usuario precione la tecla q
        break


 
camara.release()
cv2.destroyAllWindows()