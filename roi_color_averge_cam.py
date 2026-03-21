import cv2 as cv
import numpy as np

mouse_is_pressing = False
start_x, start_y, end_x, end_y = 0,0,0,0
step = 0

def safe_destroy(name):
    try:
        if cv.getWindowProperty(name, cv.WND_PROP_VISIBLE) >= 1:
            cv.destroyWindow(name)
    except:
        pass

def swap(v1,v2):
    temp = v1
    v1 = v2
    v2 = temp

# 마우스 왼쪽 버튼을 누르면 ROI 시작점
# 마우스 왼쪽 버튼을 떼면 ROI 끝점
# 마우스 이동 시 ROI 영역을 초록색 사각형으로
def mouse_callback(event,x,y,flags,param):
    global step,start_x,end_x,start_y,end_y,mouse_is_pressing
    if event == cv.EVENT_LBUTTONDOWN:
        step = 1    
        mouse_is_pressing = True
        start_x = x
        start_y = y

        # 🔹 이전 ROI/mean 창 제거
        if cv.getWindowProperty("roi", cv.WND_PROP_VISIBLE) >= 1:
            cv.destroyWindow("roi")
        if cv.getWindowProperty("mean", cv.WND_PROP_VISIBLE) >= 1:
            cv.destroyWindow("mean")


    elif event == cv.EVENT_MOUSEMOVE:
        # 마우스를 누른 상태이면 현재 마우스 커서 위치를
        # ROI 끝점을 저장하여 현재 선택된 ROI 영역을 보여주도록
        if mouse_is_pressing:
            end_x = x
            end_y = y
            step = 2

    elif event == cv.EVENT_LBUTTONUP:
        mouse_is_pressing = False
        end_x = x
        end_y = y
        step = 3

cap = cv.VideoCapture(0)
if cap.isOpened() == False:
    print*("Failed to open camera")
    exit(-1)

cv.namedWindow("color")
cv.setMouseCallback("color", mouse_callback)

while True:
    ret, img_color = cap.read()

    if ret == False:
        print("Failed to capture")
        break;
    
    if step == 1:
        cv.circle(img_color, (start_x, start_y),10,(0,255,0),-1);
    
    elif step == 2:
        # 좌클릭시 움직이는 영역 초록 사각형으로
        cv.rectangle(img_color,(start_x, start_y), (end_x, end_y), (0,255,0),3);

    elif step == 3:
        x1, x2 = sorted([start_x, end_x])
        y1, y2 = sorted([start_y, end_y])

        if x2 - x1 <= 1 or y2 - y1 <= 1:
            step = 0
            continue

        img_roi = img_color[y1:y2, x1:x2]
        m = cv.mean(img_roi)
        img_mean = np.full(img_roi.shape, (m[0], m[1], m[2]), dtype=np.uint8)
        cv.imshow("roi", img_roi)
        cv.imshow("mean", img_mean)
        cv.rectangle(img_color, (x1, y1), (x2, y2), (0,255,0), 3)
    cv.imshow('color',img_color)
    
    if cv.waitKey(25) > 0:
        break