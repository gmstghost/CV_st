# 코드 끝나면 엔터 3번
# 소챕터 끝나면 엔터 5번
# 챕터 끝나면 엔터 8번

# 2-1 이미지 다루기
# 2.1.1 이미지 파일을 읽어서 화면에 보여주기

# import cv2

# # 이미지를 numpy 배열로 대입
# img_color = cv2.imread("cat on laptop.jpg", cv2.IMREAD_COLOR)

# # 이미지 없을 때
# if img_color is None:
#     print("No Image!")
#     exit(1)

# cv2.namedWindow('Color')        # Window 생성, 타이틀바 지정
# cv2.imshow('Color', img_color)  # Window에 이미지 표시
# cv2.waitKey(0)                  # 키보드 입력 대기
# cv2.destroyAllWindows()         # 윈도우 종료



# 2.1.2 읽어온 이미지를 그레이 스케일 이미지로 변롼 후 저장하기

# import cv2

# # 컬러 이미지로 파일 읽어오기
# img_color = cv2.imread("cat on laptop.jpg", cv2.IMREAD_COLOR)

# # 이미지 없을 때
# if img_color is None:
#     print("No Image!")
#     exit(1)

# # 컬러 이미지 화면에 보여주기
# cv2.namedWindow('Color')        # Window 생성, 타이틀바 지정
# cv2.imshow('Color', img_color)  # Window에 이미지 표시

# cv2.waitKey(0)                  # 키보드 입력 대기

# img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)  # 그레이 스케일 이미지 변환

# cv2.imshow('Grayscale', img_gray)       # Window에 이미지 표시
# cv2.imwrite("grayscale.jpg", img_gray)  # 그레이스케일 이미지 저장
# cv2.waitKey(0)                          # 아무 키 입력
# cv2.destroyAllWindows()                 # 윈도우 종료



# # 2-2 동영상 다루기
# # 2.2.1 카메라에서 캡쳐한 이미지를 화면에 보여주기

# import cv2 as cv

# # 이미지 캡쳐용 객체 생성
# cap = cv.VideoCapture(0)

# # 카메라 연결 확인
# if cap.isOpened() == False:
#     print("Failed to open camera")
#     exit(1)

# # 프레임 출력 반복
# while(True):
#     # 이미지 읽어오기
#     ret, img_frame = cap.read()

#     # 캠쳐 실패 시
#     if ret == False:
#         print("Failed to Capture")

#     # 윈도우에 출력
#     cv.imshow('Color', img_frame)

#     # 키보드 입력 대기
#     key = cv.waitKey(1)

#     # ESC 시 종료
#     if key == 27:
#         break

# # 카메라 연결 종료
# cap.release()
# cv.destroyAllWindows()



# # 2.2.2 카메라에서 캡쳐한 이미지를 동영상 파일로 저장하기

# import cv2 as cv

# # 이미지 캡쳐용 객체 생성
# cap = cv.VideoCapture(0)

# # 카메라 연결 확인
# if cap.isOpened() == False:
#     print("Failed to open camera")
#     exit(1)

# # 이미지 읽어오기
# ret, img_frame = cap.read()

# # 캡쳐 실패 시
# if ret == False:
#     print("Failed to Capture")
#     exit(1)

# # 코덱 지정
# codec = cv.VideoWriter_fourcc('M', 'J', 'P', 'G');

# # 프레임 지정
# fps = 30.0

# # 이미지 크기 불러오기
# h, w = img_frame.shape[:2]

# # 동영상 저장용 객체 생성
# writer = cv.VideoWriter("output.avi", codec, fps, (w,h))

# # 객체 초기화 확인
# if writer.isOpened() == False:
#     print("Video capture is not ready")
#     exit(1)

# while(True):
#     # 이미지 캡쳐
#     ret, img_frame = cap.read()

#     if ret == False:
#         print("Failed to Capture")
#         exit(1)

#     # 이미지를 파일에 저장
#     writer.write(img_frame)
#     cv.imshow(img_frame)

#     key = cv.waitKey(1)
#     if key == 27:
#         break

# cap.release()

# # 동영상 저장 완료
# writer.release();

# cv.destroyAllWindows()



# # 2.2.3 동영상 파일 재생하기

# import cv2 as cv

# # 재생할 파일 지정
# cap = cv.VideoCapture("output.avi")

# # 카메라 연결 확인
# if cap.isOpened() == False:
#     print("Failed to open camera")
#     exit(1)

# while(True):
#     ret, img_frame = cap.read()

#     # 동영상 재생 완료
#     if ret == False:
#         print("Video playing finished")
#         break

#     cv.imshow('Color', img_frame)

#     # 동영상 재생 속도 조정
#     key = cv.waitKey(25)
#     if key == 27:
#         break

# cap.release()
# cv.destroyAllWindows()








