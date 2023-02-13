import cv2
readImage = cv2.imread("butterfly.jpg")
greyImage = cv2.cvtColor(readImage, cv2.COLOR_BGR2GRAY)
print(greyImage)
cv2.imshow("butterfly image", greyImage)
cv2.waitKey(0)