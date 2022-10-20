import numpy as np 
import cv2 
from matplotlib import pyplot as plt


img=cv2.imread('lena.jpg',0)
alto,ancho=img.shape[:2]

img1= np.fft.fft2(img)
fshift = np.fft.fftshift(img1)

img1 = 20*np.log(np.abs(fshift))

y,x= int(alto/2), int(ancho/2)
fshift[y-30:y+30, x-30:x+30] = 0

f_ishift = np.fft.ifftshift(fshift)
img2 = np.fft.ifft2(f_ishift) 
img2=np.abs(img2)
f_ishift=np.abs(f_ishift)



plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(132),plt.imshow(np.abs(fshift), cmap = 'gray')
plt.title('Filtro'), plt.xticks([]), plt.yticks([])

plt.subplot(133),plt.imshow(img2,cmap = 'gray')
plt.title('Transformada inversa'), plt.xticks([]), plt.yticks([])

plt.show()