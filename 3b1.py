import numpy as np
import cv2 as cv

def showInMovedWindow(winname, img, x, y):
    cv.namedWindow(winname)        # Create a named window
    cv.moveWindow(winname, x, y)   # Move it to (x,y)
    cv.imshow(winname,img)

img = np.zeros((768,768,3), np.uint8)
img.fill(255)

cv.rectangle(img, (190, 280), (420, 510), (0,0,0), 2)

cv.rectangle(img, (80, 310), (210, 390), (255, 255, 255), -1)
cv.rectangle(img, (80, 310), (210, 390), (0), 2)

hexagon = np.array([[390, 340], [470, 340], [500, 400], [470, 460], [390, 460], [360, 400]])
cv.fillPoly(img, [hexagon], (255, 255, 255))
cv.polylines(img,[hexagon],True,(0,0,0), 2)

showInMovedWindow('named_window',img, 0, 200)
k = cv.waitKey(0)