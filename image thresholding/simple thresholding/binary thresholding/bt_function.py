# Binary thresholding using Python function
import cv2 as cv
import numpy as np

def binary_thresholding(img):
    img1 = cv.imread(img, 0)
    _, thresholded = cv.threshold(img1, 127, 255, cv.THRESH_BINARY)

    cv.imshow('Original Image', img1)
    cv.imshow('Thresholded Image', thresholded)

img = 'gradiant.PNG'
# Function call
binary_thresholding(img)

cv.waitKey(0)
cv.destroyAllWindows()
