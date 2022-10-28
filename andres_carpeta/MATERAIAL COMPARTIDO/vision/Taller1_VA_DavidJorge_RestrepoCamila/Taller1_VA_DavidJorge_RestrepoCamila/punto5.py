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

			    elif event == cv2.EVENT_LBUTTONUP:  # Cuando se levante el boton
				print(ix, iy, x, y)

				for i in range(iy, y): ######################
				    for j in range(ix, x):
					pos = np.array([[i], [j], [1]])  # Creamos la matriz de posiciones
					translation = np.dot(transMat, pos)  # Realizamos el producto punto entre las martices
					img2[translation[0], translation[1]] = img[i, j]

				cv2.imshow('zoom X2 ', img2)
				cv2.waitKey(0)
				cv2.destroyAllWindows()

				rep1x2 = np.zeros([height*2, width*2, 3], np.uint8)
				rep1x2[:,:,0] = img2[:,:,0]
				rep1x2[:,:,1] = img2[:,:,1]
				rep1x2[:,:,2] = img2[:,:,2]
				for i in range(0, height*2):
				    for j in range(0, width*2-1):
					if rep1x2[i,j,0]==0:
					    rep1x2[i,j,0]= (img2[i,j-1,0]/2+img2[i,j+1,0]/2) #reparar errores en la matriz de azules
					if rep1x2[i,j,1]==0:
					    rep1x2[i,j,1]= (img2[i,j-1,1]/2+img2[i,j+1,1]/2) #reparar errores en la matriz de verdes
					if rep1x2[i,j,2]==0:
					    rep1x2[i,j,2]= (img2[i,j-1,2]/2+img2[i,j+1,2]/2) #reparar errores en la matriz de rojos
				rep2x2 = np.zeros([height*2, width*2, 3], np.uint8)
				rep2x2[:,:,0] = rep1x2[:,:,0]
				rep2x2[:,:,1] = rep1x2[:,:,1]
				rep2x2[:,:,2] = rep1x2[:,:,2]
				for i in range(0, height*2-1):
				    for j in range(0, width*2):
					if rep1x2[i,j,0]==0:
					    rep2x2[i,j,0]= (rep1x2[i-1,j,0]/2+rep1x2[i+1,j,0]/2) #reparar errores en la matriz de azules
					if rep2x2[i,j,1]==0:
					    rep2x2[i,j,1]= (rep1x2[i-1,j,1]/2+rep1x2[i+1,j,1]/2) #reparar errores en la matriz de verdes
					if rep2x2[i,j,2]==0:
					    rep2x2[i,j,2]= (rep1x2[i-1,j,2]/2+rep1x2[i+1,j,2]/2) #reparar errores en la matriz de rojos

				cv2.imshow('zoom X2 REPARADA ', rep2x2)
				cv2.waitKey(0)
				cv2.destroyAllWindows()       
				




				for i in range(0, height*2):
				    for j in range(0, width*2):
					pos = np.array([[i], [j], [1]])  # Creamos la matriz de posiciones
					translation = np.dot(transMat2, pos)  # Realizamos el producto punto entre las martices
					img3[translation[0], translation[1]] = rep2x2[i, j]

				cv2.imshow('zoom X4 ', img3)
				cv2.waitKey(0)
				cv2.destroyAllWindows()

				rep1x4 = np.zeros([height*4, width*4, 3], np.uint8)
				rep1x4[:,:,0] = img3[:,:,0]
				rep1x4[:,:,1] = img3[:,:,1]
				rep1x4[:,:,2] = img3[:,:,2]
				for i in range(0, height*4):
				    for j in range(0, width*4-1):
					if rep1x4[i,j,0]==0:
					    rep1x4[i,j,0]= (img3[i,j-1,0]/2+img3[i,j+1,0]/2) #reparar errores en la matriz de azules
					if rep1x4[i,j,1]==0:
					    rep1x4[i,j,1]= (img3[i,j-1,1]/2+img3[i,j+1,1]/2) #reparar errores en la matriz de verdes
					if rep1x4[i,j,2]==0:
					    rep1x4[i,j,2]= (img3[i,j-1,2]/2+img3[i,j+1,2]/2) #reparar errores en la matriz de rojos
				rep2x4 = np.zeros([height*4, width*4, 3], np.uint8)
				rep2x4[:,:,0] = rep1x4[:,:,0]
				rep2x4[:,:,1] = rep1x4[:,:,1]
				rep2x4[:,:,2] = rep1x4[:,:,2]
				for i in range(0, height*4-1):
				    for j in range(0, width*4):
					if rep1x4[i,j,0]==0:
					    rep2x4[i,j,0]= (rep1x4[i-1,j,0]/2+rep1x4[i+1,j,0]/2) #reparar errores en la matriz de azules
					if rep2x4[i,j,1]==0:
					    rep2x4[i,j,1]= (rep1x4[i-1,j,1]/2+rep1x4[i+1,j,1]/2) #reparar errores en la matriz de verdes
					if rep2x4[i,j,2]==0:
					    rep2x4[i,j,2]= (rep1x4[i-1,j,2]/2+rep1x4[i+1,j,2]/2) #reparar errores en la matriz de rojos

				cv2.imshow('zoom X4 REPARADA ', rep2x4)
				cv2.waitKey(0)
				cv2.destroyAllWindows()





				for i in range(0, height*2):
				    for j in range(0, width*2):
					pos = np.array([[i], [j], [1]])  # Creamos la matriz de posiciones
					translation = np.dot(transMat3, pos)  # Realizamos el producto punto entre las martices
					img4[translation[0], translation[1]] = rep2x4[i, j]  

				cv2.imshow('zoom X6 ', img4)
				cv2.waitKey(0)
				cv2.destroyAllWindows()

				rep1x6 = np.zeros([height*6, width*6, 3], np.uint8)
				rep1x6[:,:,0] = img4[:,:,0]
				rep1x6[:,:,1] = img4[:,:,1]
				rep1x6[:,:,2] = img4[:,:,2]
				for i in range(0, height*6):
				    for j in range(0, width*6-1):
					if rep1x6[i,j,0]==0:
					    rep1x6[i,j,0]= (img4[i,j-1,0]/2+img4[i,j+1,0]/2) #reparar errores en la matriz de azules
					if rep1x6[i,j,1]==0:
					    rep1x6[i,j,1]= (img4[i,j-1,1]/2+img4[i,j+1,1]/2) #reparar errores en la matriz de verdes
					if rep1x6[i,j,2]==0:
					    rep1x6[i,j,2]= (img4[i,j-1,2]/2+img4[i,j+1,2]/2) #reparar errores en la matriz de rojos
				rep2x6 = np.zeros([height*6, width*6, 3], np.uint8)
				rep2x6[:,:,0] = rep1x6[:,:,0]
				rep2x6[:,:,1] = rep1x6[:,:,1]
				rep2x6[:,:,2] = rep1x6[:,:,2]
				for i in range(0, height*6-1):
				    for j in range(0, width*6):
					if rep1x6[i,j,0]==0:
					    rep2x6[i,j,0]= (rep1x6[i-1,j,0]/2+rep1x6[i+1,j,0]/2) #reparar errores en la matriz de azules
					if rep2x6[i,j,1]==0:
					    rep2x6[i,j,1]= (rep1x6[i-1,j,1]/2+rep1x6[i+1,j,1]/2) #reparar errores en la matriz de verdes
					if rep2x6[i,j,2]==0:
					    rep2x6[i,j,2]= (rep1x6[i-1,j,2]/2+rep1x6[i+1,j,2]/2) #reparar errores en la matriz de rojos

				cv2.imshow('zoom X6 REPARADA ', rep2x6)
				cv2.waitKey(0)
				cv2.destroyAllWindows()








			    
			cv2.namedWindow('image')
			cv2.setMouseCallback('image', draw_circle)  # Muestro las imagenes


			while 1:
			    cv2.imshow('image', img)
			    if cv2.waitKey(1) & 0xFF == ord('q'):
				#print(ix, iy)
				# Se esperan 30ms para el cierre de la ventana o hasta que el usuario precione la tecla q
				break
			cv2.destroyAllWindows()

			# Fuente: Documentación OpenCV
