import cv2
import numpy as np

cap = cv2.VideoCapture("people.mp4")

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #ranges here, basically 170-255, 150-255, and 50-180 BGR
    lower_red = np.array([170, 150, 50])
    upper_red = np.array([255, 255, 150])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
