# Object detection and tracking. 
import numpy as np
import cv2 

while True:
    # Image read
    frame = cv2.imread('course.PNG') 

    '''Convert colored image into a HSV image. This conversion is often 
    performed because it allows for easier color-based segmentation.'''
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    '''Here, lower and upper thresholds are defined to create a mask that 
    isolates a specific color range. In this case, the code is targeting 
    a blue color range. The values specified in the arrays correspond to 
    the lower and upper limits of the HSV values for the blue color.'''
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 250, 250])

    '''Creates a binary mask where white pixels represent the areas in the 
    frame that fall within the specified color range and black pixels 
    represent the areas outside that range. in other word White pixels 
    represent the target color, while black pixels represent other colors.'''
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    '''performs a bitwise AND operation between the frame and the mask. 
    This operation retains only the pixels in the frame where the 
    corresponding mask pixels are white, effectively isolating the blue 
    object or region of interest.'''
    result = cv2.bitwise_and(frame, frame, mask = mask)

    # This is going to open three windows 
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)

    k = cv2.waitKey(1)
    # If the pressed key is escape key
    if k == 27:
        break

cv2.destroyAllWindows()
