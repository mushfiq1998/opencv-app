# Adaptive thresholding - ADAPTIVE_THRESH_GAUSSIAN_C with THRESH_BINARY
import cv2 as cv

class Thresh:
    def __init__(self, img):
        self.img = img

    def adaptive_thresh(self):
        img1 = cv.imread(self.img, 0)
        _, th_binary = cv.threshold(img1, 127, 255, cv.THRESH_BINARY)
        adp_gaussian = cv.adaptiveThreshold(img1, 255, 
            cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
        
        cv.imshow('Original Image', img1)
        cv.imshow('th_binary', th_binary)
        cv.imshow('adp_gaussian', adp_gaussian)

img = 'sudoku.PNG'
# Create object
obj = Thresh(img)
# Function call
obj.adaptive_thresh()

cv.waitKey(0)
cv.destroyAllWindows()
