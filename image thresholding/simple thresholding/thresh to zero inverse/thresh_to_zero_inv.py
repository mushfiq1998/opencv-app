# Thresh t0 zero inverse
import cv2 as cv
import numpy as np

img = cv.imread('gradiant.PNG', 0)

_, thre_to_o = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
'''If the pixel value < 127 it is assigned to 255 (white)
If the pixel value > 127 it is assigned to 0 (black)
here, thre_to_o_inv = thresholded to zeo inverse'''
_, thre_to_o_inv = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)

# Show original image
cv.imshow('Original Image', img)
# Show thresholded image
cv.imshow('thre_to_o', thre_to_o)
cv.imshow('thre_to_o_inv', thre_to_o_inv)

cv.waitKey(0)
cv.destroyAllWindows()
