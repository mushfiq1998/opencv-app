import cv2
import datetime

class Date:

    def __init__(self, webcam_index):
        self.webcam_index = webcam_index

    def date_time(self):
        cap = cv2.VideoCapture(self.webcam_index)
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                font = cv2.FONT_HERSHEY_SIMPLEX
                current_datetime = str(datetime.datetime.now())
                frame = cv2.putText(frame, current_datetime, (10,50), font, 1, 
                                    (0,255,255), 2, cv2.LINE_AA)
                cv2.imshow('Frame', frame)
                k = cv2.waitKey(1)
                if k == ord('q'):
                    break
            else:
                break

        cap.release()

webcam_index = 0
obj = Date(webcam_index)

# Function call
obj.date_time()

cv2.destroyAllWindows()