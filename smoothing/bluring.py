import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("opencvnoisy.png")

# Average blur
blur = cv2.blur(img, (9, 9))

plt.subplot(2, 4, 1), plt.imshow(img), plt.title("OpenCV")
plt.xticks([]), plt.yticks([])
plt.subplot(2, 4, 2), plt.imshow(blur), plt.title("OpenCV average blurred")
plt.xticks([]), plt.yticks([])

# Gaussian blur
blur = cv2.GaussianBlur(img, (9, 9), 0)

plt.subplot(2, 4, 3), plt.imshow(img), plt.title("OpenCV")
plt.xticks([]), plt.yticks([])
plt.subplot(2, 4, 4), plt.imshow(blur), plt.title("OpenCV Gaussian blurred")
plt.xticks([]), plt.yticks([])

blur = cv2.medianBlur(img, 9)

plt.subplot(2, 4, 5), plt.imshow(img), plt.title("OpenCV")
plt.xticks([]), plt.yticks([])
plt.subplot(2, 4, 6), plt.imshow(blur), plt.title("OpenCV median blurred")
plt.xticks([]), plt.yticks([])

blur = cv2.bilateralFilter(img, 9, 75, 75)

plt.subplot(2, 4, 7), plt.imshow(img), plt.title("OpenCV")
plt.xticks([]), plt.yticks([])
plt.subplot(2, 4, 8), plt.imshow(blur), plt.title("OpenCV bilateral blurred")
plt.xticks([]), plt.yticks([])

plt.show()
