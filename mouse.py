import cv2 
import numpy as np

drawing = False
mode = False # si es verdadero dibuje cuadrado si es falso dibuje circulo
ix, iy = -1, -1

#Función llamado del mouse
def draw(event, x, y, flags, param):
    global ix, iy, drawing, mode
    
    if event ==cv2.EVENT_LBUTTONDOWN: # Pregunta si ha presionado el mouse
        drawing = True
        ix, iy = x, y
        
    elif event == cv2.EVENT_MOUSEMOVE:#CUando se mueve el mouse
        if drawing == True:
            if mode == True:
                cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
            else:
                cv2.circle(img, (x,y), 5, (0, 0, 255), -1) # COmando para dibujar un circulo
    
    elif event == cv2.EVENT_LBUTTONUP: #CUando se levante el mouse:
        drawing = False # que ya no se dibuje
        if mode == True:
            cv2.rectangle(img, (ix, iy), (x, y), (0, 0, 255), -1)
        else:
            cv2.circle(img, (x, y), 1, (0, 0, 255, 0))
        print(ix, iy, x, y)


#imagenRecortada = [iy:y, ix:x]


img = np.zeros((500, 500, 3), np.uint8) # crea una imagen vacia
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw) #Muestro las imagenes

while 1:
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print(ix, iy)
        #Se esperan 30 ms para que cierre la ventana o hasta que el usuario presione la tecla q
        break

cv2.destroyAllWindows()
                