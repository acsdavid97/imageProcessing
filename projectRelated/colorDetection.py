import cv2
import numpy as np
import time


def update(x):
    settings.hue = cv2.getTrackbarPos('Hue(color)', 'settings')
    settings.threshold = cv2.getTrackbarPos('Threshold', 'settings')
    settings.minSaturation = cv2.getTrackbarPos('minSat', 'settings')
    settings.minValue = cv2.getTrackbarPos('minValue', 'settings')


class TrackBars(object):
    def __init__(self):
        self.hue = 50
        self.threshold = 10
        self.kernel = 5
        self.minSaturation = 50
        self.minValue = 60


def get_mask(hsvframe, setting):
    lower = np.array([setting.hue - setting.threshold, setting.minSaturation, setting.minValue])
    upper = np.array([setting.hue + setting.threshold, 255, 255])

    maskf = cv2.inRange(hsvframe, lower, upper)

    maskf = cv2.morphologyEx(maskf, cv2.MORPH_OPEN, kernel)
    #maskf = cv2.morphologyEx(maskf, cv2.MORPH_CLOSE, kernel)

    return maskf


cap = cv2.VideoCapture(0)
cv2.namedWindow('settings')

settings = TrackBars()

cv2.createTrackbar('Hue(color)', 'settings', settings.hue, 179, update)
cv2.createTrackbar('Threshold', 'settings', settings.threshold, 255, update)
cv2.createTrackbar('minSat', 'settings', settings.minSaturation, 255, update)
cv2.createTrackbar('minValue', 'settings', settings.minValue, 255, update)

shape = (settings.kernel, settings.kernel)

kernel = np.ones(shape, np.uint8)

while True:
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = get_mask(hsv, settings)



    final = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('original', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('final', final)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
