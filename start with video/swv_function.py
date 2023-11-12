import cv2

def with_video(webcam_index , video):

    cap = cv2.VideoCapture(webcam_index)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    out = cv2.VideoWriter(video, fourcc, 20.0, (640, 480))

    print(cap.isOpened())

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

            out.write(frame)
        
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('Frame', gray)

            k = cv2.waitKey(1)
            if k == ord('q'):
                break
        else:
            break

    cap.release()
    out.release()

webcam_index = 0
video = 'output.avi'
# Function call
with_video(webcam_index , video)

cv2.destroyAllWindows()