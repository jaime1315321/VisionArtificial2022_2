import cv2
import numpy as np


drawing = False  # Verdadero si el mouse es presionado
mode = True  # Si es verdadero, dibuje un rectangulo, de lo contrario un circulo
ix, iy = -1, -1

img = cv2.imread('parcial.png')  # Leemos la imagen original
height, width = img.shape[:2]
img2 = np.zeros((height, width, 3), np.uint8) # Creamos una imagen nueva
# cv2.imshow('Imagen',img) # Se aplica filtro y luego se umbraliza la imagen
# cv2.waitKey(0)


#######################################FUNCION############################

def draw_circle(event, x, y, flags, param): # Se declara la funcion
    global ix, iy, drawing, mode  # Defino unas variables globales

    if event == cv2.EVENT_LBUTTONDOWN:  # Se pregunta si se ha presionado el mouse
        drawing = True  # En caso de ser verdado se asigna una variable boleana
        ix, iy = x, y  # Almacenamos la poscion incial en las variales

    elif event == cv2.EVENT_LBUTTONUP:  # Cuando se levante el boton
        print(ix, iy, x, y)
        print("ver resultado arriba")

        for i in range(iy, y): ######################
            for j in range(ix, x):
                imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # Se convierte la imagen de color a una imagen en escala de grises. 
                imgray = cv2.GaussianBlur(imgray, (1, 1), 3) # Se aplica un filtro gausiano para reducir el ruido en la imagen de salida
                t, img_umbral = cv2.threshold(imgray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_TRIANGLE) # Umbralizacion con operador binario inverso

                imgc = cv2.medianBlur(img_umbral, 7)

                cv2.imshow('Imagen umbralizada con filtro', imgc)
                cv2.waitKey(0)
                ###


                contours, hierarchy = cv2.findContours(imgc, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # Obtenemos los contornos
                img2[i,j] = img[i,j]

                # cv2.drawContours(img,contours,-1,(125,125,0),2,cv2.LINE_AA) # Dibujamos los contornos
                # cv2.imshow('Imagen original con contornos', img) #Muestra la imagen original con contornos
                # cv2.waitKey(0)

        cv2.drawContours(img,contours,-1,(125,125,0),2,cv2.LINE_AA) # Dibujamos los contornos
        cv2.imshow('Imagen original con contornos', img2) #Muestra la imagen original con contornos
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
cv2.namedWindow('image')
cv2.setMouseCallback('imageSTEVEN', draw_circle)  # Muestro las imagenes

while 1:
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        #print(ix, iy)
        # Se esperan 30ms para el cierre de la ventana o hasta que el usuario precione la tecla q
        break
cv2.destroyAllWindows()