import cv2
import numpy as np


img = cv2.imread("messi5.jpg")

res = cv2.resize(img,None,fx=2,fy=2, interpolation=cv2.INTER_CUBIC)

# Second method

heigth, width = img.shape[0:2]

# Linear and cubic
res_lin = cv2.resize(img, (1000, 2*heigth), interpolation=cv2.INTER_LINEAR)
res_cub = cv2.resize(img, (1000, 2*heigth), interpolation=cv2.INTER_CUBIC)

cv2.imshow("res_lin", res_lin)
cv2.imshow("res_cub", res_cub)
cv2.waitKey(0)
cv2.destroyAllWindows()