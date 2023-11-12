# it does not work properly
import cv2

'''capture life from default camera of my pc. here 0 is device index of my 
camera by default, this index is either 0 in most cases or in many devives
-1. Here, cap refers to the video capture object that you have created using 
OpenCV. It is responsible for accessing video files or camera streams.'''
cap = cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
'''
Assossiate number for cv2.CAP_PROP_FRAME_WIDTH is 3 and for cv2.CAP_PROP_FRAME_HEIGHT is 4.
you can use these numbers instead of these properties.'''
# Set property using set() method
# cap.set(number assossiated for propetty, we want to change the width of frame to this number)
cap.set(3, 6000)
cap.set(4, 6000)
print('New width and height of frame after setting')
print(cap.get(3))
print(cap.get(4))

# If the file is opened successfully it returns True, otherwise False
# capture frames continuously through while loop
# while True:
while(cap.isOpened()):
    '''read() returns true if the frame is available, otherwise false.
    Boolean value is stored in ret variable. and this meyhod also returns
    frame that is stored in frame variable in this case.'''
    ret, frame = cap.read()
    if ret == True:
        # Convert colored (BGR) image into gray scale image
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Frame', gray)

        # cv2.imshow('Frame', frame)

        k = cv2.waitKey(1)
        if k == ord('q'):
            break
    else:
        break

'''Release the capture variable. After reading the video you need to release the resources.
Release or close the video capture from the device that you have opened for reading video frames.'''
cap.release()
cv2.destroyAllWindows()