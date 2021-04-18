import numpy as np
import cv2 as cv


def showInMovedWindow(winname, img, x, y):
    cv.namedWindow(winname)        # Create a named window
    cv.moveWindow(winname, x, y)   # Move it to (x,y)
    cv.imshow(winname,img)


img = np.zeros((512,512,3), np.uint8)

img.fill(255)

cv.rectangle(img,(0,0),    (420,250) ,(0,0,0),1)

cv.line(img,     (10,210), (410,210) ,(0,0,0),1)
cv.rectangle(img,(30,160), (70,200)  ,(0,0,0),-1)

cv.line(img,     (160,200), (240,200),(0,0,0),1)
cv.line(img,     (240,200), (200,130),(0,0,0),1)
cv.line(img,     (200,130), (160,200),(0,0,0),1)

cv.rectangle(img,(290,100),(390,200),(0,0,0), 1)

showInMovedWindow('named_window',img, 0, 200)
k = cv.waitKey(0)