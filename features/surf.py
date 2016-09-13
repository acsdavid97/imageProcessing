import cv2
import numpy as np

img = cv2.imread('book.jpg', 0)
sift = cv2.xfeatures2d.SURF_create()
