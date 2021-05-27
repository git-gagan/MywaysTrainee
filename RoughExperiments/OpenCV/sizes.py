import cv2

img = cv2.imread("C:/Users/Acer/Desktop/Nature.jpeg")

#Changing size based on Aspect Ratio (measurement of relationship between height and width)
#For Scaling up, use Inter_cubic or Inter_linear
#For scaling down, use INTER_AREA or INTER_NEAREST
#INTERPOLATION :- Mathematical procedure applied in order to derive the value between 2 points having prescribed values
print(img.shape)
print(img.size)
scale = int(input("Number by which you wanna scale the image"))
width = int(img.shape[1]*scale/100)
height = int(img.shape[0]*scale/100)

resized_img = cv2.resize(img, (width,height), interpolation = cv2.INTER_NEAREST)
#cv2.imshow("Original",img)
cv2.imshow("Resized",resized_img)

#flipping the image
flipped_img = cv2.flip(resized_img, 1) # 1 for horizontal flip, 0 for evrtical flip, -1 for both
cv2.imshow("Flipped",flipped_img)

cv2.waitKey(0)
cv2.destroyAllWindows()