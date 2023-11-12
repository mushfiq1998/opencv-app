# Add two images using addwaited() method
import numpy as np
import cv2

class AddImage:

    def __init__(self, weight1, weight2):
        self.weight1 = weight1
        self.weight2 = weight2

    def add_two_images(self):
        img = cv2.imread('stadium4.jpeg')
        img2 = cv2.imread('Messi.jpg')

        print('Image shape: ', img.shape)
        print('Image size: ', img.size)
        print('Image data type: ', img.dtype)

        b, g, r = cv2.split(img)  
        img = cv2.merge((b, g, r))

        img = cv2.resize(img, (512, 512))
        img2 = cv2.resize(img2, (512, 512))

        merged_img = cv2.addWeighted(img, self.weight1, img2, 
                                     self.weight1, 0)
        cv2.imshow('Image', merged_img)

# weight1 = .5
weight1 = float(input('Enter weight of first image: '))
# weight2 = .5
weight2 = float(input('Enter weight of second image: '))
obj = AddImage(weight1, weight2)
# Function call
obj.add_two_images()

cv2.waitKey(0)
cv2.destroyAllWindows()