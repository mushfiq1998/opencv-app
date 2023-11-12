# Thresh trunc
import cv2 as cv
import numpy as np

img = cv.imread('gradiant.PNG', 0)

'''The pixel value upto 200 will not changed and after 100 it remains 100'''
_, thresh_trunc = cv.threshold(img, 100, 255, cv.THRESH_TRUNC)

# Show original image
cv.imshow('Original Image', img)
# Show thresholded image
cv.imshow('Thresh Trunc', thresh_trunc)

cv.waitKey(0)
cv.destroyAllWindows()
