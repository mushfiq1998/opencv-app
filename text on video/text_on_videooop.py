import cv2

class MouseEvent:

    def __init__(self, webcam_index, pressed_key):
        self.webcam_index = webcam_index
        self.pressed_key = pressed_key

    def mouse_event(self):
        cap = cv2.VideoCapture(self.webcam_index)
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
                k = cv2.waitKey(self.pressed_key)
                if k == ord('q'):
                    break
            else:
                break
        
        cap.release()
        cv2.destroyAllWindows()
        
webcam_index = 0
pressed_key = 1
# Create object
obj = MouseEvent(webcam_index, pressed_key)
# Function call
obj.mouse_event()