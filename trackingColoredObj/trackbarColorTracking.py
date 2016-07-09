import cv2
import numpy as np


'''
We can select colors to track on the webcam with the track pads,
select the colors you want (hue), set the threshold, minimal saturation and value
the program does the rest, for example:

blue and green

blue:
firstHue 115
firstHueThreshold 15
firstMinSat 40
firstMinValue 56

green:
secondHue 45
secondHueThreshold 19
secondMinSat 35
secondMinValue 30

This example may or may not work, depending on lighting, camera etc.
play with it a little :)

Exit the program pressing 'q'

'''

def nothing(x):
    pass

cv2.namedWindow("trackbars")

cv2.createTrackbar("firstHue", "trackbars", 0, 180, nothing)
cv2.createTrackbar("firstHueThreshold", "trackbars", 0, 180, nothing)
cv2.createTrackbar("firstMinSat", "trackbars", 0, 255, nothing)
cv2.createTrackbar("firstMinValue", "trackbars", 0, 255, nothing)

cv2.createTrackbar("secondHue", "trackbars", 0, 180, nothing)
cv2.createTrackbar("secondHueThreshold", "trackbars", 0, 180, nothing)
cv2.createTrackbar("secondMinSat", "trackbars", 0, 255, nothing)
cv2.createTrackbar("secondMinValue", "trackbars", 0, 255, nothing)

cap = cv2.VideoCapture(0)

print "you can quit with 'q'"

while True:
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    firstH = cv2.getTrackbarPos("firstHue", "trackbars")
    firstHT = cv2.getTrackbarPos("firstHueThreshold", "trackbars")
    firstMS = cv2.getTrackbarPos("firstMinSat", "trackbars")
    firstMV = cv2.getTrackbarPos("firstMinValue", "trackbars")

    first = np.array([firstH, 0, 0])
    lower_first = first + np.array([-firstHT, firstMS, firstMV])
    upper_first = first + np.array([firstHT, 255, 255])

    secondH = cv2.getTrackbarPos("secondHue", "trackbars")
    secondHT = cv2.getTrackbarPos("secondHueThreshold", "trackbars")
    secondMS = cv2.getTrackbarPos("secondMinSat", "trackbars")
    secondMV = cv2.getTrackbarPos("secondMinValue", "trackbars")

    second = np.array([secondH, 0, 0])
    lower_second = second + np.array([-secondHT, secondMS, secondMV])
    upper_second = second + np.array([secondHT, 255, 255])

    mask_first = cv2.inRange(hsv, lower_first, upper_first)

    mask_second = cv2.inRange(hsv, lower_second, upper_second)

    mask = cv2.bitwise_or(mask_first,mask_second)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("original", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("final", res)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


