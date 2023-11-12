# Object detection and tracking. 
import numpy as np
import cv2 

cv2.namedWindow('Tracking') 

while True:
    # Image read
    frame = cv2.imread('course.PNG') 
    
    cv2.imshow('frame', frame)

    k = cv2.waitKey(1)
    # If the pressed key is escape key
    if k == 27:
        break

cv2.destroyAllWindows()
