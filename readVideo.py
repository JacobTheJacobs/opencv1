import cv2
import numpy

print("yeah")

frameWidth =640
frameHeight =480

cap = cv2.VideoCapture("earth.mp4")

while True:
    success,img = cap.read()

    cv2.imshow("Video",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
