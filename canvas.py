import cv2
import numpy as np
canvas = np.zeros([600,600])
canvas[200:400,300:500] = 255
cv2.imshow("poster", canvas)
cv2.waitKey(0)