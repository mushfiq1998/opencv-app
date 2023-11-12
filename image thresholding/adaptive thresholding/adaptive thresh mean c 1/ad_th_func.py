# Adaptive thresholding - ADAPTIVE_THRESH_MEAN_C
import cv2 as cv

def adaptive(img):
    img1 = cv.imread(img, 0)

    adptive_th = cv.adaptiveThreshold(img1, 255, 
        cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
    cv.imshow('Original Image', img1)
    cv.imshow('Adaptive threshold', adptive_th)

img = 'sudoku.PNG'
# Function call
adaptive(img)

cv.waitKey(0)
cv.destroyAllWindows()
