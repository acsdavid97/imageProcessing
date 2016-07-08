import cv2
import numpy as np


def average_image_color(img):
    # Return the average color in tuple form
    average = cv2.mean(img)
    average = np.array(list(average[0:3]))
    average = average.astype(np.uint8)
    b, g, r = average
    return (int(b), int(g), int(r))

img = cv2.imread("messi5.jpg", 1)
color = average_image_color(img)
print color
print (255, 255, 255)

img2 = np.zeros((512, 512, 3), np.uint8)
cv2.line(img2, (0, 0), (511, 511), color, 5)
cv2.imshow("test",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
