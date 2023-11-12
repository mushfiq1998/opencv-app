import numpy as np
import cv2

def add_two_image(image1, image2):
    img = cv2.imread(image1)
    img2 = cv2.imread(image2)

    print('Image shape: ', img.shape)
    print('Image size: ', img.size)
    print('Image data type: ', img.dtype)

    b, g, r = cv2.split(img) 
    img = cv2.merge((b, g, r))

    img = cv2.resize(img, (512, 512))
    img2 = cv2.resize(img2, (512, 512))

    merged_img = cv2.add(img, img2)
    cv2.imshow('Image', merged_img)

image1 = 'stadium4.jpeg'
image2 = 'messi.jpg'
# Function call
add_two_image(image1, image2)

cv2.waitKey(0)
cv2.destroyAllWindows()