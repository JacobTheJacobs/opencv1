import cv2
import numpy as np

#load the image
img = cv2.imread('max.jpg',cv2.IMREAD_COLOR)

#draw a line
#(where to draw),(start),(end),(color),(width)
cv2.line(img,(0,0),(150,150),(255,255,255),15)

#draw rectangle
cv2.rectangle(img,(15,25),(200,150),(0,255,0),5)

#draw circle -1 will fill shape
cv2.circle(img,(100,63),55,(0,0,255),-1)

#draw pologyn
pts=np.array([[10,155],[23,300],[702,20],[500,10]],np.int32)
#(where to draw),(points),(connect end to start),(color),(width)
cv2.polylines(img,[pts],True,(0,255,255),3)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
