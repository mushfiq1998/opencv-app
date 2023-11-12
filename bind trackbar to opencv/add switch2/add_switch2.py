# Add switch using trackbar to convert colored image to gray scale image.
# It does not work properly 
import numpy as np
import cv2 as cv

'''Define call back function using the signature 'nothing' used as 5th 
argument in callback function while creating trackbar.
Here, x is the value of current position of your trackbar'''
def nothing(x):
    print('x: ', x)

# create a nameWindow with the name image
cv.namedWindow('image')

'''Create trackbars in image window.
cv.createTrackbar('trackbarName', 'windowName', value - initial value at
which trackbar is set, count - final value you want to set for your 
trackbar, onChange - call back function which will be called whenever 
trackbar value changes).
I want to change BGR value of image using trackbar.
Add 'B' trackbar in the 'image' window.'''
# Here, cp for current position
cv.createTrackbar('cp', 'image', 10, 400, nothing)
# Add switch creating trackbar to convert colored image to gray scale image 
switch = 'color/gray'
cv.createTrackbar(switch, 'image', 0, 255, nothing)

# while True:
while(1):
    #img = cv.imread('face-rec.jpg') 
    img = cv.imread('opencv2.webp')

    '''Get current position (value) of trackbar 'B' on image.
    b = cv.getTrackbarPos('trackbarName', 'WindowName - in which window 
    trackbar is present')'''
    pos = cv.getTrackbarPos('cp', 'image')
    font = cv.FONT_HERSHEY_SIMPLEX
    # Write current position of trackbar on image.
    cv.putText(img, str(pos), (50,150), font, 5, (0,0,255), 5)

    k = cv.waitKey(1)
    # If the pressed key is escape key
    if k == 27:
        break
    '''The value of the trackbar is retrieved using cv.getTrackbarPos().
    and stored in variable s
    # Get the current position of switch'''
    s = cv.getTrackbarPos(switch, 'image')
    # If the switch is OFF, we want to do nothing
    # If the position of this trackbar is 0
    if s == 0:
        pass
    # If switch is ON, convert colored image to gray scale image
    else:
        # Convert colored image to gray scale image
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # img = cv.imshow('image', img)

cv.destroyAllWindows()
