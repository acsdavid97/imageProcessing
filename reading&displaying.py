import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('messi5.jpg', 0)
print img.shape

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
