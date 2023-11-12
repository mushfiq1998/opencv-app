import cv2
import numpy as np

# Create a black image, here height = 250, width = 500
img1 = np.zeros((250, 500, 3), np.uint8)
# Draw a white rectangle inside img1
img1 = cv2.rectangle(img1, (200,0), (300,100), (255,255,255), -1)
img2 = cv2.imread('black_white.jpg')
# img2 = cv2.imread('black.PNG')

# Resize img2 to the size of img1. Now two images are of same dimensions
img2 = cv2.resize(img2, (500, 250))
bitOr = cv2.bitwise_or(img2, img1)

cv2.imshow('Image1', img1)
cv2.imshow('Image2', img2)
cv2.imshow('bitOr', bitOr)

cv2.waitKey(0)
cv2.destroyAllWindows()
