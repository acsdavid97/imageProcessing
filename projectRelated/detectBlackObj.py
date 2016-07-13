import cv2
import numpy as np

imgToFind = cv2.imread('toFind.jpg', 0)
ret, thresh = cv2.threshold(imgToFind, 127, 255, cv2.THRESH_BINARY_INV)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frameHLS = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)

    lower = np.array([0, 0, 0])
    upper = np.array([179, 45, 120])
    mask = cv2.inRange(frameHLS, lower, upper)

    cv2.imshow('original', frame)
    cv2.imshow('mask', mask)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
