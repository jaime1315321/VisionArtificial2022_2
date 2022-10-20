import cv2
import numpy as np

drawing = False
mode = False
ix, iy = -1, -1

img = cv2.imread('lena.jpg')
height, width = img.shape[:2]  # Obtenemos sus dimensiones
img2 = np.zeros((height, width, 3), np.uint8)  # Creamos una imagen nueva

#  funcion de llamado del mouse
def draw_circle(event, x, y, flags, param): # Se declara la funcion
    global ix, iy, drawing, mode  # Defino unas variables globales

    if event == cv2.EVENT_LBUTTONDOWN:  # Se pregunta si se ha presionado el mouse
        drawing = True  # En caso de ser verdado se asigna una variable boleana
        ix, iy = x, y  # Almacenamos la poscion incial en las variales
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            img2[y,x,0] = img[y,x,2]
            img2[y,x,2] = img[y,x,1]
            img2[y,x,1] = img[y,x,0]
    elif event == cv2.EVENT_LBUTTONUP:  # Cuando se levante el boton
        drawing = False
        
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)  # Muestro las imagenes


while 1:
    cv2.imshow('image', np.hstack([img, img2]))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        #print(ix, iy)
        # Se esperan 30ms para el cierre de la ventana o hasta que el usuario precione la tecla q
        break
cv2.destroyAllWindows()