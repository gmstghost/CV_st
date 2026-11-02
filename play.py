## 노는곳

# import cv2 as cv

# img_gray = cv.imread("resource1.jpg", cv.IMREAD_COLOR)
# img_gray1 = cv.imread("resource1.jpg", cv.IMREAD_GRAYSCALE)

# # copy 메소드로 데이터 복사
# img_copyed1 = img_gray1.copy()

# # id 리턴 다름
# print(id(img_gray),id(img_copyed1))

# #cv.line(img_gray, (0,0), (200,200), 0, 10)

# ret1, img_gray1 = cv.threshold(img_gray1, 127, 255, cv.THRESH_BINARY)

# print(id(img_gray),id(img_copyed1))

# cv.imshow("img_gray", img_gray)
# cv.imshow("img_gray1", img_gray1)
# cv.imshow("img_copyed1", img_copyed1)

# cv.waitKey(0)

##############################################################

# import cv2 as cv
# import numpy as np

# img_color = cv.imread("resource1.jpg", cv.IMREAD_COLOR)

# h, w = img_color.shape[:2]

# b = img_color[:, :, 0].astype(np.float32)
# g = img_color[:, :, 1].astype(np.float32)
# r = img_color[:, :, 2].astype(np.float32)

# img_gray = (r*0.2126 + g*0.7152 + b*0.0722).astype(np.uint8)

# img_result = cv.cvtColor(img_gray, cv.COLOR_GRAY2BGR)

# img_result[150:201, 200:251] = (0, 255, 0)

# cv.imshow('color', img_color)
# cv.imshow('result', img_result)

# cv.waitKey(0)
# cv.destroyAllWindows()

# ################################################################

# import cv2 as cv
# import sys

# img_color = cv.imread("resource1.jpg", cv.IMREAD_COLOR)
# if img_color is None:
#     print("No Image!")
#     exit(1)

# # 그레이스케일 변환
# img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)

# # 적응형 이진화 적용 
# img_binary = cv.adaptiveThreshold(img_gray,255,
# cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,5,4)

# red = (0,0,255)
# green = (0,255,0)
# white = (255,255,255)
# yellow = (0,255,255)

# location = (50,100)
# font = cv.FONT_HERSHEY_SCRIPT_SIMPLEX
# fontScale = 3.5
# cv.putText(img_binary,'Little Rabbit and the Big Bad Leopard',location,font,0.8,yellow,2)

# cv.imshow('Color', img_color)
# cv.imshow('Grayscale', img_gray)
# cv.imshow('Binary', img_binary)
# cv.waitKey(0)






# import cv2 as cv
# import numpy as np

# mouse_is_pressing = False
# start_x, start_y, end_x, end_y = 0,0,0,0
# step = 0

# def swap(v1,v2):
#     temp = v1
#     v1 = v2
#     v2 = temp

# # 마우스 왼쪽 버튼을 누르면 ROI 시작점
# # 마우스 왼쪽 버튼을 떼면 ROI 끝점
# # 마우스 이동 시 ROI 영역을 초록색 사각형으로
# def mouse_callback(event,x,y,flags,param):
#     global step,start_x,end_x,start_y,end_y,mouse_is_pressing
#     if event == cv.EVENT_LBUTTONDOWN:
#         step = 1    
#         mouse_is_pressing = True
#         start_x = x
#         start_y = y

#     elif event == cv.EVENT_MOUSEMOVE:
#         # 마우스를 누른 상태이면 현재 마우스 커서 위치를
#         # ROI 끝점을 저장하여 현재 선택된 ROI 영역을 보여주도록
#         if mouse_is_pressing:
#             end_x = x
#             end_y = y
#             step = 2

#     elif event == cv.EVENT_LBUTTONUP:
#         mouse_is_pressing = False
#         end_x = x
#         end_y = y
#         step = 3

# cap = cv.VideoCapture(0)
# if cap.isOpened() == False:
#     print*("Failed to open camera")
#     exit(-1)

