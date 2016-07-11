import cv2
import numpy as np


def update(x):
    # Updates the settings values
    settings.hue = cv2.getTrackbarPos('Hue(color)', 'settings')
    settings.threshold = cv2.getTrackbarPos('Threshold', 'settings')
    settings.minSaturation = cv2.getTrackbarPos('minSat', 'settings')
    settings.minValue = cv2.getTrackbarPos('minValue', 'settings')


class TrackBars(object):
    # The current state of track bars.
    def __init__(self):
        self.hue = 110
        self.threshold = 5
        self.kernel = 5
        self.minSaturation = 120
        self.minValue = 120


def get_mask(currframe, setting):
    # Returns the mask from the current frame, depending on the settings.
    hsv = cv2.cvtColor(currframe, cv2.COLOR_BGR2HSV)

    lower = np.array([setting.hue - setting.threshold, setting.minSaturation, setting.minValue])
    upper = np.array([setting.hue + setting.threshold, 255, 255])

    maskf = cv2.inRange(hsv, lower, upper)

    maskf = cv2.morphologyEx(maskf, cv2.MORPH_OPEN, kernel)
    maskf = cv2.morphologyEx(maskf, cv2.MORPH_CLOSE, kernel)

    return maskf


# Initialize GUI and get ready for capturing images from webcam
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

    mask = get_mask(frame, settings)
    cv2.imshow('mask', mask)
    # Finding all contours in the mask
    cnt, hier = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    max_area = 0
    for contour in cnt:
        # Getting maximal area from mask, whose area must be bigger than
        curr_area = cv2.contourArea(contour)
        if curr_area > 1000 and curr_area > max_area:
            maxCnt = contour
            max_area = curr_area

    if max_area != 0:
        # If we found the object with maximal area, find and draw a rectangle around it
        x, y, w, h = cv2.boundingRect(maxCnt)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 1)

        # Putting coordinates of rectangle on image
        font = cv2.FONT_HERSHEY_SIMPLEX
        coord = "x:%d y:%d" % (x, y)
        cv2.putText(frame, coord, (x + 1, y + 15), font, 0.5, (0, 0, 255), 2)
        coord = "x:%d y:%d" % (x+w, y+h)
        cv2.putText(frame, coord, (x+w +1, y+h + 15), font, 0.5, (0, 0, 255), 2)
    '''
    final = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('final', final)
    '''
    # Display image
    cv2.imshow('frame', frame)

    # If 'q' is pressed exit
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
