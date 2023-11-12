# Adaptive thresholding - ADAPTIVE_THRESH_MEAN_C with THRESH_BINARY
import cv2 as cv

def adaptive_thresh(img):
    img1 = cv.imread(img, 0)
    _, th_binary = cv.threshold(img1, 127, 255, cv.THRESH_BINARY)
    adptive_th = cv.adaptiveThreshold(img1, 255, 
        cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)

    cv.imshow('Original Image', img1)
    cv.imshow('th_binary', th_binary)
    cv.imshow('Adaptive threshold', adptive_th)

img = 'sudoku.PNG'
# Function call
adaptive_thresh(img)

cv.waitKey(0)
cv.destroyAllWindows()
