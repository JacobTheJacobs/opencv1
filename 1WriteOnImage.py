import cv2
import numpy as np

#load the image
img = cv2.imread('max.jpg',cv2.IMREAD_COLOR)

#write on the image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'WAZZZUUUUUUUUUUUUUUUUUUUUUUPPPPPPPP!',(0,130), font, 1, (200,255,155), 2, cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
