# Add switch using trackbar through Python function 
import numpy as np
import cv2 as cv

class Switch:

    def add_switch(self):

        def nothing(x):
            print('x: ', x)

        img = np.zeros((300, 512, 3), np.uint8)
        cv.namedWindow('image')

        cv.createTrackbar('B', 'image', 0, 255, nothing)
        cv.createTrackbar('G', 'image', 0, 255, nothing) 
        cv.createTrackbar('R', 'image', 0, 255, nothing)
        switch = '0 : OFF\n  1: ON'
        cv.createTrackbar(switch, 'image', 0, 255, nothing)

        while(1):
            cv.imshow('image', img)

            k = cv.waitKey(1)
            if k == 27:
                break

            b = cv.getTrackbarPos('B', 'image')
            g = cv.getTrackbarPos('G', 'image')
            r = cv.getTrackbarPos('R', 'image')
            s = cv.getTrackbarPos(switch, 'image')

            if s == 0:
                img[:] = 0
            else:
                img[:] = [b, g, r]

# Create object
obj = Switch()

# Function call
obj.add_switch()

cv.destroyAllWindows()
