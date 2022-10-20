import numpy as np
import cv2
import csv 

#camara=cv2.VideoCapture('http://192.168.1.67:4747/video') 
carac=[]
chart=[] 

path="D:\Nueva carpeta (2)\RECUPERADO\Universidad\Vision" #ubicacion de capturas registradas
cont=0


while 1:
    ret, frame= camara.read()
    ImgGris=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    FGauss=cv2.GaussianBlur(ImgGris, (3,3), 0)
    _,thres = cv2.threshold(FGauss, 90, 255, cv2.THRESH_BINARY)


    contornos,_=cv2.findContours(thres, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for c in contornos:
        area=cv2.contourArea(c)
        if area>50000 and area<130000 :
            nuevoContorno=cv2.convexHull(c)
            cv2.drawContours(frame,[nuevoContorno],0,(255,255,0),3)

            epsilon=0.1*cv2.arcLength(c,True) #PARAMETRO QUE AYUDA A DETECTAR DIRECTAMENTE EL RECTANGULO Y NO LAS SILUETAS GENERADAS
            aprox=cv2.approxPolyDP(c,epsilon,True) 
            #print(len(aprox))

            x,y,w,h= cv2.boundingRect(aprox)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),1) #segmentacion del billete, COORDENDAS EN EL PLANO
            relacion=w/h #SI ES VERDADERO EL CUADRARO ES UN POCO MAS ANGOSTO Y SI ES FALSO ES MAS LARGO, ESTO ES UNA CARACTERÍSTICA QUER SE TIENE EN CUENTA PARA LA BASE DE DATOS


            ImgCrop1=ImgGris[y:y+h,x:x+w]  #BILLETE MODO BINARIO
            #cv2.imshow('CROP', ImgCrop1)

            cara=ImgCrop1[30:150,10:130]  #CARA 
            #cv2.imshow('cara', cara)


            _,BilleBinario=cv2.threshold(ImgCrop1, 120, 255, cv2.THRESH_BINARY)
            cv2.imshow('billete binario', BilleBinario)
            _,CaraBinaria=cv2.threshold(cara, 180, 255, cv2.THRESH_BINARY)
            cv2.imshow('cara Binaria', CaraBinaria)

            humm = cv2.HuMoments(cv2.moments(BilleBinario)).flatten()
            hCara=cv2.HuMoments(cv2.moments(CaraBinaria)).flatten()
            promCara=np.mean(CaraBinaria, dtype=np.float32) # SE BINARIZA PARA HALLAR CARACTERISTICAS ES UN PROMEDIO

            if cv2.waitKey(1) & 0xFF ==ord('c'): # SI SE OPRIME C SE GUARDA LA IMAGEN Y EMPIEZA CONTEO DE IMAGENES
                cv2.imwrite(path + str(cont) + '.jpg', frame)
                cont=cont+1
                etiqueta=int(input('ingrese la etiqueta: '))
                chart=[humm[0],humm[1],humm[2],humm[3],humm[4],humm[5],humm[6],hCara[0],hCara[1],hCara[2],hCara[3],hCara[4],hCara[5],hCara[6],promCara, area, relacion, etiqueta] #RELACION ANCHO CON ALTO DEL BILLETE ES UN INDICADOR
                carac.append(chart) 
                print(carac)

    cv2.imshow('frame', frame)
    cv2.imshow('imgen gris',ImgGris)
    #cv2.imshow('filtro gaussiano', FGauss)
    #cv2.imshow('IMAGEN BINARIA',thres)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
camara.release()

test=open("lista", 'w')
wr=csv.writer(test, dialect='excel')
for item in carac:
    wr.writerow(item)

cv2.waitKey(0)
cv2.destroyAllWindows()