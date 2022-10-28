import cv2
import numpy as np

drawing = False  # Verdadero si el mouse es presionado
mode = False  # Si es verdadero, dibuje un rectangulo, de lo contrario un circulo
ix, iy = -1, -1

img = cv2.imread('lena.jpg')
height, width = img.shape[:2]  # Obtenemos sus dimensiones
img2 = np.zeros((height*2, width*2, 3), np.uint8) # Creamos una imagen nueva
img3 = np.zeros((height*4, width*4, 3), np.uint8) 
img4 = np.zeros((height*6, width*6, 3), np.uint8) 
transMat = np.array([[2, 0, 0], [0, 2, 0], [0, 0, 1]])  # Creamos la matriz de transformacion
transMat2 = np.array([[2, 0, 0], [0, 2, 0], [0, 0, 1]]) 
transMat3 = np.array([[3, 0, 0], [0, 3, 0], [0, 0, 1]]) 
#  funcion de llamado del mouse
def draw_circle(event, x, y, flags, param): # Se declara la funcion
    global ix, iy, drawing, mode  # Defino unas variables globales

    if event == cv2.EVENT_LBUTTONDOWN:  # Se pregunta si se ha presionado el mouse
        drawing = True  # En caso de ser verdado se asigna una variable boleana
        ix, iy = x, y  # Almacenamos la poscion incial en las variales
        print("click")

    elif event == cv2.EVENT_LBUTTONUP:  # Cuando se levante el boton
        print(ix, iy, x, y)
        print("ver resultado arriba")

        for i in range(iy, y): ######################
            for j in range(ix, x):
                pos = np.array([[i], [j], [1]])  # Creamos la matriz de posiciones
                translation = np.dot(transMat, pos)  # Realizamos el producto punto entre las martices
                img2[translation[0], translation[1]] = img[i, j]

        cv2.imshow('zoom X2 ', img2)
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

# Fuente: Documentación OpenCV