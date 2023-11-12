import cv2

def mouse_event(webcam_index, pressed_key):
    cap = cv2.VideoCapture(webcam_index)
    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            font = cv2.FONT_HERSHEY_SIMPLEX
            text = 'width: ' + str(cap.get(3)) + ' Height: ' + str(cap.get(4)) 
            frame = cv2.putText(frame, text, (10,50), font, 1, 
                                (0,255,255), 2, cv2.LINE_AA)
            cv2.imshow('Frame', frame)
            k = cv2.waitKey(pressed_key)
            if k == ord('q'):
                break
        else:
            break
    
    cap.release()
    cv2.destroyAllWindows()

pressed_key = 1
webcam_index = 0
# Function call
mouse_event(webcam_index, pressed_key)