# Add two images using addwaited() method
import numpy as np
import cv2

def add_two_images(weight1, weight2):
    img = cv2.imread('stadium4.jpeg')
    img2 = cv2.imread('Messi.jpg')

    print('Image shape: ', img.shape)
    print('Image size: ', img.size)
    print('Image data type: ', img.dtype)

    b, g, r = cv2.split(img)  
    img = cv2.merge((b, g, r))

    img = cv2.resize(img, (512, 512))
    img2 = cv2.resize(img2, (512, 512))

    merged_img = cv2.addWeighted(img, weight1, img2, weight2, 0)
    cv2.imshow('Image', merged_img)

# weight1 = .5
weight1 = float(input('Enter weight of first image: '))
# weight2 = .5
weight2 = float(input('Enter weight of second image: '))
# Function call
add_two_images(weight1, weight2)

cv2.waitKey(0)
cv2.destroyAllWindows()