# Add two images using addwaited() method
import numpy as np
import cv2

img = cv2.imread('stadium4.jpeg')
img2 = cv2.imread('Messi.jpg')

# Returns a tuple of number of rows, columns and channels
print('Image shape: ', img.shape)
# Returns total of number of pixels is accessed
print('Image size: ', img.size)
# Returns image data type is obtained
print('Image data type: ', img.dtype)

# Split image in three channels
b, g, r = cv2.split(img)
# Merge three channels (passed in tuple form) into an image  
img = cv2.merge((b, g, r))

# Resize two images in common size
# img = cv2.resize(img, (rows, columns)) # in tuple format
img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))

'''You can only add two images of same size
# merged_img = cv2.addWeighted(img, weight of 1st image, img2, 
weight of 1st image, scalar value)
weight of 1st image + weight of 1st image = 1
For example: .9 + .1 = 1  or .8 + .2 = 1 0r .5 + .5 = 1     '''
merged_img = cv2.addWeighted(img, .5, img2, .5, 0)
cv2.imshow('Image', merged_img)

'''when this method takes 0 as argument, it will not be disappeared 
until you close it'''
cv2.waitKey(0)
cv2.destroyAllWindows()