# Binary thresholding and binary inverse thresholding using function
import cv2 as cv
import numpy as np

def inverse_binary(img):
    img1 = cv.imread(img, 0)

    _, b_th = cv.threshold(img1, 127, 255, cv.THRESH_BINARY)
    _, inv_b_th = cv.threshold(img1, 200, 255, cv.THRESH_BINARY_INV)

    cv.imshow('Original Image', img1)
    cv.imshow('Binary', b_th)
    cv.imshow('Inverse', inv_b_th)

img = 'gradiant.PNG'
# Function call
inverse_binary(img)

cv.waitKey(0)
cv.destroyAllWindows()
