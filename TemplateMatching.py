import cv2
import numpy as np

img_rgb = cv2.imread('look.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template = cv2.imread('find.jpg',0)
#get the shape
w, h = template.shape[::-1]

#matching images
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
#80% accuration
threshold = 0.8
#where is the shape
loc = np.where( res >= threshold)

#all locations
for pt in zip(*loc[::-1]):
    #draw rectangle
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

cv2.imshow('Detected',img_rgb)

cv2.waitKey(0)
