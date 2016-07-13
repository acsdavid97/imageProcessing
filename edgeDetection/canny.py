import cv2
import numpy as np
from matplotlib import pyplot as plt


def nothing(x):
    pass


cv2.namedWindow('settings')
cv2.createTrackbar('lower', 'settings', 100, 255, nothing)
cv2.createTrackbar('upper', 'settings', 200, 255, nothing)

img = cv2.imread('totest.jpg', 0)
img2 = cv2.imread('totest.jpg')
cv2.imshow('original', img)

while True:
    lower = cv2.getTrackbarPos('lower', 'settings')
    upper = cv2.getTrackbarPos('upper', 'settings')
    edges = cv2.Canny(img, lower, upper, L2gradient=False, apertureSize=3)
    cv2.imshow('edges', edges)
    lel = cv2.bitwise_and(img2, img2, mask=edges)
    cv2.imshow('lel', lel)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
