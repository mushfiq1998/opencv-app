# Add switch using trackbar to convert colored image to gray scale image through py function. 
# It does not work properly
import numpy as np
import cv2 as cv

def add_switch(img):

    def nothing(x):
        print('x: ', x)

    cv.namedWindow('image')

    cv.createTrackbar('cp', 'image', 10, 400, nothing)
    switch = 'color/gray'
    cv.createTrackbar(switch, 'image', 0, 255, nothing)

    while(1):
        img = cv.imread(img)
        pos = cv.getTrackbarPos('cp', 'image')
        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(img, str(pos), (50,150), font, 5, (0,0,255), 5)

        k = cv.waitKey(1)
        if k == 27:
            break
        s = cv.getTrackbarPos(switch, 'image')
        if s == 0:
            pass
        else:
            img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        
        img = cv.imshow('image', img)

img = 'opencv2.webp'
# Function call
add_switch(img)

cv.destroyAllWindows()
