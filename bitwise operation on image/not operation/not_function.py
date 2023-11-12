import cv2
import numpy as np

def not_operation(img):
    img1 = np.zeros((250, 500, 3), np.uint8)
    img1 = cv2.rectangle(img1, (200,0), (300,100), (255,255,255), -1)
    img2 = cv2.imread(img)

    img2 = cv2.resize(img2, (500, 250))

    bitNot1 = cv2.bitwise_not(img1)
    bitNot2 = cv2.bitwise_not(img2)

    cv2.imshow('Image1', img1)
    cv2.imshow('Image2', img2)
    cv2.imshow('bitNot1', bitNot1)
    cv2.imshow('bitNot2', bitNot2)

img = 'black_white.jpg'
# Function call
not_operation(img)

cv2.waitKey(0)
cv2.destroyAllWindows()
