import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('book.jpg', 0)
img2 = cv2.imread('bookInContext.jpg', 0)

orb = cv2.ORB_create(100)

kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, True)

matches = bf.match(des1, des2)

matches = sorted(matches, key = lambda x:x.distance)

img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], flags=2)

plt.imshow(img3), plt.show()
