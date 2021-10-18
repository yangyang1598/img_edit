##흑백사진 중간에 색깔 이미지 붙이기
import cv2
import numpy as np
img=cv2.imread('animal-05.jpg',cv2.IMREAD_COLOR)
h,w=img.shape[:2]
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_gray=cv2.cvtColor(img_gray,cv2.COLOR_GRAY2BGR)


img_temp = img[int(h*0.25):int(h*0.75),int(w*0.25):int(w*0.75),:]
h1,w1=img_temp.shape[:2]

img_gray[int(h*0.25):int(h*0.75),int(w*0.25):int(w*0.75),:]=img_temp




# a=cv2.hconcat([img,img_gray])
cv2.imshow("img",img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()