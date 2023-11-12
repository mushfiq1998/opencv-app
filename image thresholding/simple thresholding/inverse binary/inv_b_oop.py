# Binary thresholding and binary inverse thresholding using OOP
import cv2 as cv
import numpy as np

class Threshold:
    def __init__(self, img):
        self.img = img

    def inverse_binary(self):
        img1 = cv.imread(self.img, 0)
        _, b_th = cv.threshold(img1, 127, 255, cv.THRESH_BINARY)
        _, inv_b_th = cv.threshold(img1, 200, 255, cv.THRESH_BINARY_INV)

        cv.imshow('Original Image', img1)
        cv.imshow('Binary', b_th)
        cv.imshow('Inverse', inv_b_th)

img = 'gradiant.PNG'
# create object
obj = Threshold(img)
# Function call
obj.inverse_binary()

cv.waitKey(0)
cv.destroyAllWindows()
