import cv2
import numpy as np

# from matplotlib import pyplot as plt


img = cv2.imread('messi5.jpg', 0)
# reading image, in grayscale ^
img2 = img.copy()
template = cv2.imread('template.jpg', 0)

w, h = template.shape[::-1]

print w, h

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
           'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
for meth in methods:
    img = img2.copy()
    # Convert method to corresponding integer
    method = eval(meth)

    # Template matching
    res = cv2.matchTemplate(img, template, method)
    cv2.imshow(meth, res)
    cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # Getting the location of image
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # Adjusting location, depending on method
    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum 
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc

    # Knowing the top left coordinates and dimensions of template, calculate bottom left coords
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(img, top_left, bottom_right, 255, 2)

cv2.imshow('image', img)
# creating a window, showing image
cv2.waitKey(0)
# waiting user input
cv2.destroyAllWindows()
# closing windows
