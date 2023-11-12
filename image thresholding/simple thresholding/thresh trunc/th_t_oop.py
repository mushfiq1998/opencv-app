# Thresh trunc using Python OOP
import cv2 as cv
import numpy as np

class Threshold:
    def __init__(self, img):
        self.img = img

    def thresh_trunc(self):
        img1 = cv.imread(self.img, 0)
        '''The pixel value upto 200 will not changed 
        and after 100 it remains 100'''
        _, thresh_trunc = cv.threshold(img1, 100, 255, cv.THRESH_TRUNC)
        # Show original image
        cv.imshow('Original Image', img1)
        # Show thresholded image
        cv.imshow('Thresh Trunc', thresh_trunc)

img = 'gradiant.PNG'
# Create object
obj = Threshold(img)
# Function call
obj.thresh_trunc()

cv.waitKey(0)
cv.destroyAllWindows()