# # 3-1 색공간
# # 3.1.1 RGB 색공간
# # 3.1.2 Grayscale 색공간
# # 3.1.3 HSV 색공간





# # 3-2 픽셀과 이미지 개념





# # 3-3 Mat 객체와 넘파이 배열
# # 3.3.1 같은 이미지 데이터 공유

# import cv2 as cv 

# img_gray = cv.imread("cat on laptop.jpg", cv.IMREAD_GRAYSCALE)

# # 대입 연산자
# img_copyed1 = img_gray

# # 같은 numpy 배열 가리킴
# # 리턴 같음
# print(id(img_gray), id(img_copyed1))

# # 배열 공유하므로 두개 배열에 선 그려짐
# cv.line(img_gray, (0,0), (100,100), 0, 10)

# # 이진화 적용 시 배열이 별개가 됨
# ret, img_gray = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)

# # 달라진 리턴값 출력
# print(id(img_gray), id(img_copyed1))

# # img_copyed1에는 영향 없고 img_gray만 이진화
# cv.imshow("img_gray", img_gray)
# cv.imshow("img_copyed1", img_copyed1)

# cv.waitKey(0)



# # 3.3.2 이미지 복사본 생성

# import cv2 as cv

# img_gray = cv.imread("resource1.jpg", cv.IMREAD_GRAYSCALE)

# # copy 메소드로 데이터 복사
# img_copyed1 = img_gray.copy()

# # id 리턴 다름
# print(id(img_gray),id(img_copyed1))

# cv.line(img_gray, (0,0), (200,200), 0, 10)

# ret1, img_gray = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)

# print(id(img_gray),id(img_copyed1))

# cv.imshow("img_gray", img_gray)
# cv.imshow("img_copyed1", img_copyed1)

# cv.waitKey(0)





# # 3-4 픽셀에 접근하는 방법

# import cv2 as cv
# import numpy as np

# img_color = cv.imread("resource1.jpg", cv.IMREAD_COLOR)

# # 이미지크기 가져오기
# h, w = img_color.shape[:2]

# # 그레이스케일 저장할 배열
# img_gray = np.zeros((h,w), np.uint8)

# # for문으로 (x,y)픽셀 접근
# for y in range(0,h):
#     for x in range(0,w):

#         # 컬러이미지 픽셀의 bgr채널 읽기
#         b = img_color.item(y,x,0)
#         g = img_color.item(y,x,1)
#         r = img_color.item(y,x,2)

#         # 픽셀에 그레이스케일 저장
#         gray = int(r*0.2126 + g*0.7152 + b*0.0722)

#         img_gray.itemset(y,x,gray)

# # 컬러이미지 변환
# img_result = cv.cvtColor(img_gray, cv.COLOR_GRAY2BGR)

# # y: 150~200, x: 200~250을 초록색으로
# for y in range(150, 201):
#     for x in range(200, 251):
#         img_result.itemset(y,x,0,0)     # b
#         img_result.itemset(y,x,1,255)   # g
#         img_result.itemset(y,x,2,0)     # r

# cv.imshow('color', img_color)
# cv.imshow('result', img_result)

# cv.waitKey(0)

# cv.destroyAllWindows()

# ################# 업 데 이 트  #################

# import cv2 as cv
# import numpy as np

# img_color = cv.imread("resource1.jpg", cv.IMREAD_COLOR)

# h, w = img_color.shape[:2]

# b = img_color[:, :, 0].astype(np.float32)
# g = img_color[:, :, 1].astype(np.float32)
# r = img_color[:, :, 2].astype(np.float32)

# img_gray = (r*0.2126 + g*0.7152 + b*0.0722).astype(np.uint8)

# img_result = cv.cvtColor(img_gray, cv.COLOR_GRAY2BGR)

# img_result[340:531, 0:220] = (0, 255, 0)

# cv.imshow('color', img_color)
# cv.imshow('result', img_result)

# cv.waitKey(0)
# cv.destroyAllWindows()





# # 3-5 이미지 채널 분리 및 합치기
# import cv2 as cv

# img_color = cv.imread('resource1.jpg', cv.IMREAD_COLOR)

# # 컬러 이미지 채널별로 분리
# img_b, img_g, img_r = cv.split(img_color)

# # 조합해서 컬러 영상 생성
# img_result = cv.merge((img_b, img_g, img_r))

# cv.imshow("Color", img_result)
# cv.imshow("B", img_b)
# cv.imshow("G", img_g)
# cv.imshow("R", img_r)

# cv.waitKey(0)
# cv.destroyAllWindows








# # 4-1 트랙바

# import cv2 as cv

# # 트랙바 조정 시 콜백
# def on_trackbar(x):
#     pass

# # 트랙바 넣을 윈도우 생성
# cv.namedWindow('Canny')

