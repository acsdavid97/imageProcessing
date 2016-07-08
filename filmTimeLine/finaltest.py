import cv2
import numpy as np
import math
import time


def average_image_color(img):
    # Return the average color in tuple form
    average = cv2.mean(img)
    average = np.array(list(average[0:3]))
    average = average.astype(np.uint8)
    b, g, r = average
    return (int(b), int(g), int(r))

cap = cv2.VideoCapture("vid.divx")

t1 = time.time()

frameNr = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)
fpsInt = int(math.floor(fps))
nrOfLines = frameNr/fpsInt
currFrame, currLine = 0, 0
print frameNr

img = np.zeros((100, nrOfLines+1, 3), np.uint8)

ret = True


while cap.isOpened() and ret:
    ret, frame = cap.read()
    # Consider a frame every second
    if currFrame % fpsInt == 0:
        color = average_image_color(frame)
        cv2.line(img, (currLine, 0), (currLine, 99), color, 1)
        currLine += 1

    print currFrame
    currFrame += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
print "exited while"
cv2.imwrite("lines.jpg", img)
cap.release()

t2 = time.time()
print t2 - t1

