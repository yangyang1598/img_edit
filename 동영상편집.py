import cv2
import numpy as np

cap=cv2.VideoCapture("cute song.mp4")

if cap.isOpened()==False:
    print("카메라를 열 수 없습니다")
    exit(1)

while True:

    rt,img_frame=cap.read()

    # 동영상이 끝나면 재생되는 프레임의 위치를 0으로 다시 지정
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    img_frame=cv2.resize(img_frame,None,fx=0.3,fy=0.3)
    h, w = img_frame.shape[:2]
    img_gray = cv2.cvtColor(img_frame, cv2.COLOR_BGR2GRAY)
    img_gray = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)
    zero = np.zeros((h, w, 1), dtype=np.uint8)
    img_b, img_g, img_r = cv2.split(img_frame)
    img_b1 = cv2.merge((img_b, zero, zero))
    img_g1 = cv2.merge((zero, img_g, zero))
    img_r1 = cv2.merge((zero, zero, img_r))

    video=cv2.hconcat([img_frame,img_gray,img_b1,img_g1,img_r1])
    cv2.imshow('video', video)


    key=cv2.waitKey(33)#waitkey(time(ms)),즉 33밀리세컨드마다 동영상을 재생하기위한 장치
    if key==27:
        break


cap.release()
cv2.destroyAllWindows()