# # 트랙바 생성
# cv.createTrackbar('low threshold', 'Canny', 0, 1000, on_trackbar)
# cv.createTrackbar('high threshold', 'Canny', 0, 1000, on_trackbar)

# # 초기값 설정
# cv.setTrackbarPos('low threshold', 'Canny', 50)
# cv.setTrackbarPos('high threshold', 'Canny', 150)

# # 이미지를 그레이스케일로 열기
# img_gray = cv.imread('resource1.jpg', cv.IMREAD_GRAYSCALE)

# while (1):
#     # 트랙바 위치
#     low = cv.getTrackbarPos('low threshold', 'Canny')
#     high = cv.getTrackbarPos('high threshold', 'Canny')

#     # 파라미터 지정
#     img_canny = cv.Canny(img_gray, low, high)

#     # 실행 결과 출력
#     cv.imshow('Canny', img_canny)

#     if cv.waitKey(1) & 0xFF == 27:
#         break

# cv.destroyAllWindows()





# # 4-2 키보드 이벤트

# import cv2 as cv
# import sys

# cap = cv.VideoCapture(0)
# if cap.isOpened() == False:
#     print("Failed to open camera")
#     exit(1)

# # 출력 결과 지정
# step = 1

# while(True):
#     ret, img_frame = cap.read()

#     if ret == False:
#         print("Failed to Capture")
#         break;

#     # step > 2 : 그레이스케일
#     if step > 1:
#         img_frame = cv.cvtColor(img_frame, cv.COLOR_BGR2GRAY)

#         # 3일때 에지 이미지
#         if step > 2:
#             img_frame = cv.Canny(img_frame, 30, 90)

#     cv.imshow('Result', img_frame)

#     key = cv.waitKey(1)

#     if key == 27:
#         break

#     # 입력 키별로 다른 값 대입
#     elif key == ord('1'):
#         step = 1
#     elif key == ord('2'):
#         step = 2
#     elif key == ord('3'):
#         step = 3





# # 4-3 마우스 이벤트

# import cv2 as cv
# import numpy as np
# import random

# # 좌클릭 상태체크
# mouse_is_pressing = False
# # 그리기 모드 선택
# drawing_mode = True
# # 좌클릭 초기값
# start_x, start_y = -1,-1
# # 도형 내부채움 색상
# color = (255,255,255)
# # 결과 저장 이미지
# img = np.zeros((512,512,3), np.uint8)

# # 마우스 이벤트 콜백함수 정의
# def mouse_callback(event,x,y,flags,param):
#     global color,start_x,start_y,drawing_mode,mouse_is_pressing

#     # 마우스 이동
#     if event == cv.EVENT_MOUSEMOVE:
#         # 좌클릭 이동
#         if mouse_is_pressing == True:
#             # 도형 그리기
#             if drawing_mode == True:
#                 cv.rectangle(img,(start_x,start_y),(x,y), color, -1)
#             else:
#                 cv.circle(img, (start_x, start_y), max(abs(start_x-x),
#                     abs(start_y-y)),color,-1)
                
#     # 좌클릭
#     elif event == cv.EVENT_LBUTTONDOWN:
#         # 랜덤 색지정
#         color = (random.randrange(256), random.randrange(256),
#                 random.randrange(256))
#         # 좌클릭 확인
#         mouse_is_pressing = True
#         # 좌클릭 위치 저장
#         start_x, start_y = x,y
    
#     # 좌클릭 해제
#     elif event == cv.EVENT_LBUTTONUP:
#         # 좌클릭 해제 확인
#         mouse_is_pressing = False

#         # 도형 그리기
#         if drawing_mode == True:
#             cv.rectangle(img,(start_x,start_y),(x,y), color, -1)
#         else:
#             cv.circle(img, (start_x, start_y), max(abs(start_x-x),
#                 abs(start_y-y)),color,-1)
    
#     # 우클릭
#     elif event == cv.EVENT_RBUTTONDOWN:
#         drawing_mode = 1 - drawing_mode

# cv.namedWindow('image')

# # 윈도우에 대한 마우스 콜백함수
# cv.setMouseCallback('image',mouse_callback)

# while(1):
#     cv.imshow('image', img)

#     key = cv.waitKey(1)
#     if key == 27:
#         break

# cv.destroyAllWindows()





# 4-4 하나의 윈도우에 2개 이상 이미지 보여주기

# import cv2 as cv
# import sys

# img_color = cv.imread("resource1.jpg", cv.IMREAD_COLOR)

# if img_color is None:
#     print("No Image!")
#     exit(1)

# # 그레이스케일 변환
# img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)

# # 에지 검출
# img_canny = cv.Canny(img_gray,90,180)

# # 윈도우 분리해서 출력
# cv.imshow("Color", img_color)
# cv.imshow("Grayscale",img_gray)
# cv.imshow("Canny",img_canny)

# cv.waitKey(0)
# cv.destroyAllWindows()  

# ##################################

