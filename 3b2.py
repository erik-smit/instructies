import numpy as np
import cv2 as cv

def showInMovedWindow(winname, img, x, y):
    cv.namedWindow(winname)        # Create a named window
    cv.moveWindow(winname, x, y)   # Move it to (x,y)
    cv.imshow(winname,img)

img = np.zeros((768,768,3), np.uint8)
img.fill(255)

triangle = np.array([[380, 210], [470, 380], [290, 380]])
cv.polylines(img,[triangle],True,(0,0,0), 2)

cv.rectangle(img, (80, 440), (280, 550), (0,0,0), 2)

cv.circle(img, (270, 390), 100, (255,255,255), -1)
cv.circle(img, (270, 390), 100, (0,0,0), 2)

showInMovedWindow('named_window',img, 0, 200)
k = cv.waitKey(0)