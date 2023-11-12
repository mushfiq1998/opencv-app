import cv2
import datetime

def date_time(webcam_index):
    cap = cv2.VideoCapture(webcam_index)
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
# Function call
date_time(webcam_index)

cv2.destroyAllWindows()