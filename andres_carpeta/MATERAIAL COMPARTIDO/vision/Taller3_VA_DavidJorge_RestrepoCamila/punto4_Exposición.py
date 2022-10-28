import cv2
import numpy as np

captura=cv2.VideoCapture(0)

#'variable'=np.array(['H','S','V'],np.uint8)
redBajo1=np.array([0,130,40],np.uint8)
redAlto1=np.array([3,255,255],np.uint8)
# //#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#   CIELA ROJO   /#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#
redBajo1_CIELA=np.array([23,139,132],np.uint8)
redAlto1_CIELA=np.array([138,286,195],np.uint8)

redBajo2=np.array([170,50,40],np.uint8)
redAlto2=np.array([179,255,255],np.uint8)
# //#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#   CIELA  ROJO 2  /#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#
redBajo2_CIELA=np.array([33,133,127],np.uint8)
redAlto2_CIELA=np.array([136,288,193],np.uint8)

blueBajo=np.array([100,100,20],np.uint8)
blueAlto=np.array([140,255,255],np.uint8)
# //#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#   CIELA  Azul  /#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#
blueBajo_CIELA=np.array([12,126,126],np.uint8)
blueAlto_CIELA=np.array([119,215,44],np.uint8)

yellowBajo=np.array([18,50,75],np.uint8)
yellowAlto=np.array([24,255,255],np.uint8)
# //#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#   CIELA  Amarillo  /#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#
yellowBajo_CIELA=np.array([69,135,130],np.uint8)
yellowAlto_CIELA=np.array([138,285,195],np.uint8)

greenBajo=np.array([40,50,75],np.uint8)
greenAlto=np.array([80,255,255],np.uint8)
# //#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#   CIELA  vERDE  /#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#
greenBajo_CIELA=np.array([79,123,176],np.uint8)
greenAlto_CIELA=np.array([277,59,155],np.uint8)

celestBajo=np.array([78,50,50],np.uint8)
celestAlto=np.array([95,255,255],np.uint8)
# //#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#   CIELA  celeste  /#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#
celestBajo_CIELA=np.array([50,122,131],np.uint8)
celestAlto_CIELA=np.array([201,100,95],np.uint8)

magentBajo=np.array([130,50,50],np.uint8)
magentAlto=np.array([170,255,255],np.uint8)
# //#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#   CIELA  celeste  /#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#
magentBajo_CIELA=np.array([43,132,122],np.uint8)
magentAlto_CIELA=np.array([138,210,157],np.uint8)



while 1:
    _,frame=captura.read()
    frameHSV=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # conversion de espacio de color BGR A HSV
    frame_CIELA = cv2.cvtColor(frame, cv2.COLOR_BGR2Lab)
    
    
    
    maskRed1=cv2.inRange(frameHSV,redBajo1,redAlto1)
    maskRed2=cv2.inRange(frameHSV,redBajo2,redAlto2)
    
    maskRed1_CIELA=cv2.inRange(frame_CIELA,redBajo1_CIELA,redAlto1_CIELA)
    maskRed2_CIELA=cv2.inRange(frame_CIELA,redBajo2_CIELA,redAlto2_CIELA)
    
    maskBlue=cv2.inRange(frameHSV,blueBajo,blueAlto)
    maskBlue_CIELA=cv2.inRange(frame_CIELA,blueBajo_CIELA,blueAlto_CIELA)
        
    maskYellow=cv2.inRange(frameHSV,yellowBajo,yellowAlto)
    maskYellow_CIELA=cv2.inRange(frame_CIELA,yellowBajo_CIELA,yellowAlto_CIELA)

    maskGreen=cv2.inRange(frameHSV,greenBajo,greenAlto)
    maskGreen_CIELA=cv2.inRange(frame_CIELA,greenBajo_CIELA,greenAlto_CIELA)
    
    maskCelest=cv2.inRange(frameHSV,celestBajo,celestAlto)
    maskCelest_CIELA=cv2.inRange(frame_CIELA,celestBajo_CIELA,celestAlto_CIELA)
        
    maskMagent=cv2.inRange(frameHSV,magentBajo,magentAlto)
    maskMagent_CIELA=cv2.inRange(frame_CIELA,magentBajo_CIELA,magentAlto_CIELA)
    



    maskTotalRed=cv2.add(maskRed1,maskRed2)
    maskTotalRed_CIELA=cv2.add(maskRed1_CIELA,maskRed2_CIELA)

    maskRealRed=cv2.bitwise_and(frame,frame, mask=maskTotalRed)
    maskRealBlue=cv2.bitwise_and(frame,frame, mask=maskBlue)

    maskRealYellow=cv2.bitwise_and(frame, frame, mask=maskYellow)
    maskRealYellow_CIELA=cv2.bitwise_and(frame_CIELA, frame_CIELA, mask=maskYellow_CIELA)

    maskRealGreen=cv2.bitwise_and(frame,frame, mask=maskGreen)
    maskRealGreen_CIELA=cv2.bitwise_and(frame_CIELA,frame_CIELA, mask=maskGreen_CIELA)
    
    maskRealCelest=cv2.bitwise_and(frame,frame,mask=maskCelest)
    maskRealCelest_CIELA=cv2.bitwise_and(frame_CIELA,frame_CIELA,mask=maskCelest_CIELA)
    
    maskRealMagent=cv2.bitwise_and(frame,frame,mask=maskMagent)
    maskRealMagent_CIELA=cv2.bitwise_and(frame_CIELA,frame_CIELA,mask=maskMagent_CIELA)

    

    cv2.imshow('mask Rojo',maskTotalRed)
    cv2.imshow('mask Rojo_CIELA',maskTotalRed_CIELA)
    
    cv2.imshow('mask azul',maskBlue)
    cv2.imshow('mask azul_CIELA',maskBlue_CIELA)
    
    cv2.imshow('mask amarillo',maskYellow)
    cv2.imshow('mask amarillo_CIELA',maskYellow_CIELA)
    
    cv2.imshow('mask verde', maskGreen)
    cv2.imshow('mask verde_CIELA', maskGreen_CIELA)
    
    cv2.imshow('mask celeste',maskCelest)
    cv2.imshow('mask celeste_CIELA',maskCelest_CIELA)
    
    cv2.imshow('mask magenta',maskMagent)
    cv2.imshow('mask magenta_CIELA',maskMagent_CIELA)
    
    cv2.imshow('maskReal_CELESTE',maskRealCelest)
    cv2.imshow('maskReal_CELESTE_CIELA',maskRealCelest_CIELA)
    
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

captura.release()
cv2.destroyAllWindows()
