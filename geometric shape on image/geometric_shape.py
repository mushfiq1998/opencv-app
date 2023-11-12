import numpy as np
import cv2

# flag value 0 indicates gray scale image, 1 color image
# img = cv2.imread('lena.jpg', 1)

# Create image using numpy zeros() method
# img = np.zeros([height, width, 3 channels = red, green, blue], datatype)
'''So, the code creates a blank image with a black background, having a size of 512x512 pixels 
and 3 color channels. All the pixel values are initialized to zero, indicating no color intensity.
'''
img = np.zeros([512, 512, 3], np.uint8)

'''img = cv2.line(img, (starting point coordinate), (end point coordinate), 
color in BGR format), thikness)'''
# Draw line on the image
img = cv2.line(img, (0,0), (255,255), (0,0,255), 5)
# Draw an arrow line on image
img = cv2.arrowedLine(img, (0,255), (255,255), (0,0,255), 5)

'''img = cv2.rectangle(img, (top left coordinate), 
(bottom right coordinate), (color in BGR format), thikness)'''
# Draw rectangle on image
img = cv2.rectangle(img, (384,0), (510,128), (0,0,255), 5)
# Draw another rectangle on image, -1 fillup the rectangle with specific color
# img = cv2.rectangle(img, (384,0), (510,128), (0,0,255), -1)

# Draw circle on image
'''img = cv2.circle(img, (cordinate of center), center, (color), thikness)'''
img = cv2.circle(img, (447,63), 63, (0,255,0), -1)

# Write text on image
font = cv2.FONT_HERSHEY_SIMPLEX
'''img = cv2.putText(img, 'text', (coordinate of starting point), font, fontSize, 
(color in BGR format), thikness, fontType)'''
img = cv2.putText(img, 'OpenCV', (10,500), font, 4, (0,255,255), 10, cv2.LINE_AA)

cv2.imshow('Image', img)

'''when this method takes 0 as argument, it will not be disappeared 
until you close it'''
cv2.waitKey(0)
cv2.destroyAllWindows()