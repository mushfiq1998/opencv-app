# Start with adaptive thresholding
import cv2 as cv

img = cv.imread('sudoku.PNG', 0)
'''We are comparing each and every pixel of original image to 127. 
if the value of pixel < 127 the pixel value is assigned to 0 (black)
and if the value of pixel > 127 the pixel value is assigned to 255 (white)
Here, 127 is global threshold value.'''
_, th_binary = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

# Show original image
cv.imshow('Original Image', img)
# Show thresholded image
cv.imshow('Thresholded binary', th_binary)

cv.waitKey(0)
cv.destroyAllWindows()
