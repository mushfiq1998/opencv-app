# Binary thresholding and binary inverse thresholding
import cv2 as cv
import numpy as np

img = cv.imread('gradiant.PNG', 0)

# _, b_th = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
_, b_th = cv.threshold(img, 50, 255, cv.THRESH_BINARY)
'''We are comparing each and every pixel of original image to 127. 
if the value of pixel < 127 the pixel value is assigned to 255 (white)
and if the value of pixel > 127 the pixel value is assigned to 0 (black)
here, b_th=binary thresholded and inv_b_th=inverse binary thresholded'''
# _, inv_b_th = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
_, inv_b_th = cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV)

# Show original image
cv.imshow('Original Image', img)
# Show thresholded image
cv.imshow('Binary', b_th)
cv.imshow('Inverse', inv_b_th)

cv.waitKey(0)
cv.destroyAllWindows()
