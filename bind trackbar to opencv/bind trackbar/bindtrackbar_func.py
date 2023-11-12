import numpy as np
import cv2 as cv

def bind_trackbar():

    def nothing(x):
        print('x: ', x)

    img = np.zeros((300, 512, 3), np.uint8)
    cv.namedWindow('image')

    cv.createTrackbar('B', 'image', 0, 255, nothing)
    cv.createTrackbar('G', 'image', 0, 255, nothing) 
    cv.createTrackbar('R', 'image', 0, 255, nothing)

    while(1):
        cv.imshow('image', img)
        k = cv.waitKey(1)
        if k == 27:
            break

# Function call
bind_trackbar()

cv.destroyAllWindows()
