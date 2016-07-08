import cv2
import numpy as np
import time


e1 = cv2.getTickCount()
t1 = time.time()

img = np.zeros((512, 512, 3), np.uint8)
cv2.line(img, (0, 0), (511, 511), (0, 255, 0), 5)
cv2.imshow("imagewithline", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

e2 = cv2.getTickCount()
t2 = time.time()
ti1 = (e2 - e1)/cv2.getTickFrequency()
ti2 = (t2 - t1)

# Should be true, otherwise programs run slowly
print cv2.useOptimized()
print ti1, ti2, e2, e1, cv2.getTickFrequency()
