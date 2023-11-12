# Binary thresholding
import cv2 as cv
import numpy as np

img = cv.imread('gradiant.PNG', 0)
'''Thresholding gives two result - ret and thresholded value
cv.threshold(input img, threshold value, threshold maxvalue, 
threshold type)
We are comparing each and every pixel of original image to 127. 
if the value of pixel < 127 the pixel value is assigned to 0 (black)
and if the value of pixel > 127 the pixel value is assigned to 255 (white)'''
_, thresholded = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

# Show original image
cv.imshow('Original Image', img)
# Show thresholded image
cv.imshow('Thresholded Image', thresholded)

cv.waitKey(0)
cv.destroyAllWindows()
