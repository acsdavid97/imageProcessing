import cv2
import numpy as np


def draw(event, x, y, flags, param):
    global ix, iy, drawing, mode, img, img2
    img2 = np.copy(img)
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            if mode:
                cv2.rectangle(img2, (ix, iy), (x, y), (0, 255, 0), 5)
            else:
                cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode:
            cv2.rectangle(img2, (ix, iy), (x, y), (0, 255, 0), 5)
            img = np.copy(img2)
        else:
            cv2.circle(img, (x, y), 5, (0, 0, 255), -1)


img = np.zeros((512, 512, 3), np.uint8)
img2 = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow("image")
cv2.setMouseCallback("image", draw)

drawing = False
mode = True
ix, iy = -1, -1

while True:
    if mode and drawing:
        cv2.imshow("image", img2)
    else:
        cv2.imshow("image", img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == ord('q'):
        break

cv2.destroyAllWindows()