# import cv2 as cv
# import sys

# img_color = cv.imread("resource1.jpg", cv.IMREAD_COLOR)

# if img_color is None:
#     print("No Image!")
#     exit(1)

# # 그레이스케일 변환
# img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)

# # 에지 검출
# img_canny = cv.Canny(img_gray,90,180)

# img_gray = cv.cvtColor(img_gray, cv.COLOR_GRAY2BGR)
# img_canny = cv.cvtColor(img_canny, cv.COLOR_GRAY2BGR)

# # 연결할 입력
# # 수평방향
# img_result = cv.hconcat([img_gray, img_canny])
# img_result = cv.hconcat([img_color, img_result])

# # 수직방향
# # img_result = cv.vconcat([img_gray, img_canny])

# cv.imshow('Result', img_result)
# cv.waitKey(0)
# cv.destroyAllWindows()








# # 5-1 전역 임게값 사용

# import cv2 as cv
# import sys

# img_color = cv.imread("resource1.jpg", cv.IMREAD_COLOR)

# if img_color is None:
#     print("No Image!")
#     exit(1)

# # 그레이스케일 변환
# img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)

# # 암계값 127로 이진화
# retval, img_binary = cv.threshold(img_gray,127,255,cv.THRESH_BINARY)

# cv.imshow('Color', img_color)
# cv.imshow('Grayscale', img_gray)
# cv.imshow('Binary', img_binary)
# cv.waitKey(0)

# ##################################

# import cv2 as cv
# import sys

# # 트랙바 콜백함수
# def on_trackbar(x):
#     pass

# img_color = cv.imread("resource1.jpg", cv.IMREAD_COLOR)

# if img_color is None:
#     print("No Image!")
#     exit(1)

# cv.imshow('Color', img_color)

# # 그레이스케일 변환
# img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
# cv.imshow('Grayscale', img_gray)

# # 트랙바 추가
# cv.namedWindow('Binary')
# cv.createTrackbar("threshold","Binary",0,255,on_trackbar)
# cv.setTrackbarPos("threshold","Binary",127)

# while True:
#     # 트랙바 값 파라미터로
#     thresh = cv.getTrackbarPos("threshold","Binary")

#     # 임계값보다 작으면 흰색
#     retval, img_binary = cv.threshold(img_gray,thresh,255,cv.THRESH_BINARY)

#     cv.imshow('Binary',img_binary)

#     if cv.waitKey(1) & 0xFF == 27:
#         break





# # 5-2 적응형 이진화

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

# cv.imshow('Color', img_color)
# cv.imshow('Grayscale', img_gray)
# cv.imshow('Binary', img_binary)
# cv.waitKey(0)








# # 6-1 블렌딩

# import cv2 as cv

# alpha = 0.0
# beta = 1.0

# while alpha <= 1.0:
#     # 루프 시작 시 새로고침
#     img1 = cv.imread('960_.png',cv.IMREAD_COLOR)
#     img2 = cv.imread('siuuuuuuu.png',cv.IMREAD_COLOR)

#     # 블렌딩 적용
#     dst = cv.addWeighted(img1,alpha,img2,beta,0)

#     # 파라미터 확인
#     print(alpha,"",beta)

#     cv.imshow('dst', dst)
#     cv.waitKey(0)

#     # 가중치 조절
#     alpha = round(alpha + 0.1, 1)
#     beta = round(beta - 0.1, 1)

# cv.destroyAllWindows()





# # 6-2 차영상

# import cv2 as cv

# img_back = cv.imread('bb.png', cv.IMREAD_COLOR)
# img_object = cv.imread('aa.png', cv.IMREAD_COLOR)

# # 차영상 추출 (순서 중요)
# img_sub = cv.subtract(img_object,img_back)

# # # 차영상 이진화
# # retval, img_binary = cv.threshold(img_sub,50,250,cv.THRESH_BINARY)

# cv.imshow('background',img_back)
# cv.imshow('object',img_object)
# cv.imshow('sub',img_sub)
# # cv.imshow('binary',img_binary)
# cv.waitKey(0)



# # 6-3 이미지 비트 연산

# import cv2 as cv
# import numpy as np

# img_logo = cv.imread('naverwebtoon.png',cv.IMREAD_COLOR)
# img_bck = cv.imread('YOR.png',cv.IMREAD_COLOR)

# # 로고 이진화
# img_gray = cv.cvtColor(img_logo, cv.COLOR_BGR2GRAY)
# ret, img_mask = cv.threshold(img_gray,200,255,cv.THRESH_BINARY)

# # 반전 이미지
# img_mask_inv = cv.bitwise_not(img_mask)

# h,w = img_logo.shape[:2]
# img_roi = img_bck[0:h,0:w]

# # 로고에서 배경지우기, 배경에서 로고위치지우기
# img1 = cv.bitwise_and(img_logo,img_logo,mask=img_mask_inv)
# img2 = cv.bitwise_and(img_roi,img_roi,mask=img_mask)

