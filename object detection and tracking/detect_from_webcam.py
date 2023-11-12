# Detect blue color object from webcam using trackbar 
import numpy as np
import cv2 

def nothing(x):
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow('Tracking')
# Create six trackbars to define HSV dynamicly
cv2.createTrackbar('LowerHue', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('LowerSaturation', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('LowerValue', 'Tracking', 0, 255, nothing)

cv2.createTrackbar('UpperHue', 'Tracking',  255, 255, nothing)
cv2.createTrackbar('UpperSaturation', 'Tracking',  255, 255, nothing)
cv2.createTrackbar('UpperValue', 'Tracking',  255, 255, nothing)

while True:
    # Read frame from default waecam
    _, frame = cap.read() 

    # Convert colored image into a HSV image. 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get current position of the above trackbars
    lower_hue = cv2.getTrackbarPos('LowerHue', 'Tracking')
    lower_saturation = cv2.getTrackbarPos('LowerSaturation', 'Tracking')
    lower_value = cv2.getTrackbarPos('LowerValue', 'Tracking')

    upper_hue = cv2.getTrackbarPos('UpperHue', 'Tracking')
    uper_saturation = cv2.getTrackbarPos('UpperSaturation', 'Tracking')
    upper_value = cv2.getTrackbarPos('UpperValue', 'Tracking')

    # we will threshold the HSV image for a range of blue color.
    # Define lower range of blue color for HSV image inside np array.
    # lower_blue = np.array([110, 50, 50])
    lower_blue = np.array([lower_hue, lower_saturation, lower_value])
    # Define upper range of blue color for HSV image inside np array
    # upper_blue = np.array([130, 250, 250])
    upper_blue = np.array([upper_hue, uper_saturation, upper_value])

    '''Threshold the HSV image to get only the blue color.
    the input image (hsv), the lower threshold array 
    mask = cv2.inRange(input image - hsv, the lower threshold array, 
    the upper threshold array)'''
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    '''result = cv2.bitwise_and(frame, frame, mask = mask)
    Peroforms bitwise_and operation to mask the original image.
    result = cv2.bitwise_and(the source input array, the destination output
    array - same image, the mask array - attribute is set in order to apply
    the mask for the lower_blue value and upper_blue value)'''
    result = cv2.bitwise_and(frame, frame, mask = mask)

    # This is going to open three windows 
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    # cv2.imshow('hsv', hsv)
    cv2.imshow('result', result)

    k = cv2.waitKey(1)
    # If the pressed key is escape key
    if k == 27:
        break

cap.relaese()
cv2.destroyAllWindows()
