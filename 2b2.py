import numpy as np
import cv2 as cv


def showInMovedWindow(winname, img, x, y):
    cv.namedWindow(winname)        # Create a named window
    cv.moveWindow(winname, x, y)   # Move it to (x,y)
    cv.imshow(winname,img)


img = np.zeros((768,768,3), np.uint8)

img.fill(255)

triangle = np.array([[340,420],[520,430],[435,255]], np.int32)
cv.polylines(img,[triangle],True,(0,0,0), 2)

diamond = np.array([[410,340], [290, 410], [180, 340], [300, 250]], np.int32)
cv.fillPoly(img, [diamond], (255, 255, 255))
cv.polylines(img,[diamond],True,(0,0,0), 2)

cv.circle(img, (150,340), 80, (255,255,255), -1)
cv.circle(img, (150,340), 80, (0,0,0), 2)

showInMovedWindow('named_window',img, 0, 200)
k = cv.waitKey(0)