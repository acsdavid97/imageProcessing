import cv2


def nothing(x):
    pass

cv2.namedWindow('settings')
cv2.createTrackbar('lower', 'settings', 100, 255, nothing)
cv2.createTrackbar('upper', 'settings', 200, 255, nothing)

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    lower = cv2.getTrackbarPos('lower','settings')
    upper = cv2.getTrackbarPos('upper','settings')
    edges = cv2.Canny(img, lower, upper, L2gradient=False, apertureSize=3)

    cv2.imshow('original', img)
    cv2.imshow('edges', edges)
    lel = cv2.bitwise_and(img, img, mask=edges)
    cv2.imshow('lel', lel)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
