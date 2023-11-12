import numpy as np
import cv2
'''
It is the name of the callback function that will be executed when a 
mouse event occurs. It is a user-defined function that you need to 
implement separately.'''
def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        # cv2.circle(img, (cordinate of center), radius, (color), thikness)
        cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
        points.append((x, y))
        if len(points) >= 2:
            '''img = cv2.line(img, (starting point coordinate), 
            (end point coordinate), color in BGR format), thikness)'''
            cv2.line(img, points[-1], points[-2], (0, 0, 255), 1)
        cv2.imshow('Image', img)

# Create image using numpy zeros() method
# img = np.zeros([height, width, 3 channels = red, green, blue], datatype)
'''So, the code creates a blank image with a black background, having a 
size of 512x512 pixels and 3 color channels. All the pixel values are 
initialized to zero, indicating no color intensity.'''
img = np.zeros([512, 512, 3], np.uint8)
# img = cv2.imread('lena.jpg')
cv2.imshow('Image', img)
points = []
'''It is a function that allows to specify a callback function 
to handle mouse events.'''
cv2.setMouseCallback('Image', click_event)
'''
when this method takes 0 as argument, it will not be disappeared 
until you close it'''
cv2.waitKey(0)
cv2.destroyAllWindows()