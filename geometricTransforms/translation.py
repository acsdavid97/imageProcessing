import cv2
import numpy as np

img = cv2.imread("messi5.jpg", 1)
rows, cols = img.shape[:2]

M = np.float32([[1, 0, 100], [0, 1, 50]])
'''
This ^ is a translation matrix:
[ 1 0 100 ]
[ 0 1 50  ]
'''

res = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow("res", res)
cv2.waitKey(0)
cv2.destroyAllWindows()
