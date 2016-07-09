import cv2
import numpy as np


img = cv2.imread("messi5.jpg", 1)
cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.imshow("asdf",img)

cv2.waitKey(0)
cv2.destroyAllWindows()