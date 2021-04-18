import numpy as np
import cv2 as cv


def showInMovedWindow(winname, img, x, y):
    cv.namedWindow(winname)        # Create a named window
    cv.moveWindow(winname, x, y)   # Move it to (x,y)
    cv.imshow(winname,img)


img = np.zeros((512,512,3), np.uint8)

img.fill(255)

cv.rectangle(img,(0,0),    (420,250) ,(0,0,0),1)

cv.line(img,     (220,10), (220,240) ,(0,0,0),1)
cv.circle(img,   (220,70), 50, (0,0,0), 1)
cv.circle(img,   (220,155), 30, (0,0,0), 1)
cv.circle(img,   (220,210), 15, (0,0,0), 1)

showInMovedWindow('named_window',img, 0, 200)
k = cv.waitKey(0)