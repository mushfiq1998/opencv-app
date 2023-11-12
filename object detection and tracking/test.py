import numpy as np
import cv2

def nothing(x):
    pass

cv2.namedWindow('Tracking')
cv2.createTrackbar('LowerHue', 'Tracking', 120, 179, nothing)
cv2.createTrackbar('LowerSaturation', 'Tracking', 50, 255, nothing)
cv2.createTrackbar('LowerValue', 'Tracking', 50, 255, nothing)
cv2.createTrackbar('UpperHue', 'Tracking', 150, 179, nothing)
cv2.createTrackbar('UpperSaturation', 'Tracking', 255, 255, nothing)
cv2.createTrackbar('UpperValue', 'Tracking', 255, 255, nothing)

while True:
    frame = cv2.imread('course.PNG')
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_hue = cv2.getTrackbarPos('LowerHue', 'Tracking')
    lower_saturation = cv2.getTrackbarPos('LowerSaturation', 'Tracking')
    lower_value = cv2.getTrackbarPos('LowerValue', 'Tracking')
    upper_hue = cv2.getTrackbarPos('UpperHue', 'Tracking')
    upper_saturation = cv2.getTrackbarPos('UpperSaturation', 'Tracking')
    upper_value = cv2.getTrackbarPos('UpperValue', 'Tracking')

    lower_purple = np.array([lower_hue, lower_saturation, lower_value])
    upper_purple = np.array([upper_hue, upper_saturation, upper_value])

    mask = cv2.inRange(hsv, lower_purple, upper_purple)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    min_contour_area = 100
    max_contour_area = 5000
    min_aspect_ratio = 0.5
    max_aspect_ratio = 1.5
    ball_contours = []
    
    for contour in contours:
        area = cv2.contourArea(contour)
        x, y, width, height = cv2.boundingRect(contour)
        aspect_ratio = width / float(height)

        if min_contour_area < area < max_contour_area and min_aspect_ratio < aspect_ratio < max_aspect_ratio:
            ball_contours.append(contour)

    cv2.drawContours(frame, ball_contours, -1, (0, 255, 0), 2)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)

    k = cv2.waitKey(1)
    if k == 27:
        break

cv2.destroyAllWindows()