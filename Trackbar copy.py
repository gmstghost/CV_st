import numpy as np
import cv2
import logging

logging.basicConfig(level=logging.INFO, format="[%(levelname)s %(lineno)d] %(message)s")    # 로그 출력 형식 설정

cap = cv2.VideoCapture(0)                  # 카메라 연결
cam_w = 0                                  # 카메라 화면 너비
cam_h = 0                                  # 카메라 화면 높이

# hsv 배열, 기타변수 초기화
max=[179,255,255]
hsv_val=np.array([0,0,0,0,0,0])
l=np.array([])
cnt=0

# TrackBar 업데이트시 콜백함수
def ch(pos):
    global hsv_val
    hsv_val = cv2.getTrackbarPos("min_H", "Tr"), cv2.getTrackbarPos("min_S", "Tr"), cv2.getTrackbarPos("min_V", "Tr"), 
    cv2.getTrackbarPos("max_H", "Tr"), cv2.getTrackbarPos("max_S", "Tr"), cv2.getTrackbarPos("max_V", "Tr")

# openCV Window 생성 
cv2.namedWindow("Tr")
cv2.namedWindow("res")
cv2.namedWindow("dst")

for i,t in enumerate(["min_H", "min_S", "min_V", "max_H", "max_S", "max_V"]):
    cv2.createTrackbar(t, "Tr", 0, max[i%3], ch)

# 마우스 클릭시 
def mouse_event(event, x, y, _, param):
    if event == cv2.EVENT_FLAG_LBUTTON:
        global hsv_val, cnt

        if cnt == 0:
            hsv_val=np.append(hsv[y,x],hsv[y,x])
            print(hsv_val)
        
        tmp1=hsv_val[:3]
        tmp2=hsv_val[3:]
        if cnt !=0:

            tmp1=np.minimum(tmp1, hsv[y,x])
            tmp2=np.maximum(tmp2, hsv[y,x])
            hsv_val=np.append(tmp1,tmp2)
            print(hsv[y,x], hsv_val)

        logging.info(f"MIN HSV CHANGED 2 {hsv_val[:3]}")
        for i,t in enumerate(["min_H", "min_S", "min_V"]):
            cv2.setTrackbarPos(t, "Tr", int(tmp1[i]))
            
        logging.info(f"MAX HSV CHANGED 2 {hsv_val[3:]}")
        for i,t in enumerate(["max_H", "max_S", "max_V"]):
            cv2.setTrackbarPos(t, "Tr", int(tmp2[i]))
        cnt+=1
    return


while cv2.waitKey(1) != ord('q'):
    cam_ret, dst = cap.read()   # 카메라 사용 여부와 카메라 화면 추출

    if not cam_ret:                                                 # 카메라가 비활성화 되어있다면
        logging.warning("CameraError: Failed to capture camera")    # 경고레벨로 로그 출력
        exit()
    dst = cv2.GaussianBlur(dst, (0, 0), 5)      # 기본 화면에 강도 10의 블러 효과
    hsv = cv2.cvtColor(dst, cv2.COLOR_BGR2HSV)  # 기본 화면의 BGR 색공간을 HSV 색공간으로 변환
    cam_h, cam_w = dst.shape[:2]                # 카메라 화면의 높이와 너비 추출

    mask = cv2.inRange(hsv, hsv_val[:3], hsv_val[3:])   # mask 적용
    cv2.setMouseCallback("dst", mouse_event, dst)       # 마우스 콜백함수 mouse_event로 지정

    if cv2.waitKey(1)== ord('r'):
        cnt=0
        hsv_val=np.array([0,0,0,0,0,0])
        for i in ["min_H", "min_S", "min_V", "max_H", "max_S", "max_V"]:
            cv2.setTrackbarPos(i, "Tr", 0)
        
    # openCV 창 표시
    cv2.imshow("res", mask)
    cv2.imshow("dst",dst)
cv2.destroyAllWindows()