import numpy as np
import cv2
import logging

logging.basicConfig(level=logging.INFO, format="[%(levelname)s %(lineno)d] %(message)s")    # 로그 출력 형식 설정

cap = cv2.VideoCapture(0)                  # 카메라 연결
cam_w = 0                                  # 카메라 화면 너비
cam_h = 0                                  # 카메라 화면 높이

# hsv 배열, 기타변수 초기화
min_hsv = np.array([179,255,255])
max_hsv = np.array([0,0,0])
tmp1 = np.array([0,0,0])
tmp2 = np.array([0,0,0])
lst = np.array([])
cnt=0

# TrackBar 업데이트시 콜백함수
def ch(pos):
    pass

# openCV Window 생성 
cv2.namedWindow("Trackbar Windows")
cv2.namedWindow("res")
cv2.namedWindow("dst")

# TrackBar 생성
cv2.createTrackbar("min_H", "Trackbar Windows", 0, 179, ch)
cv2.createTrackbar("min_S", "Trackbar Windows", 0, 255, ch)
cv2.createTrackbar("min_V", "Trackbar Windows", 0, 255, ch)
cv2.createTrackbar("max_H", "Trackbar Windows", 0, 179, ch)
cv2.createTrackbar("max_S", "Trackbar Windows", 0, 255, ch)
cv2.createTrackbar("max_V", "Trackbar Windows", 0, 255, ch)

# TrackBar 기본값 설정
cv2.setTrackbarPos("min_H", "Trackbar Windows", 179)
cv2.setTrackbarPos("min_S", "Trackbar Windows", 255)
cv2.setTrackbarPos("min_V", "Trackbar Windows", 255)

# 마우스 클릭시 
def mouse_event(event, x, y, _, param):
    if event == cv2.EVENT_FLAG_LBUTTON:
        global min_hsv, max_hsv, tmp1, tmp2, lst, cnt
        if cnt == 0:
            lst = np.array([hsv[y,x]])

        lst = np.append(lst, [hsv[y,x]], axis=0)

        if len(lst)>=20:
            lst = lst[-19:]
        
        if cnt>=5:
            tmp1 = min_hsv
            tmp2 = max_hsv
            min_hsv = np.min(lst,axis=0)
            max_hsv = np.max(lst,axis=0)

            if np.array_equal(tmp1,min_hsv) == False:
                logging.info(f"MIN HSV CHANGED! {tmp1} -> {min_hsv}")
                cv2.setTrackbarPos("min_H", "Trackbar Windows", int(min_hsv[0]))
                cv2.setTrackbarPos("min_S", "Trackbar Windows", int(min_hsv[1]))
                cv2.setTrackbarPos("min_V", "Trackbar Windows", int(min_hsv[2]))

            if np.array_equal(tmp2,max_hsv) == False:
                logging.info(f"MAX HSV CHANGED! {tmp2} -> {max_hsv}")
                cv2.setTrackbarPos("max_H", "Trackbar Windows", int(max_hsv[0]))
                cv2.setTrackbarPos("max_S", "Trackbar Windows", int(max_hsv[1]))
                cv2.setTrackbarPos("max_V", "Trackbar Windows", int(max_hsv[2]))
        cnt+=1
    return


while cv2.waitKey(1) != ord('q'):
    cam_ret, dst = cap.read()                   # 카메라 사용 여부와 카메라 화면 추출

    if not cam_ret:                                                 # 카메라가 비활성화 되어있다면
        logging.warning("CameraError: Failed to capture camera")    # 경고 레벨로 로그 출력
        exit()
    dst = cv2.GaussianBlur(dst, (0, 0), 10)     # 기본 화면에 강도 10의 블러 효과
    hsv = cv2.cvtColor(dst, cv2.COLOR_BGR2HSV)  # 기본 화면의 BGR 색공간을 HSV 색공간으로 변환
    cam_h, cam_w = dst.shape[:2]                # 카메라 화면의 높이와 너비 추출

    # hsv 최대 최소 설정    
    min_hsv = cv2.getTrackbarPos("min_H", "Trackbar Windows"), cv2.getTrackbarPos("min_S", "Trackbar Windows"), cv2.getTrackbarPos("min_V", "Trackbar Windows")
    max_hsv = cv2.getTrackbarPos("max_H", "Trackbar Windows"), cv2.getTrackbarPos("max_S", "Trackbar Windows"), cv2.getTrackbarPos("max_V", "Trackbar Windows")

    mask = cv2.inRange(hsv, min_hsv, max_hsv)       # mask 적용
    cv2.setMouseCallback("dst", mouse_event, dst)   # 마우스 콜백함수 mouse_event로 지정

    # openCV 창 표시
    cv2.imshow("res", mask)
    cv2.imshow("dst",dst)

cv2.destroyAllWindows()