# # 합쳐서 결과
# dst = cv.add(img1,img2)

# # 결과 배경에 복사
# img_bck[0:h,0:w] = dst

# cv.imshow('background',img_bck)
# cv.waitKey(0)





# # 6-4 관심 영역 설정

# import cv2 as cv

# img_color = cv.imread('resource1.jpg', cv.IMREAD_COLOR)

# h,w = img_color.shape[:2]
# center_x, center_y = int(w*0.5),int(h*0.5)

# # 이미지 중심에서 일정 거리를 ROI영역으로
# img_roi = img_color[center_y-100:center_y+100,center_x-100:center_x+100].copy()

# # 변환 후 Canny edge 구하기
# img_gray = cv.cvtColor(img_roi, cv.COLOR_BGR2GRAY)
# img_edge = cv.Canny(img_gray,100,300)

# img_edge = cv.cvtColor(img_edge,cv.COLOR_GRAY2BGR)

# # 원본에 ROI 복사
# img_color[center_y-100:center_y+100,center_x-100:center_x+100] = img_edge

# cv.imshow("COLOR", img_color)
# cv.imshow("ROI",img_roi)

# cv.waitKey(0)
# cv.destroyAllWindows()








# # 7-1 OpenCV 좌표계

# import numpy as np
# import cv2 as cv

# # 빈 넘파이 배열
# w = 640
# h = 480

# img = np.zeros((h,w,3),np.uint8)

# # 이미지 너비, 높이, 채널 수 가져오기
# img_h = img.shape[0]
# img_w = img.shape[1]
# img_bpp = img.shape[2]

# print(img_h, img_w, img_bpp)

# cv.circle(img, (100,300), 10, (0,255,255),-1)

# cv.imshow("drawing",img)
# cv.waitKey(0);





# # 7-2 무작위 색 사용

# import cv2 as cv
# import numpy as np
# from random import randint

# w = 640
# h = 480

# img = np.zeros((h,w,3), np.uint8)

# img_h = img.shape[0]
# img_w = img.shape[1]

# for y in range(img_h):
#     for x in range(img_w):
#         # 픽셀별로 다른 색 가지도록
#         img.itemset(y,x,0,randint(0.255))   # b
#         img.itemset(y,x,1,randint(0.255))   # g
#         img.itemset(y,x,2,randint(0.255))   # r

# cv.imshow("drawing",img)
# cv.waitKey(0);





# # 7-3 사각형 그리기

# import numpy as np
# import cv2 as cv

# w = 640
# h = 480
# bpp = 3

# img = np.zeros((h,w,bpp),np.uint8)

# # 선굵기 3인 빨간색 사각형을 그립니다.
# cv.rectangle(img,(50,50),(450,450),(0,0,255),3)

# # 내부가 초록색으로 채워진 사각형을 그립니다.
# cv.rectangle(img,(10,200),(250,300),(0,255,0),-1)

# # 내부가 마젠타색으로 채워진 사각형을 그립니다.
# cv.rectangle(img,(300,150,50,100),(255,0,255),-1)

# cv.imshow("result",img)
# cv.waitKey(0);





# # 7-4 원 그리기

# import numpy as np
# import cv2 as cv

# w = 640
# h = 480
# bpp = 3

# img = np.zeros((h,w,bpp), np.uint8)

# # 중점 (320,240), 반지름 10, 초록색 내부채움 원
# cv.circle(img,(320,240),10,(0,255,0), -1)

# # 중점 (320,240), 반지름 100, 빨간색, 선굵기 1 원
# cv.circle(img,(320,240),100,(0,0,255), 1)

# cv.imshow("result",img)
# cv.waitKey(0)





# # 7-5 선분 그리기 

# import numpy as np
# import cv2 as cv

# w = 640
# h = 480
# bpp = 3

# img = np.zeros((h,w,bpp), np.uint8)

# # 선굵기 3인 대각선 2개 교차
# cv.line(img,(w-1,0),(0,h-1),(0,255,0),3)
# cv.line(img,(0,0),(w-1,h-1),(0,0,255),3)

# cv.imshow("result",img)
# cv.waitKey(0)





# # 7-6 타원 그리기

# import numpy as np
# import cv2 as cv

# w = 640
# h = 480
# bpp = 3

# img = np.zeros((h,w,bpp), np.uint8)

# center = (int(w/2), int(h/2))

# # x축 방향 반지름 길이 200, y축 방향 반지름 길이 10인 노란색 타원
# cv.ellipse(img,center,(200,10),0,0,360,(0,255,255),3)

# #축 방향 반지름 길이 10, y축 방향 반지름 길이 200인 녹색 타원
# cv.ellipse(img,center,(10,200),0,0,360,(0,0,255),3)

