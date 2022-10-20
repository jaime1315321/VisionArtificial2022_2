import numpy as np
import cv2

from sklearn.model_selection import train_test_split #Librerias para leer la red SKLEARN
from sklearn import svm #Librerias para leer la red SKLEARN

dataset=np.loadtxt('trabajo final\OneDrive_2022-05-29\datos.txt', delimiter=',') #LEER BASE DE DATOS
np.random.shuffle(dataset) #RECONOCIMIENTO DE BASE DE DATOS Y SE DESORDENAN DATOS PARA QUE SE PUEDA ENTRENAR POR SI SOLA LA RED
data, labels=dataset[:, 0:17], dataset[:, 17] #DATA.. CARACTERIASTICAS LABELS ETIQUETA ... RESULTADO DE TODO INDICA SI ES FALSO O NO FINAL 0 FALSO 1 VERDAD

data_train, data_test, labels_train, labels_test = train_test_split(data, labels, test_size=0.20, random_state=10) #CUATRO VARTIABLES, DATOS DE ENTRENAMIENTO, DE TESTEO, PARA PODER RECONOCER ASI CUALES FALSA Y CUAL NO
# DATA: DATOS, LABELS: TESTEO, TEST SIZE: PORCENTAJE DE ADQUISICIÓN DE DATOS, RANDOM: TIEMPO
clf=svm.SVC(kernel='rbf')
clf.fit(data_train, labels_train) #SEPARA DATOS DE ETIQUETAS
print("porcentaje de efectivdad: ", clf.score(data_test, labels_test)) # PERMITE Q  UE PORCENTAJE ES EFECTIVO, QUE TAN BUENO ES PREDICIENDO
carac=[] #LISTA DE VARIABLE

camara=cv2.VideoCapture('http://192.168.1.67:4747/video')
while True:
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

            epsilon=0.1*cv2.arcLength(c,True)
            aprox=cv2.approxPolyDP(c,epsilon,True)
            #print(len(aprox))

            x,y,w,h= cv2.boundingRect(aprox)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),1)
            relacion=w/h



            ImgCrop1=ImgGris[y:y+h,x:x+w]  #BILLETE
            #cv2.imshow('CROP', ImgCrop1)

            cara=ImgCrop1[30:150,10:130]  #CARA
            #cv2.imshow('cara', cara)


            _,BilleBinario=cv2.threshold(ImgCrop1, 120, 255, cv2.THRESH_BINARY) 
            cv2.imshow('billete binario', BilleBinario)
            _,CaraBinaria=cv2.threshold(cara, 180, 255, cv2.THRESH_BINARY)
            cv2.imshow('cara Binaria', CaraBinaria)

            humm = cv2.HuMoments(cv2.moments(BilleBinario)).flatten()
            hCara=cv2.HuMoments(cv2.moments(CaraBinaria)).flatten()
            promCara=np.mean(CaraBinaria, dtype=np.float32)
            carac=np.array([humm[0],humm[1],humm[2],humm[3],humm[4],humm[5],humm[6],hCara[0],hCara[1],hCara[2],hCara[3],hCara[4],hCara[5],hCara[6],promCara,area,relacion])
            carac=carac.reshape(1,-1)
            signal= clf.predict(carac)

            if signal == 0:
                print("EL BILLETE ES FALSO")
            elif signal == 1:
                print("correcto")

    cv2.imshow('frame', frame)
    cv2.imshow('imgen gris',ImgGris)
    #cv2.imshow('filtro gaussiano', FGauss)
    #cv2.imshow('IMAGEN BINARIA',thres)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
camara.release()

            