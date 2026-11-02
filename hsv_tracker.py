import cv2
import numpy as np
import logging

# HSV 최소, 최댓값 배열 초기화
MIN_LINE_HSV = np.array([0, 0, 0])
MAX_LINE_HSV = np.array([0, 0, 0])

# TrackBar 값 수정시 콜백되는 함수
def on_level_change(pos):
    pass

# 카메라 화면 불러오기
cap = cv2.VideoCapture(0)

img = np.zeros((480, 640), np.uint8)    # numpy 배열 초기화
cv2.namedWindow('image')                # image window 정의
cv2.namedWindow('dst')                  # dst window 정의

# TrackBar 6개 정의
cv2.createTrackbar('min_h', 'image', 0, 180, on_level_change)
cv2.createTrackbar('min_s', 'image', 0, 255, on_level_change)
cv2.createTrackbar('min_v', 'image', 0, 255, on_level_change)
cv2.createTrackbar('max_h', 'image', 0, 180, on_level_change)
cv2.createTrackbar('max_s', 'image', 0, 255, on_level_change)
cv2.createTrackbar('max_v', 'image', 0, 255, on_level_change)

# 좌클릭시 hsv 범위 선택
def click_event(event, x, y, _, param):
    if event == cv2.EVENT_FLAG_LBUTTON:
        global lst
        lst = np.append(lst, lst[y, x])

        # TrackBar 값 nparray 형식 배열로 저장
        global MIN_LINE_HSV, MAX_LINE_HSV
        MIN_LINE_HSV = np.array([cv2.getTrackbarPos('min_h', 'image'), cv2.getTrackbarPos('min_s', 'image'), cv2.getTrackbarPos('min_v', 'image')])
        MAX_LINE_HSV = np.array([cv2.getTrackbarPos('max_h', 'image'), cv2.getTrackbarPos('max_s', 'image'), cv2.getTrackbarPos('max_v', 'image')])

# 1프레임마다 키 검사, q키 입력 시
while cv2.waitKey(1) != ord('q'):
    cam_ret, dst = cap.read()   # 카메라 화면 불러오기
    if not cam_ret:             # 카메라 없을 때
        logging.warning("CameraError: Failed to capture camera")
        exit()

    dst = cv2.GaussianBlur(dst, (0, 0), 10)         # 가우시안 블러 적용
    hsv = cv2.cvtColor(dst, cv2.COLOR_BGR2HSV)      # 색공간 형식 변환
    cam_h, scam_w = dst.shape[:2]                   # 화면 크기 받아와서 dst에 적용

    mask = cv2.inRange(hsv, MIN_LINE_HSV, MAX_LINE_HSV)     # mask 적용

    # 창 표시
    cv2.imshow('image', mask)
    cv2.imshow('dst', dst)

cv2.destroyAllWindows()