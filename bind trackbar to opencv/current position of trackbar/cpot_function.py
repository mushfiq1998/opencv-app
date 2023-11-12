# Get current position of trackbar on image using function
import numpy as np
import cv2 as cv

def find_position():
     
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

# Function call
find_position()

cv.destroyAllWindows()
