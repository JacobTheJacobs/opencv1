import cv2
import numpy as np

#import and convert to gray scale
img = cv2.imread('max.jpg',cv2.IMREAD_GRAYSCALE)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('comedyGray.jpg',img)