# cv.imshow("result",img)
# cv.waitKey(0);

# ##################################

# import numpy as np
# import cv2 as cv

# w = 640
# h = 480
# bpp = 3

# img = np.zeros((h,w,bpp), np.uint8)

# center = (int(w/2), int(h/2))

# cv.ellipse(img, center, (10, 200), 0, 0, 360, (0, 255, 0), 3 )
# cv.ellipse(img, center, (10, 200), 45, 0, 360, (0, 0, 255), 3)
# cv.ellipse(img, center, (10, 200), -45, 0, 360, (0, 255, 255), 3)

# cv.imshow("result",img)
# cv.waitKey(0);

# ##################################

# import numpy as np
# import cv2 as cv

# w = 640
# h = 480
# bpp = 3

# img = np.zeros((h,w,bpp), np.uint8)

# center = (int(w/2), int(h/2))

# # 타원을 시계 방향으로 90도까지 그림
# cv.ellipse(img, center, (100, 100), 0, 0, 90, (0, 0, 255),3)

# cv.imshow("result", img)
# cv.waitKey(0);





# # 7-7 폴리곤 그리기

# import numpy as np
# import cv2 as cv

# w = 640
# h = 640
# bpp = 3

# img = np.zeros((h,w,bpp), np.uint8)

# red = (0,0,255)
# green = (0,255,0)
# yellow = (0,255,255)
# thickness = 2

# # 내부가 채워지지 않은 폴리곤
# pts = np.array([[315,50],[570,240],[475,550],[150,550],[50,240]],np.int32)
# pts = pts.reshape((-1,1,2))
# cv.polylines(img,[pts],True,green,thickness)

# # 내부가 노란색으로 채워진 폴리곤
# pts = pts.reshape((-1,1,2))
# cv.fillPoly(img,[pts],yellow)

# cv.imshow("drawing",img)
# cv.waitKey(0)





# # 7-8 글자 출력

# import numpy as np
# import cv2 as cv
# w = 640
# h = 480
# bpp = 3

# img = np.zeros((h,w,bpp), np.uint8)

# red = (0,0,255)
# green = (0,255,0)
# white = (255,255,255)
# yellow = (0,255,255)

# center_x = int(w/2.0)
# center_y = int(h/2.0)

# thickness = 2

# location = (center_x-200,center_y-100)
# font = cv.FONT_HERSHEY_SCRIPT_SIMPLEX
# fontScale = 3.5
# cv.putText(img,'OpenCV',location,font,fontScale,yellow,thickness)

# location = (center_x-150,center_y+20)
# font = cv.FONT_ITALIC
# fontScale = 2
# cv.putText(img,'OpenCV',location,font,fontScale,red,thickness)

# location = (center_x-250,center_y+100)
# font = cv.FONT_HERSHEY_SIMPLEX
# fontScale = 1.5
# cv.putText(img,'OpenCV',location,font,fontScale,white,thickness)

# location = (center_x-130,center_y-150)
# font = cv.FONT_HERSHEY_COMPLEX
# fontScale = 1.2
# cv.putText(img,'OpenCV',location,font,fontScale,green,thickness)

# cv.imshow("drawing", img)
# cv.waitKey(0)








# 8-1 실시간 ROI 구현

import cv2 as cv

mouse_is_pressing = False
start_x, start_y, end_x, end_y = 0,0,0,0
step = 0

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

cv.namedWindow("Color")
cv.setMouseCallback("Color", mouse_callback)

while True:
    ret, img_color = cap.read()

    if ret == False:
        print("Failed to capture")
        break;

    if step == 1:
        cv.circle(img_color, (start_x, start_y),10, (0,255,0),-1);

    elif step == 2:
        # 좌클릭시 움직이는 영역 초록 사각형으로
        cv.rectangle(img_color,(start_x, start_y), (end_x, end_y), (0,255,0),3);

    elif step == 3:
        if start_x > end_x:
            swap(start_x, end_x)
            swap(start_y, end_y)

        #시작점 y좌표:끝점 y좌표, 시작점 좌표: 끝점 좌표
        ROI = img_color[start_y:end_y, start_x:end_x]
        ROI = cv.cvtColor(ROI, cv.COLOR_BGR2GRAY)
        ROI = cv.Canny(ROI, 150, 50)
        ROI = cv.cvtColor(ROI, cv.COLOR_GRAY2BGR)

        # 원본에 ROI 복사
        img_color[start_y:end_y, start_x:end_x] = ROI
    
    cv.imshow('Color', img_color);

    if cv.waitKey(25) > 0:
        break;





# # 8-2 ROI 평균 색 추출하기

# import cv2 as cv
# import numpy as np

# capture = cv.VideoCapture(0)

# while True:
#     ret, img_color = capture.read()
#     img_result = img_color.copy()

#     h, w = img_color.shape[:2]
#     center_x = int(w*0.5)
#     center_y = int(h*0.5)

