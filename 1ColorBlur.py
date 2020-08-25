import cv2
import numpy as np

cap = cv2.VideoCapture("people.mp4")

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #ranges here, basically 170-255, 150-255, and 50-180 BGR hue sta value
    lower_red = np.array([170, 150, 70])
    upper_red = np.array([255, 255, 150])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    #blur
    kernel = np.ones((15,15),np.float32)/225
    smoothed = cv2.filter2D(res,-1,kernel)
    # GaussianBlur
    blur = cv2.GaussianBlur(res,(15,15),0)
    # MedianBlur
    median = cv2.medianBlur(res,15)
    # BilateralBlur
    bilateral = cv2.bilateralFilter(res, 15, 75, 75)
    

    cv2.imshow('Original',frame)
    cv2.imshow('Averaging',smoothed)
    cv2.imshow('Gaussian Blurring',blur)
    cv2.imshow('Median Blur',median)
    cv2.imshow('bilateral Blur', bilateral)



    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