# cv.namedWindow("color")
# cv.setMouseCallback("color", mouse_callback)

# while True:
#     ret, img_color = cap.read()

#     if ret == False:
#         print("Failed to capture")

#     if step == 1:
#         cv.circle(img_color, (start_x, start_y),10,(0,255,0),-1);
    
#     elif step == 2:
#         # 좌클릭시 움직이는 영역 초록 사각형으로
#         cv.rectangle(img_color,(start_x, start_y), (end_x, end_y), (0,255,0),3);

#     elif step == 3:
#         if start_x > end_x:
#             swap(start_x, end_x)
#             swap(start_y, end_y)

#         # ROI에서 평균 계산
#         img_roi = img_color[start_y:end_y,start_x:end_x]
#         m = cv.mean(img_roi)

#         # 평균 픽셀로 채운 이미지 생성
#         img_mean = np.zeros(img_roi.shape,dtype=np.uint8)
#         img_mean[:] = (m[0],m[1],m[2])

#         cv.imshow('mean', img_mean)
#         cv.imshow('roi',img_roi)
#         cv.rectangle(img_color,(start_x, start_y), (end_x, end_y), (0,255,0),3); 
#     cv.imshow('color',img_color)
    
#     if cv.waitKey(25) > 0:
#         break;







# import cv2 as cv
# import numpy as np

# mouse_is_pressing = False
# start_x, start_y, end_x, end_y = 0,0,0,0
# step = 0

# def safe_destroy(name):
#     try:
#         if cv.getWindowProperty(name, cv.WND_PROP_VISIBLE) >= 1:
#             cv.destroyWindow(name)
#     except:
#         pass

# def swap(v1,v2):
#     temp = v1
#     v1 = v2
#     v2 = temp

# # 마우스 왼쪽 버튼을 누르면 ROI 시작점
# # 마우스 왼쪽 버튼을 떼면 ROI 끝점
# # 마우스 이동 시 ROI 영역을 초록색 사각형으로
# def mouse_callback(event,x,y,flags,param):
#     global step,start_x,end_x,start_y,end_y,mouse_is_pressing
#     if event == cv.EVENT_LBUTTONDOWN:
#         step = 1    
#         mouse_is_pressing = True
#         start_x = x
#         start_y = y

#         # 🔹 이전 ROI/mean 창 제거
#         if cv.getWindowProperty("roi", cv.WND_PROP_VISIBLE) >= 1:
#             cv.destroyWindow("roi")
#         if cv.getWindowProperty("mean", cv.WND_PROP_VISIBLE) >= 1:
#             cv.destroyWindow("mean")


#     elif event == cv.EVENT_MOUSEMOVE:
#         # 마우스를 누른 상태이면 현재 마우스 커서 위치를
#         # ROI 끝점을 저장하여 현재 선택된 ROI 영역을 보여주도록
#         if mouse_is_pressing:
#             end_x = x
#             end_y = y
#             step = 2

#     elif event == cv.EVENT_LBUTTONUP:
#         mouse_is_pressing = False
#         end_x = x
#         end_y = y
#         step = 3

# cv.namedWindow("color")
# cv.setMouseCallback("color", mouse_callback)

# while True:
#     img_color = cv.imread("EpGpT0AUYAI4U7s_1.jpg", cv.IMREAD_COLOR)

#     if step == 1:
#         cv.circle(img_color, (start_x, start_y),10,(0,255,0),-1);
    
#     elif step == 2:
#         # 좌클릭시 움직이는 영역 초록 사각형으로
#         cv.rectangle(img_color,(start_x, start_y), (end_x, end_y), (0,255,0),3);

#     elif step == 3:
#         x1, x2 = sorted([start_x, end_x])
#         y1, y2 = sorted([start_y, end_y])

#         if x2 - x1 <= 1 or y2 - y1 <= 1:
#             step = 0
#             continue

