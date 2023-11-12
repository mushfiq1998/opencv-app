# Add switch using trackbar 
import numpy as np
import cv2 as cv

'''Define call back function using the signature 'nothing' used as 5th 
argument in callback function while creating trackbar.
Here, x is the value of current position of your trackbar'''
def nothing(x):
    print('x: ', x)

# Create a black image, here height = 300, width = 512
img = np.zeros((300, 512, 3), np.uint8)
# create a nameWindow with the name image
cv.namedWindow('image')

'''Create multiple trackbars in image window.
cv.createTrackbar('trackbarName', 'windowName', value - initial value at
which trackbar is set, count - final value you want to set for your 
trackbar, onChange - call back function which will be called whenever 
trackbar value changes).
I want to change BGR value of image using trackbar.
Add 'B' trackbar in the 'image' window.'''
cv.createTrackbar('B', 'image', 0, 255, nothing)
cv.createTrackbar('G', 'image', 0, 255, nothing) 
cv.createTrackbar('R', 'image', 0, 255, nothing)
# Add switch creating trackbar 
switch = '0 : OFF\n  1: ON'
cv.createTrackbar(switch, 'image', 0, 255, nothing)

# while True:
while(1):
    cv.imshow('image', img)

    k = cv.waitKey(1)
    # If the pressed key is escape key
    if k == 27:
        break

    '''Get current position (value) of trackbar 'B' on image.
    b = cv.getTrackbarPos('trackbarName', 'WindowName - in which window 
    trackbar is present')'''
    b = cv.getTrackbarPos('B', 'image')
    g = cv.getTrackbarPos('G', 'image')
    r = cv.getTrackbarPos('R', 'image')
    s = cv.getTrackbarPos(switch, 'image')
    # If the switch is OFF, set all pixels values of img to 0
    # If the position of this trackbar is 0
    if s == 0:
        img[:] = 0
    # If switch is ON, set the pixels values to current BGR values
    else:
        '''Updating the image:
        Within the loop, the values of the trackbars are retrieved using 
        cv.getTrackbarPos(). The values are stored in variables b, g, and r 
        representing the B, G, and R channel values, respectively.
        The img array is updated with these channel values using 
        img[:] = [b, g, r]. This means that all pixels in the image will have 
        the same B, G, and R values.
        Set current b, g, r values to our image. '''
        img[:] = [b, g, r]

cv.destroyAllWindows()
