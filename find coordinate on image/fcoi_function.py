import numpy as np
import cv2

def find_coordinate(img):

    def click_event(event, x, y, flags, params):
        if event == cv2.EVENT_LBUTTONDOWN:
            cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
            print('coordinate of x y: ', (x, y))
            points.append((x, y))
            if len(points) >= 2:
                cv2.line(img, points[-1], points[-2], (0, 0, 255), 4)
            cv2.imshow('Image', img)

    img = cv2.imread(img)
    cv2.imshow('Image', img)
    points = []
    cv2.setMouseCallback('Image', click_event)

img = 'Messi4.jpg'
# function call
find_coordinate(img)

cv2.waitKey(0)
cv2.destroyAllWindows()