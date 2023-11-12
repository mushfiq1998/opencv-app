# Get current position of trackbar on image using Python OOP
import numpy as np
import cv2 as cv

class Position:

    def __init__(self):
        pass

    def find_position(self):
        
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

            b = cv.getTrackbarPos('B', 'image')
            g = cv.getTrackbarPos('G', 'image')
            r = cv.getTrackbarPos('R', 'image')

            img[:] = [b, g, r]

# Create object
obj = Position()

# Function call
obj.find_position()

cv.destroyAllWindows()
