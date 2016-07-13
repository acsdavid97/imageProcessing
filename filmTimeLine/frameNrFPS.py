import cv2
import numpy as np


cap = cv2.VideoCapture("vid.divx")
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap.get(cv2.CAP_PROP_FPS)
print length, fps
time = length/fps
print time

cap.release()
