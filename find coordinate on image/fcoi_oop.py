import numpy as np
import cv2

class Find:

    def __init__(self, img):
        self.img = img

    def find_coordinate(self):

        def click_event(event, x, y, flags, params):
            if event == cv2.EVENT_LBUTTONDOWN:
                cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
                print('coordinate of x y: ', (x, y))
                points.append((x, y))
                if len(points) >= 2:
                    cv2.line(img, points[-1], points[-2], (0, 0, 255), 4)
                cv2.imshow('Image', img)

        img = cv2.imread(self.img)
        cv2.imshow('Image', img)
        points = []
        cv2.setMouseCallback('Image', click_event)

img = 'Messi4.jpg'
# Create object
obj = Find(img)

# function call
obj.find_coordinate()

cv2.waitKey(0)
cv2.destroyAllWindows()