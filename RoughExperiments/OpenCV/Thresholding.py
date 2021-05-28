import cv2

img = cv2.imread("C:/Users/Acer/Desktop/zoom.png")
#cv2.imshow("Thor",img)

#Thresholding at most basic level is to convert everything to black or white based upon threshold value for image analysis
#if given pixel value is less then thres, its taken as 0, otherwise max value
_ , thres_img = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
cv2.imshow("Threshed",thres_img)

cv2.waitKey(0)
cv2.destroyAllWindows()