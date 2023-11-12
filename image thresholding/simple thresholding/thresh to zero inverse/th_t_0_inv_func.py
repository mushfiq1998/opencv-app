# Thresh t0 zero inverse
import cv2 as cv
import numpy as np

def thresh_to_zero(img):
    img1 = cv.imread(img, 0)

    _, thre_to_o = cv.threshold(img1, 127, 255, cv.THRESH_TOZERO)
    _, thre_to_o_inv = cv.threshold(img1, 127, 255, cv.THRESH_TOZERO_INV)

    cv.imshow('Original Image', img1)
    cv.imshow('thre_to_o', thre_to_o)
    cv.imshow('thre_to_o_inv', thre_to_o_inv)

img = 'gradiant.PNG'
# Function call
thresh_to_zero(img)

cv.waitKey(0)
cv.destroyAllWindows()
