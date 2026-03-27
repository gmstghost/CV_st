# 이미지 윤곽선 검출

import cv2 as cv
import tkinter as tk
from tkinter import filedialog
from matplotlib import pyplot as plt

# 트랙바 조정 시 콜백
def on_trackbar(x):
    pass

# 파일 선택기 열어서 이미지 파일 선택
files = filedialog.askopenfilenames(initialdir="/",\
                 title = "파일 열기",\
                    filetypes = (("*.jpg","*jpg"),("*.png","png")))

# 트랙바 넣을 윈도우 생성
cv.namedWindow('Canny')

# 트랙바 생성
cv.createTrackbar('low threshold', 'Canny', 0, 1000, on_trackbar)
cv.createTrackbar('high threshold', 'Canny', 0, 1000, on_trackbar)

# 초기값 설정
cv.setTrackbarPos('low threshold', 'Canny', 50)
cv.setTrackbarPos('high threshold', 'Canny', 150)

# 이미지를 그레이스케일로 열기
img_gray = cv.imread(files[0], cv.IMREAD_GRAYSCALE)

while (1):
    # 트랙바 위치
    low = cv.getTrackbarPos('low threshold', 'Canny')
    high = cv.getTrackbarPos('high threshold', 'Canny')

    # 파라미터 지정
    img_canny = cv.Canny(img_gray, low, high)

    # 실행 결과 출력
    cv.imshow('Canny', img_canny)

    if cv.waitKey(1) & 0xFF == 27:
        break

cv.destroyAllWindows()
