import cv2
import numpy as np

img = cv2.imread("C:/Users/Acer/Desktop/Nature.jpeg")

img = cv2.resize(img , (1080,840))
cv2.imshow("Original",img)

kernel = np.ones((5,5), dtype= "uint8")
#Changing pixel values using Kernel. When kernel is applied to every pixel in the image, we call it convolution.
#print(kernel)

#morphology operations
erosion = cv2.erode(img, kernel, iterations = 1)
#Erosion is removing pixels from foreground object
cv2.imshow("Eroded",erosion)

dilation = cv2.dilate(img, kernel, iterations= 1)
#Dilation means Adding pixels
cv2.imshow("Dilation",dilation)

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
#Erosion Followed by dilation
cv2.imshow("Opening",opening)

closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
#dilation Followed by Erosion
cv2.imshow("Closing",closing)

grad = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
#Difference between erosion and dilation
cv2.imshow("Gradient",grad)

top_hat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
#Difference between input and output image
cv2.imshow("top_hat", top_hat)

black_hat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
#Difference between closing of input image and input image
cv2.imshow("black_hat", black_hat)

cv2.waitKey(0)
cv2.destroyAllWindows()