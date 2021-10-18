import cv2
import numpy as np

img=cv2.imread("welcome.jpg",cv2.IMREAD_COLOR)
img_b,img_g,img_r=cv2.split(img)
imgbgr=cv2.merge((img_b,img_g,img_r))

h,w=imgbgr.shape[:2]

zero=np.zeros((h,w,1),dtype=np.uint8)
img_b1=cv2.merge((img_b,zero,zero))
img_g1=cv2.merge((zero,img_g,zero))
img_r1=cv2.merge((zero,zero,img_r))

cv2.imshow("wow",img)
cv2.imshow("b",img_b1)
cv2.imshow("g",img_g1)
cv2.imshow("r",img_r1)
cv2.waitKey(0)
cv2.destroyAllWindows()