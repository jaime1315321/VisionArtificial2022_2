import math 
import numpy as np 
import cv2
import matplotlib
#import pyplot as plt 

imgOriginal = cv2.imread('lena.jpg', 0)
filas, columnas = imgOriginal.shape

cv2.imshow('Imagen Original', imgOriginal)
cv2.waitKey(0)

#Rotacion con OpenCv