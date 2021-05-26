import cv2

#reading an image
img  = cv2.imread("C:/Users/Acer/Desktop/zoom.png",0) #second param 0 for grayscale
cv2.imshow("TheMarvellousThor",img)    #to display the read image in a named window
cv2.waitKey(0)
#resizing our image
#print(img.shape) to get current dimensions of the image
width = 600
height = 800
dim = (width,height) #width,height
img = cv2.resize(img, dim)
cv2.imshow("TheMarvellousThor",img)

#writing an image
cv2.imwrite("Thor.jpg",img)

#to hold the output screen
cv2.waitKey(0)  # 0 for infinite and any other value for milliseconds
cv2.destroyAllWindows() #deallocates anything not taken care of, closes all windows


