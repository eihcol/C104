import cv2
readImage = cv2.imread("poster.jpg")
text = "Space Ship"
cv2.putText(readImage, text, (20,250), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 1, color = (0,0,255))
cv2.imshow("poster", readImage)
cv2.waitKey(0)