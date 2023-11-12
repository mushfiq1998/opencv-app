import cv2
import numpy as np

def nor_operation(img):
    img1 = np.zeros((250, 500, 3), np.uint8)
    img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)

    img2 = cv2.imread(img)

    img2 = cv2.resize(img2, (500, 250))

    bitNot1 = cv2.bitwise_not(img1)
    bitNot2 = cv2.bitwise_not(img2)

    bitNor = cv2.bitwise_or(bitNot1, bitNot2)

    cv2.imshow('Image1', img1)
    cv2.imshow('Image2', img2)
    cv2.imshow('bitNor', bitNor)

img = 'black_white.jpg'
# Function call
nor_operation(img)

cv2.waitKey(0)
cv2.destroyAllWindows()