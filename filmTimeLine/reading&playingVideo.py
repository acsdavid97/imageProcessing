import numpy as np
import cv2


# Reads, plays and writes a video.
cap = cv2.VideoCapture('vid.divx')

# Codec and VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# Resolution has to be exact, otherwise file will not be readable.
out = cv2.VideoWriter('output.avi', fourcc, 24.0, (1920, 768))

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        frame = cv2.flip(frame, 0)

        out.write(frame)

        cv2.imshow("stream", frame)
        if cv2.waitKey(24) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
