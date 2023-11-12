# Adaptive thresholding - ADAPTIVE_THRESH_MEAN_C
import cv2 as cv

class AdaptiveThresh:
    def __init__(self, img):
        self.img = img

    def adaptive(self):
        img1 = cv.imread(self.img, 0)
        adptive_th = cv.adaptiveThreshold(img1, 255, 
            cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
        cv.imshow('Original Image', img1)
        cv.imshow('Adaptive threshold', adptive_th)
img = 'sudoku.PNG'
# Create object
obj = AdaptiveThresh(img)
# Function call
obj.adaptive()
cv.waitKey(0)
cv.destroyAllWindows()
