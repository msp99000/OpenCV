# Working with Live Videos

import numpy as np
import cv2


# To capture Live Video from Webcam, use the code below
# capture = cv2.VideoCapture(0)

# But here I'm using my own Source, so I'll just enter my file name
capture = cv2.VideoCapture('MyDroneShot_MiKee.mp4')


while True:
    
    ret, frame = capture.read()
    width = int(capture.get(3))
    height = int(capture.get(4))

    image = np.zeros(frame.shape, np.uint8)

    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)
    image[height//2:, :width//2] = smaller_frame
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)
    image[height//2:, width//2:] = smaller_frame

    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()