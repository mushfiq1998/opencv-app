import cv2
import numpy as np

class Operation:

    def __init__(self, img):
        self.img = img

    def nor_operation(self):
        img1 = np.zeros((250, 500, 3), np.uint8)
        img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)

        img2 = cv2.imread(self.img)

        img2 = cv2.resize(img2, (500, 250))

        bitNot1 = cv2.bitwise_not(img1)
        bitNot2 = cv2.bitwise_not(img2)

        bitNor = cv2.bitwise_or(bitNot1, bitNot2)

        cv2.imshow('Image1', img1)
        cv2.imshow('Image2', img2)
        cv2.imshow('bitNor', bitNor)

img = 'black_white.jpg'
# Create object
obj = Operation(img)

# Function call
obj.nor_operation()

cv2.waitKey(0)
cv2.destroyAllWindows()