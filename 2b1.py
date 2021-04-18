import numpy as np
import cv2 as cv


def showInMovedWindow(winname, img, x, y):
    cv.namedWindow(winname)        # Create a named window
    cv.moveWindow(winname, x, y)   # Move it to (x,y)
    cv.imshow(winname,img)


img = np.zeros((512,512,3), np.uint8)

img.fill(255)

cv.rectangle(img,(0,0),    (270,270) ,(0,0,0),1)

cv.line(img,     (20,140), (250,140) ,(0,0,0),1)
cv.circle(img,   (135,90), 80, (0,0,0), 1)

cv.line(img,     (20,210), (250,210) ,(0,0,0),1)
cv.line(img,     (250,210), (135,90) ,(0,0,0),1)
cv.line(img,     (135,90), (20,210) ,(0,0,0),1)


showInMovedWindow('named_window',img, 0, 200)
k = cv.waitKey(0)