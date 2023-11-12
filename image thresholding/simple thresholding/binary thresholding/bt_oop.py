# Binary thresholding using Python function
import cv2 as cv
import numpy as np

class Thresholding:
    def __init__(self, img):
        self.img = img

    def binary_thresholding(self):
        img1 = cv.imread(self.img, 0)
        _, thresholded = cv.threshold(img1, 127, 255, cv.THRESH_BINARY)
        cv.imshow('Original Image', img1)
        cv.imshow('Thresholded Image', thresholded)

img = 'gradiant.PNG'
# Create object
obj = Thresholding(img)
# Function call
obj.binary_thresholding()

cv.waitKey(0)
cv.destroyAllWindows()
