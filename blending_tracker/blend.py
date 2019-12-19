import cv2
import numpy as np
from matplotlib import pyplot as plt

def nop(x):
  pass

cv2.namedWindow('Blending')

cv2.createTrackbar("Alpha", "Blending" , 0,10, nop)
cv2.createTrackbar("Beta" ,  "Blending", 0,10, nop)
cv2.createTrackbar("Gamma",  "Blending", 0,10, nop)


img1 = cv2.imread('C:\\Users\\student\\Desktop\\33.jpg')
img2 = cv2.imread('C:\\Users\\student\\Desktop\\44.jpg')
new_w, new_h = 640, 640
img1 = cv2.resize(img1, (new_w, new_h), interpolation = cv2.INTER_AREA)
img2 = cv2.resize(img2, (new_w, new_h), interpolation = cv2.INTER_AREA)

while (1): 
    a = cv2.getTrackbarPos("Alpha", "Blending")
    b = cv2.getTrackbarPos("Beta",  "Blending")
    c = cv2.getTrackbarPos("Gamma",  "Blending")
    dst = cv2.addWeighted(img1,a/10,img2,b/10, c/10)
    cv2.imshow('dst',dst)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
      break

cv2.destroyAllWindows()