#     # ROI 영역 빨간색 사각형으로
#     cv.rectangle(img_result, (center_x-100, center_y-100),
#                      (center_x+100, center_y+100), (0,0,255),3)
        
#     # ROI에서 평균 계산
#     img_roi = img_color[center_y-100:center_y+100,center_x-100:center_x+100]
#     m = cv.mean(img_roi)

#     # 평균 픽셀로 채운 이미지 생성
#     img_mean = np.zeros(img_roi.shape,dtype=np.uint8)
#     img_mean[:] = (m[0],m[1],m[2])

#     cv.imshow('mean', img_mean)
#     cv.imshow('color',img_result)
#     cv.imshow('roi',img_roi)

#     key = cv.waitKey(1)
#     if key == 27:
#         break








# # 9-1 회전

# import cv2 as cv

# img_color = cv.imread('resource1.jpg')
# cv.imshow("color", img_color)

# h, w = img_color.shape[:2]

# # 센터를 중심으로 CCW 45도 회전시키는 행렬
# M = cv.getRotationMatrix2D((w/2.0,h/2.0),45,0.55)

# # 행렬 M img_color에 적용
# img_rotated = cv.warpAffine(img_color,M,(w,h))

# cv.imshow("rotation", img_rotated)
# cv.waitKey(0)
# cv.destroyAllWindows()





# # 9-2 크기 조정

# import cv2 as cv

# img_color = cv.imread('EpGpT0AUYAI4U7s.jpg')
# cv.imshow("original",img_color)

# h,w = img_color.shape[:2]
# img_result = cv.resize(img_color,None,fx=0.5,fy=0.5,interpolation=cv.INTER_AREA)
# cv.imshow("x0.5 INTER_CUBIC",img_result)




# # 9-3 이동

# import cv2 as cv
# import numpy as np

# img_color = cv.imread('resource1.jpg')
# cv.imshow("original", img_color)

# h,w = img_color.shape[:2]

# # 이미지를 우측으로 100, 아래로 50 이동시키는 이동 행렬
# M = np.float32([[1,0,100],[0,1,50]])

# # 이미지에 적용
# # img_translation = cv.warpAffine(img_color,M, (w,h))
# img_translation = cv.warpAffine(img_color, M, (w+100, h+50))    # 원본이미지 모두나오게

# cv.imshow("translation", img_translation)

# cv.waitKey(0)
# cv.destroyAllWindows()





# # 9-4 아핀 변환

# import numpy as np
# import cv2 as cv

# point_list = []

# def mouse_callback(event,x,y,flags,param):
#     if event == cv.EVENT_LBUTTONDOWN:
#         # 리스트에 좌표 저장
#         print("(%d, %d)" % (x,y))
#         point_list.append((x,y))
#         cv.circle(img_color, (x,y),3,(0,0,255),-1)

# # 마우스 콜백함수 등록
# cv.namedWindow('source')
# cv.setMouseCallback('source',mouse_callback)

# img_color = cv.imread('resource1.jpg')

# # 마우스 클릭으로 세 점 지정
# while(True):
#     cv.imshow('source',img_color)

#     # 스페이스바 루프 탈출
#     if cv.waitKey(1) == 32:
#         break

#     h,w = img_color.shape[:2]

# # 우측상단 대응점'만' y 100 이동
# pts1 = np.float32([point_list[0],point_list[1],point_list[2]])
# pts2 = np.float32([point_list[0],point_list[1],point_list[2]])
# pts2[1][1] += 100

# # 아핀 변환 행렬 생성
# M = cv.getAffineTransform(pts1, pts2)

# # 이미지에 아빈변환 적용
# img_result = cv.warpAffine(img_color, M, (w,h))

# cv.imshow("result",img_result)
# cv.waitKey(0)
# cv.destroyAllWindows()





# # 9-5 퍼스펙티브 변환

# import numpy as np
# import cv2 as cv

# # 좌표저장할 리스트
# src = np.zeros([4,2], dtype=np.float32)
# idx = 0

# def mouse_callback(event,x,y,flags,param):
#     global point_list, idx

#     if event == cv.EVENT_LBUTTONDOWN:
#         src[idx] = (x,y)
#         idx = idx + 1
#         print("(%d, %d)" % (x,y))
#         cv.circle(img_color,(x,y),10,(0,0,255),-1)

# # 마우스 콜백함수 등록
# cv.namedWindow('original')
# cv.setMouseCallback('original',mouse_callback)

# img_color = cv.imread('resource1.jpg')
# img_original = img_color.copy()

# while(True):
#     cv.imshow("original",img_color)
#     h,w = img_color.shape[:2]

#     if cv.waitKey(1) == 32:
#         break

# # 퍼스펙티브 변환 후 사각 영역 지정
# dst = np.float32([[0,0],[w,0],[0,h],[w,h]])

