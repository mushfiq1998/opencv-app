import numpy as np
import cv2
'''
It is the name of the callback function that will be executed when a 
mouse event occurs. It is a user-defined function that you need to 
implement separately.'''
def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        # cv2.circle(img, (cordinate of center), radius, (color), thikness)
        cv2.circle(img, (x, y), 15, (0, 0, 255), -1)
        print('coordinate of x y: ', (x, y))
        points.append((x, y))
        if len(points) >= 2:
            '''img = cv2.line(img, (starting point coordinate), 
            (end point coordinate), color in BGR format), thikness)'''
            cv2.line(img, points[-1], points[-2], (0, 0, 255), 4)
        cv2.imshow('Image', img)

img = cv2.imread('lena.jpg')
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