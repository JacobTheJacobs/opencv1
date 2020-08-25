import cv2
import numpy as np

#load the image
img = cv2.imread('max.jpg',cv2.IMREAD_COLOR)

#reference specific pixels
px = img[55,55]

#change a pixel
img[55,55] = [0,0,0]

#re-reference
px = img[55,55]
print(px)

#ROI, or Region of Image
px = img[100:150,100:150]
print(px)

#modify the ROI
img[100:150,100:150] = [255,255,255]
print(img.shape)
print(img.size)
print(img.dtype)

#region of the image
face_face = img[37:111,107:194]

#set the region to this region
img[0:74,0:87] = face_face

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
