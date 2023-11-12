# Thresh t0 zero
import cv2 as cv
import numpy as np

img = cv.imread('gradiant.PNG', 0)

'''If the pixel value < 127 it is assigned to 0 (black)
If the pixel value > 127 it is assigned to 255 (white)
here, thre_to_o = thresholded to zeo'''
_, thre_to_o = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)

# Show original image
cv.imshow('Original Image', img)
# Show thresholded image
cv.imshow('thre_to_o', thre_to_o)

cv.waitKey(0)
cv.destroyAllWindows()
