import cv2
import matplotlib

imgJaime = cv2.imread('lena.jpg', 0)
alto, ancho = imgJaime.shape[:2]
cols, rows = imgJaime.shape

rotacionJaime = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
dst = cv2.warpAffine(imgJaime, rotacionJaime, (cols, rows))

cv2.imshow('Rotación',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
