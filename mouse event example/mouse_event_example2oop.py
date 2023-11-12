import numpy as np
import cv2

class MouseEvent:

    def __init__(self):
        pass
    
    def click_event(self, event, x, y, flags, params):
        if event == cv2.EVENT_LBUTTONDOWN:
            cv2.circle(img, (x, y), 15, (0, 0, 255), -1)
            points.append((x, y))
            if len(points) >= 2:
                cv2.line(img, points[-1], points[-2], (0, 0, 255), 4)
            cv2.imshow('Image', img)

img = cv2.imread('lena.jpg')
cv2.imshow('Image', img)
points = []
# Create object
obj = MouseEvent()
# Function call
cv2.setMouseCallback('Image', obj.click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()