# # 퍼스펙티브 변환 행렬 생성
# M = cv.getPerspectiveTransform(src,dst)

# # 이미지에 적용
# img_result = cv.warpPerspective(img_original,M,(w,h))

# cv.imshow("result1",img_result)
# cv.waitKey(0)
# cv.destroyAllWindows()








# # 10-1 블러링

# import numpy as np
# import cv2 as cv

# img = cv.imread('resource1.jpg')
# kernel = np.ones((5,5),np.float32)/25
# dst = cv.filter2D(img,-1,kernel)

# cv.imshow('Original',img)
# cv.imshow('Result',dst)

# cv.waitKey(0)
# cv.destroyAllWindows()

# ############# 평균 블러링 #############

# import cv2 as cv

# img = cv.imread('resource1.jpg')
# img_blur = cv.blur(img,(15,15))

# cv.imshow('Original',img)
# cv.imshow('Result',img_blur)

# cv.waitKey(0)
# cv.destroyAllWindows()

# ############# 가우시안 블러링 #############

# import cv2 as cv

# img = cv.imread('resource1.jpg')
# img_blur = cv.GaussianBlur(img,(5,5),0)

# cv.imshow('Original',img)
# cv.imshow('Result',img_blur)

# cv.waitKey(0)
# cv.destroyAllWindows()

# ############# 중간값 블러링 #############

# import cv2 as cv

# img = cv.imread('IMG_9419.jpg')
# img_blur = cv.medianBlur(img,5)

# cv.imshow('Original',img)
# cv.imshow('Result',img_blur)

# cv.waitKey(0)
# cv.destroyAllWindows()

# ############# 중간값 블러링 #############

# import cv2 as cv

# img = cv.imread('resource1.jpg')
# img_blur = cv.bilateralFilter(img,9,75,75)

# cv.imshow('Original',img)
# cv.imshow('Result',img_blur)

# cv.waitKey(0)
# cv.destroyAllWindows()





# 10-3 에지 검출
# ############################# 소 벨 ##############################

# import cv2

# img_color = cv2.imread ('resource1.jpg', cv2.IMREAD_COLOR)

# img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
# img_sobel_x = cv2.Sobel(img_gray, cv2.CV_64F, 1, 0, ksize=3)

# img_sobel_x = cv2.convertScaleAbs(img_sobel_x)
# img_sobel_y = cv2.Sobel(img_gray, cv2.CV_64F, 0, 1, ksize=3)

# img_sobel_y = cv2.convertScaleAbs(img_sobel_y)
# img_sobel = cv2.addWeighted(img_sobel_x, 1, img_sobel_y, 1,0);

# cv2.imshow("SobelX", img_sobel_x)
# cv2.imshow("Sobel Y", img_sobel_y)
# cv2.imshow("Sobel", img_sobel)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# ################# 캐니 에지 디텍터 #################

# import cv2
# img_gray = cv2.imread ('resource1.jpg', cv2.IMREAD_GRAYSCALE)
# cv2.imshow("Original", img_gray)

# # 블러 적용 후, 캐니 에지 디텍터 적용
# img_gray = cv2.blur(img_gray, (3, 3));

# # 첫 번째 임계값의 2~3배로 두 번째 임계값.
# img_canny = cv2.Canny(img_gray, 50, 150)
# cv2.imshow("Canny Edge", img_canny)

# cv2.waitKey(0)
# cv2.destroyAllWindows()








# # 11-1 Erosion

# import cv2
# import numpy as np

# img_gray = cv2.imread('resource1.jpg', cv2.IMREAD_GRAYSCALE)

# kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
# img_result = cv2.erode(img_gray,kernel,iterations=1)

# cv2.imshow("Input",img_gray)
# cv2.imshow("Result",img_result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()





# # 11-2 Dliation

# import cv2
# import numpy as np

# img_gray = cv2.imread('resource1.jpg', cv2.IMREAD_GRAYSCALE)

# kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
# img_result = cv2.dilate(img_gray,kernel,iterations=1)

# cv2.imshow("Input",img_gray)
# cv2.imshow("Result",img_result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()





# # 11-3 Opening

# import cv2
# import numpy as np

# img_gray = cv2.imread('resource1.jpg', cv2.IMREAD_GRAYSCALE)

# kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
# img_result = cv2.morphologyEx(img_gray,cv2.MORPH_OPEN,kernel)

# cv2.imshow("Input",img_gray)
# cv2.imshow("Result",img_result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()





# # 11-4 Closing

# import cv2
# import numpy as np

# img_gray = cv2.imread('resource1.jpg', cv2.IMREAD_GRAYSCALE)

# kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
# img_result = cv2.morphologyEx(img_gray,cv2.MORPH_CLOSE,kernel)

# cv2.imshow("Input",img_gray)
# cv2.imshow("Result",img_result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()