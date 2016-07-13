import cv2
import numpy as np

cap = cv2.VideoCapture(0)

blue = np.array([120, 0, 0])
lower_blue = blue + np.array([-15, 50, 50])
upper_blue = blue + np.array([15, 255, 255])
while True:
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("original", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("final", res)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
