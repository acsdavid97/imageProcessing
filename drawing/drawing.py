import numpy as np
import cv2

def printImWaitKey(windowname, img):
    cv2.imshow(windowname, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Creating a black image with dimensions 512 by 512, 3 colors, 8 bit mode
img = np.zeros((512, 512, 3), np.uint8)

printImWaitKey("black", img)

# Putting a blue line on the black image
cv2.line(img, (1, 1), (511, 511), (255, 0, 0), 5)

printImWaitKey("line", img)

cv2.rectangle(img, (0, 0), (300, 250), (0, 255, 0), -1)

printImWaitKey("rectangle", img)

font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, "myText", (30, 300), font, 1, (255, 255, 255), 2, cv2.CV_AA)

printImWaitKey("text", img)