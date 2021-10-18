import cv2
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread("welcome.jpg",cv2.IMREAD_COLOR)
img_b,img_g,img_r=cv2.split(img)
imgbgr=cv2.merge((img_b,img_g,img_r))
cv2.imshow("b",img_b)
cv2.imshow("g",img_g)
cv2.imshow("r",img_r)
cv2.imshow("bgr",imgbgr)
cv2.waitKey(0)
cv2.destroyAllWindow()