# Adaptive thresholding - ADAPTIVE_THRESH_MEAN_C with THRESH_BINARY
import cv2 as cv

class Adaptive:
    def __init__(self, img):
        self.img = img

    def adaptive_thresh(self):
        img1 = cv.imread(self.img, 0)
        _, th_binary = cv.threshold(img1, 127, 255, cv.THRESH_BINARY)
        adptive_th = cv.adaptiveThreshold(img1, 255, 
            cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
        cv.imshow('Original Image', img1)
        cv.imshow('th_binary', th_binary)
        cv.imshow('Adaptive threshold', adptive_th)

img = 'sudoku.PNG'
# Create object
obj = Adaptive(img) 
# Function call
obj.adaptive_thresh()

cv.waitKey(0)
cv.destroyAllWindows()
