'''This does not provides expected result, but it is obtained in the file:
calculate_coordinate_on_image.py and image_on_image.py'''
import numpy as np
import cv2

# img = cv2.imread('Messi.PNG')
img = cv2.imread('Messi4.jpg')
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

'''img = cv2.rectangle(img, (top left coordinate), 
(bottom right coordinate), (color in BGR format), thikness)'''
# Draw rectangle on image
img = cv2.rectangle(img, (372,335), (438,392), (0,0,255), 2)

'''Work with ROI - Region of Interest.
Copy the ball (coordinate of ball) from the image through numpy indexing.
The specified coordinates [280:340, 330:390] define a rectangular region 
within the image. This region represents the area where the ball is 
located. '''
# football_roi = image[top_left_x:top_left_y, bottom_right_x:bottom_right_y]
# ball = img[372:335, 438:392]
# football_roi = image[top_left_y:bottom_right_y, top_left_x:bottom_right_x]
ball = img[330:397, 366:446]
'''place the ball on the specific coordinate of image.
img[280:340 = top left hand corner of this ball), 
330:390 = bottom right hand corner of this ball]
The coordinates [273:333, 100:160] specify another rectangular region 
where you want to place the ball.'''
# img[101:337, 179:393] = ball
img[225:347, 43:194] = ball

cv2.imshow('Image', img)

'''when this method takes 0 as argument, it will not be disappeared 
until you close it'''
cv2.waitKey(0)
cv2.destroyAllWindows()