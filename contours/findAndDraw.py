import cv2
import numpy as np

img = cv2.imread('binary.jpg', 1)
imgC = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imgGray, 127, 255, cv2.THRESH_BINARY_INV)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

img = cv2.drawContours(imgC, contours, -1, (0, 255, 0), 3)

cv2.imshow('contour', imgC)
cv2.waitKey(0)
cv2.destroyAllWindows()
