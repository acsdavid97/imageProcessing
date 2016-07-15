import cv2
import numpy as np


def prep_frame(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(img, (7, 7), 0)
    img = cv2.equalizeHist(img)
    return img

cap = cv2.VideoCapture(0)
cv2.waitKey(200)
ret, refFrame = cap.read()
refFrame = prep_frame(refFrame)
cv2.imshow('refFrame', refFrame)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))

while True:
    ret, frame = cap.read()
    frame = prep_frame(frame)
    cv2.imshow('stream', frame)

    diff = np.abs(frame - refFrame)
    diff[diff > 50] = 255
    diff[diff <= 51] = 0
    diff = cv2.morphologyEx(diff, cv2.MORPH_OPEN, kernel)

    cv2.imshow('diff', diff)

    if cv2.waitKey(10) & 0xFF == ord('n'):
        refFrame = frame
        cv2.imshow('refFrame', refFrame)

    if cv2.waitKey(10) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
