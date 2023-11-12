# Adaptive thresholding - ADAPTIVE_THRESH_MEAN_C
import cv2 as cv

img = cv.imread('sudoku.PNG', 0)
'''cv.threshold(input img, threshold maxvalue, threshold method, 
             threshold type, blocksize, C)
Here, maxvalue is non zero value assigned to pixels for which the 
condition is satisfied.
threshold method decides how the thresholding value is calculated.
ADAPTIVE_THRESH_MEAN_C it means that the threshold value is the 
mean of neighbourhood area.
block size is the size of neighbourhood area.
C is just a constant and taken from ADAPTIVE_THRESH_MEAN_C'''
adptive_th = cv.adaptiveThreshold(img, 255, 
    cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
# Show original image
cv.imshow('Original Image', img)
# Show thresholded image
cv.imshow('Adaptive threshold', adptive_th)

cv.waitKey(0)
cv.destroyAllWindows()
