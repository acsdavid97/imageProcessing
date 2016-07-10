import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread("sat_noisy.jpg", 0)

ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

gauss = cv2.GaussianBlur(img, (5, 5), 0)

retg, res = cv2.threshold(gauss, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

titles = ['Original Noisy Image', 'Histogram', 'Global Thresholding (v=127)',
          'Original Noisy Image', 'Histogram', "Otsu's Thresholding",
          'Gaussian filtered Image', 'Histogram', "Otsu's Thresholding"]

images = [img, 0, th1,
          img, 0, th2,
          gauss, 0, res]

for i in range(3):
    plt.subplot(3, 3, 3*i + 1), plt.imshow(images[3*i], 'gray')
    plt.xticks([]), plt.yticks([]), plt.title(titles[3*i])
    plt.subplot(3, 3, 3*i + 2), plt.hist(images[3*i].ravel(), 256)
    plt.xticks([]), plt.yticks([]), plt.title(titles[3*i +1])
    plt.subplot(3, 3, 3*i + 3), plt.imshow(images[3*i +2], "gray")
    plt.xticks([]), plt.yticks([]), plt.title(titles[3*i +2])

plt.show()


