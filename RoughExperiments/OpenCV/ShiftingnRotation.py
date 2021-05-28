import cv2 
import numpy as np

img = cv2.imread("C:/Users/Acer/Desktop/Nature.jpeg")

#creating a transformation matrix for rectilinear translation (2*3)
mat = np.float32([[1,0,150],[0,1,200]])

img1 = cv2.warpAffine(img, mat,(img.shape[0],img.shape[1]))
cv2.imshow("Shifted",img1)

#rotation
center = img.shape[0]/2,img.shape[1]/2
angle = 90

mat = cv2.getRotationMatrix2D(center , angle, scale= 1)
img2 = cv2.warpAffine(img, mat, (img.shape[0],img.shape[1]))
cv2.imshow("Rotated",img2)

cv2.waitKey(0)
cv2.destroyAllWindows()