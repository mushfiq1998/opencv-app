import cv2
import datetime
'''capture life from default camera of my pc. here 0 is device index of my 
camera by default, this index is either 0 in most cases or in many devives
-1. Here, cap refers to the video capture object that you have created using 
OpenCV. It is responsible for accessing video files or camera streams.'''
cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
'''Assossiate number for cv2.CAP_PROP_FRAME_WIDTH is 3 and for cv2.CAP_PROP_FRAME_HEIGHT is 4.
you can use these numbers instead of these properties.'''
# If the file is opened successfully it returns True, otherwise False
# capture frames continuously through while loop
# while True:
while(cap.isOpened()):
    '''read() returns true if the frame is available, otherwise false.
    Boolean value is stored in ret variable. and this meyhod also returns
    frame that is stored in frame variable in this case.'''
    ret, frame = cap.read()
    if ret == True:
        # Write text on image
        font = cv2.FONT_HERSHEY_SIMPLEX
        '''img = cv2.putText(img, 'text', (coordinate of starting point), font, fontSize, 
        (color in BGR format), thikness, fontType)
        text = 'width: ' + str(cap.get(3)) + ' Height: ' + str(cap.get(4)) 
        frame = cv2.putText(frame, text, (10,50), font, 1, (0,255,255), 2, cv2.LINE_AA)'''
        current_datetime = str(datetime.datetime.now())
        frame = cv2.putText(frame, current_datetime, (10,50), font, 1, 
                            (0,255,255), 2, cv2.LINE_AA)
        cv2.imshow('Frame', frame)
        k = cv2.waitKey(1)
        if k == ord('q'):
            break
    else:
        break
'''Release the capture variable. After reading the video you need to release the resources.
Release or close the video capture from the device that you have opened for reading video frames.'''
cap.release()
cv2.destroyAllWindows()