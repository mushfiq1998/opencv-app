# Object detection and tracking. 
import numpy as np
import cv2 

while True:
    # Image read
    frame = cv2.imread('course.PNG') 

    # Convert colored image into a HSV image. 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # we will threshold the HSV image for a range of blue color.
    # Define lower range of blue color for HSV image inside np array.
    # lower_blue = np.array([110, 50, 50])
    lower_blue = np.array([57, 49, 50])
    # Define upper range of blue color for HSV image inside np array
    # upper_blue = np.array([130, 250, 250])
    upper_blue = np.array([85, 250, 250])

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

cv2.destroyAllWindows()
