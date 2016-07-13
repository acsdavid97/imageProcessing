import cv2
import numpy as np

# Rotating by 90 degrees
img = cv2.imread("messi5.jpg")
rows, cols = img.shape[:2]

M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)
res = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow("res", res)
cv2.waitKey(0)
cv2.destroyAllWindows()
