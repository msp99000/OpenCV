
import numpy as np
import cv2

capture = cv2.VideoCapture('/home/mikee/Documents/Sublime Text 3/OpenCV/MyDroneShot_MiKee.mp4')

while True:
    ret, frame = capture.read()
    width = int(capture.get(3))
    height = int(capture.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', result)
    cv2.imshow('mask', mask)

    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()