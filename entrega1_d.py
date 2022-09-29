import cv2  # Se importa la libreria de OpenCV
from matplotlib import pyplot as plt  # Se importa la libreria de Matplot para plotear los histogramas

# Cargar imagen en gris
grayImg1 = cv2.imread('app1.jpeg', 0)
grayImg2 = cv2.imread('app2.jpeg', 0)

# Calcular histograma
hist_img1 = cv2.calcHist([grayImg1], [0], None, [256], [0, 256])
plt.subplot(221), plt.imshow(grayImg1, 'gray')
plt.title('Manzana_1')
plt.subplot(222), plt.hist(grayImg1.ravel(), 256, [0, 256])
plt.title('Histograma para imagen gris')

hist_img2 = cv2.calcHist([grayImg2], [0], None, [256], [0, 256])
plt.subplot(223), plt.imshow(grayImg2, 'gray')
plt.title('Manzana_2')
plt.subplot(224), plt.hist(grayImg2.ravel(), 256, [0, 256])
plt.title('Histograma para imagen gris')

#funcion para comparacion de histogramas(comparehist(h1,h2,method))
correlacion=cv2.compareHist(hist_img1,hist_img2,cv2.HISTCMP_CORREL)
print(correlacion)

metric_val = cv2.compareHist(hist_img1, hist_img2, cv2.HISTCMP_BHATTACHARYYA)
print(metric_val)

plt.show()

