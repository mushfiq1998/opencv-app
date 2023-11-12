import cv2

'''capture life from default camera of my pc. here 0 is device index of my 
camera by default, this index is either 0 in most cases or in many devives
-1. Here, cap refers to the video capture object that you have created using 
OpenCV. It is responsible for accessing video files or camera streams.'''
cap = cv2.VideoCapture(0)

# Get Fourcc
# fourcc = cv2.VideoWriter_fourcc(fourcc code)
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# Save captured video
'''
output = cv2.VideoWriter(nameOfOutputFile, fourcc code, 
noOfFrames perSecond, size of video)'''
# Fourcc is a 4 byte code used to specify video codecs
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

# cap = cv2.VideoCapture(8)
# If the file is opened successfully it returns True, otherwise False
print(cap.isOpened())

# capture frames continuously through while loop
# while True:
while (cap.isOpened()):
    '''
    read() returns true if the frame is available, otherwise false.
    Boolean value is stored in ret variable. and this meyhod also returns
    frame that is stored in frame variable in this case.'''
    ret, frame = cap.read()
    if ret == True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        out.write(frame)
    
        # Convert colored (BGR) image into gray scale image
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Frame', gray)

        # cv2.imshow('Frame', frame)

        k = cv2.waitKey(1)
        if k == ord('q'):
            break
    else:
        break

'''Release the capture variable. After reading the video you need to 
release the resources.
Release or close the video capture from the device that you have 
opened for reading video frames.'''
cap.release()
out.release()
cv2.destroyAllWindows()