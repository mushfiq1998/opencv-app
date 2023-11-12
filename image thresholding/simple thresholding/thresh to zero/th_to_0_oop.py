# Thresh to zero using Python OOP
import cv2 as cv
import numpy as np

class ToZero:

    def __init__(self, img):
        self.img = img

    def thresh_to_zero(self):
        img1 = cv.imread(self.img, 0)
        _, thre_to_o = cv.threshold(img1, 127, 255, cv.THRESH_TOZERO)

        cv.imshow('Original Image', img1)
        cv.imshow('thre_to_o', thre_to_o)

img = 'gradiant.PNG'
# Create object
obj = ToZero(img)
# Function call
obj.thresh_to_zero()

cv.waitKey(0)
cv.destroyAllWindows()