#         img_roi = img_color[y1:y2, x1:x2]
#         m = cv.mean(img_roi)
#         img_mean = np.full(img_roi.shape, (m[0], m[1], m[2]), dtype=np.uint8)
#         cv.imshow("roi", img_roi)
#         cv.imshow("mean", img_mean)
#         cv.rectangle(img_color, (x1, y1), (x2, y2), (0,255,0), 3)
#     cv.imshow('color',img_color)
    
#     if cv.waitKey(25) > 0:
#         break





# import cv2
# import numpy as np
# from tkinter import colorchooser

# colorpick = colorchooser.askcolor()
# print(colorpick[0])



import numpy as np
import cv2
import logging
from tkinter import filedialog

logging.basicConfig(level=logging.INFO, format="[%(levelname)s %(lineno)d] %(message)s")    # 로깅 기본설정

# 0: ASUS Webcam, 1: OBS 가상 카메라
cap = cv2.VideoCapture(1)
cam_w = 0
cam_h = 0

hsv_val=np.array([0,0,0,0,0,0])     # HSV 최댓값 최솟값 지정
l=np.array([])                      # 빈 배열 생성
cnt=0

cv2.namedWindow("blended")
files = filedialog.askopenfilenames(initialdir="/",\
                 title = "파일 열기",\
                    filetypes = (("*.jpg","*jpg"),("*.png","png")))

# 마우스 이벤트 콜백
def mouse_event(event, x, y, _, param):
    if event == cv2.EVENT_FLAG_LBUTTON:
        global hsv_val, cnt     # 전역변수 선언

        if cnt == 0:    # 영역 선택 첫번째일 때 리스트에 바로 추가
            hsv_val = np.append(hsv[y,x],hsv[y,x])
            print(hsv_val)
        
        tmp1=hsv_val[:3]    # 기존 최솟값 임시 저장
        tmp2=hsv_val[3:]    # 기존 최댓값 임시 저장

        if cnt !=0:     # 최대 최소 각각 선택해서 리스트에 추가
            tmp1=np.minimum(tmp1, hsv[y,x])
            tmp2=np.maximum(tmp2, hsv[y,x])
            hsv_val=np.append(tmp1,tmp2)
            print(hsv[y,x], hsv_val)

        logging.info(f"MIN HSV CHANGED 2 {hsv_val[:3]}")    # HSV 최솟값 로깅
        logging.info(f"MAX HSV CHANGED 2 {hsv_val[3:]}")    # HSV 최댓값 로깅
        cnt += 1
        print(cnt)
    return

while True:
    src = cv2.imread(files[0], cv2.IMREAD_COLOR)
    logging.debug(type(hsv_val[:3]), type(hsv_val[3:]),hsv_val[:3],hsv_val[3:])
    dst = cv2.GaussianBlur(src, (0, 0), 5)              # 기본 화면에 강도 5의 블러 효과
    hsv = cv2.cvtColor(dst, cv2.COLOR_BGR2HSV)          # 기본 화면의 BGR 색공간을 HSV 색공간으로 변환
    cam_h, cam_w = dst.shape[:2]                        # 카메라 화면의 높이와 너비 추출

    mask = cv2.inRange(hsv, hsv_val[:3], hsv_val[3:])   # hsv 배열에서 최소~최대 범위의 마스크
    mask2 = np.zeros_like(dst)                          # dst와 같은 형태의 배열 복사
    mask2[mask > 0] = [255, 0, 0]                   # mask 있을때 노란색 씌움
    cv2.setMouseCallback("blended", mouse_event, dst)   # 마우스콜백 설정

    key = cv2.waitKey(1)
    if key == ord('r'):     # r키 누르면 초기화
        cnt=0
        hsv_val=np.array([0,0,0,0,0,0])     # 배열 초기화
    elif key == ord('q'):
        logging.info("Pressed 'Q'")
        break

    if mask.shape is not None:
        blended = cv2.addWeighted(dst, 1.0, mask2, 0.5, 0)      # 영상 혼합

    cv2.imshow("blended", blended)
cv2.destroyAllWindows()