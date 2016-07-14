import cv2
import numpy as np

'''
imgToFind = cv2.imread('toFind.jpg', 0)
ret, thresh = cv2.threshold(imgToFind, 127, 255, cv2.THRESH_BINARY_INV)
'''

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('original', frame)

    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('gray', frameGray)

    equ = cv2.equalizeHist(frameGray)

    ret, thresh = cv2.threshold(equ, 165, 255, cv2.THRESH_BINARY)
    # cv2.imshow('thresh', thresh)
    cv2.imshow('equ', equ)

    lower = np.array([0, 0, 175])
    upper = np.array([179, 255, 255])
    mask = cv2.inRange(frameHSV, lower, upper)
    cv2.imshow('mask', mask)

    newmask = cv2.bitwise_and(thresh, mask)
    notmask = cv2.bitwise_not(newmask)
    cv2.imshow('newmask', newmask)
    im, contours, hierarchy = cv2.findContours(newmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    max_area = 0
    for cnt in contours:
        if cv2.contourArea(cnt) > max_area:
            max_area = cv2.contourArea(cnt)
            maxCnt = cnt

    if max_area > 0:
        x, y, w, h = cv2.boundingRect(maxCnt)
        roi = notmask[y:y+h, x:x+w]
        cv2.imshow('roi', roi)

    cv2.imshow('notmask', notmask)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
