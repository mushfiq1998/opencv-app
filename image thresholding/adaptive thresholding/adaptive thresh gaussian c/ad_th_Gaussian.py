# Adaptive thresholding - ADAPTIVE_THRESH_GAUSSIAN_C with THRESH_BINARY
import cv2 as cv

img = cv.imread('sudoku.PNG', 0)
_, th_binary = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
'''cv.threshold(input img, threshold maxvalue, threshold method, 
             threshold type, blocksize, C)
Here, maxvalue is non zero value assigned to pixels for which the 
condition is satisfied.
threshold method decides how the thresholding value is calculated.
block size is the size of neighbourhood area.
C is just a constant and taken from ADAPTIVE_THRESH_GAUSSIAN_C'''
adp_gaussian = cv.adaptiveThreshold(img, 255, 
    cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
# Show original image
cv.imshow('Original Image', img)
# Show thresholded image
cv.imshow('th_binary', th_binary)
cv.imshow('adp_gaussian', adp_gaussian)

cv.waitKey(0)
cv.destroyAllWindows()
