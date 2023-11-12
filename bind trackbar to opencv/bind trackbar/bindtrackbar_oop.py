import numpy as np
import cv2 as cv

class Bind:

    def __init__(self):
        pass

    def bind_trackbar(self):

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

# Create object
obj = Bind()

# Function call
obj.bind_trackbar()

cv.destroyAllWindows()
