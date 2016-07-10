import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread("gradient.jpg", 0)

thresholds = [None, cv2.THRESH_BINARY, cv2.THRESH_BINARY_INV,
              cv2.THRESH_TRUNC, cv2.THRESH_TOZERO, cv2.THRESH_TOZERO_INV]
threshim = []
for i in range(1,6):
    ret, aux = cv2.threshold(img, 127, 255, thresholds[i])
    threshim.append(aux)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img] + threshim

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
