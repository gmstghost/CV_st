import cv2
import numpy as np
from matplotlib import pyplot as plt
import time

# src = cv2.imread('img\resource2.jpg')
# src = cv2.imread('img\resource2.jpg', cv2.IMREAD_GRAYSCALE)
src = cv2.imread('img\shape.png')
# src = cv2.imread('img\\torso1.png')

# # 3.1 직선 밎 사각형 그리기

# # 흰색 배경
# img= np.zeros(shape=(512,512,3),dtype=np.uint8)+255
# pt1 = 100,100
# pt2 = 400,400
# cv2.rectangle(img,pt1,pt2,(0,255,0),2)

# cv2.line(img,(0,0),(500,0),(255,0),2)
# cv2.line(img,(0,0),(0,500),(0,0,255),5)

# cv2.imshow('img',img)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 3.2 직선-사각형 교차점

# img = np.zeros(shape=(512,512,3),dtype=np.uint8)+255    # 배경

# x1, x2 = 10, 400
# y1, y2 = 100, 500
# cv2.rectangle(img, (x1, y1), (x2, y2), (0,0,255))       # 사각형 그리기

# pt1 = 120, 50
# pt2 = 300, 500
# cv2.line(img, pt1, pt2, (255,0,0),2)                    # 직선 그리기

# imgRect = (x1, y1, x2 - x1, y2 - y1)
# retval, rpt1, rpt2 = cv2.clipLine(imgRect, pt1, pt2)    # 접하는지 여부, 교점1, 교점2
# if retval:
#     cv2.circle(img, rpt1, radius=5, color=(0,255,0),thickness=-1)
#     cv2.circle(img, rpt2, radius=5, color=(0,255,0),thickness=-1)

# cv2.imshow('img', img)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 3.3 원 그리기

# img = np.zeros(shape=(512,512,3),dtype=np.uint8)+255
# cy = img.shape[0] // 2
# cx = img.shape[1] // 2

# for r in range(200,0,-100):
#     cv2.circle(img,(cx, cy),r,color=(255,0,0))

# cv2.circle(img,(cx,cy),radius=50,color=(0,0,255),thickness=-1)
# cv2.imshow('img',img)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 3.4 타원 그리기

# img = np.zeros(shape=(512,512,3),dtype=np.uint8)+255
# ptCenter = img.shape[1] // 2, img.shape[0] // 2
# size = 200, 100

# cv2.ellipse(img, ptCenter, size, 0, 0, 360,(255,0,0))
# cv2.ellipse(img, ptCenter, size, 45, 0, 360,(0,0,255))

# box = (ptCenter, size, 0)
# cv2.ellipse(img, box, (255,0,0), 5)

# box = (ptCenter, size, 45)
# cv2.ellipse(img, box, (0,0,255), 5)

# cv2.imshow('img',img)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 3.6 다각형 그리기 1

# img = np.zeros(shape=(512,512,3),dtype=np.uint8)+255

# pts1 = np.array([[100,100],[200,100],[200,200],[100,200]])
# pts2 = np.array([[300,200],[400,100],[400,200]])

# cv2.polylines(img,[pts1,pts2],isClosed=True,color=(255,0,0))
# cv2.imshow('img',img)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 3.7 다각형 그리기 2

# img = np.zeros(shape=(512,512,3),dtype=np.uint8)+255

# ptCenter = img.shape[1] // 2, img.shape[0] // 2
# size = 200,100

# cv2.ellipse(img,ptCenter,size,0,0,360,(255,0,0))
# pts1 = cv2.ellipse2Poly(ptCenter,size,0,0,360,delta=45)

# cv2.ellipse(img,ptCenter,size,45,0,360,(255,0,0))
# pts2 = cv2.ellipse2Poly(ptCenter,size,45,0,360,delta=45)
# cv2.polylines(img,[pts1,pts2],isClosed=True,color=(0,0,255))

# cv2.imshow('img',img)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 3.7 다각형 그리기 3: 회전 사각형

# img = np.zeros(shape=(512,512,3),dtype=np.uint8)+255

# x,y = 256,256
# size = 350

# for angle in range(0,360,1):
#     rect = ((256,256),(size,size),angle)
#     box = cv2.boxPoints(rect).astype(np.int32)
#     r = np.random.randint(256)
#     g = np.random.randint(256)
#     b = np.random.randint(256)
#     cv2.polylines(img,[box],True,(b,g,r),2)

# cv2.imshow('img',img)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 3.8 다각형 채우기 (Colorchooser 적용)

# from tkinter import colorchooser
# colorpick1 = (colorchooser.askcolor())[0]
# colorpick2 = (colorchooser.askcolor())[0]

# img = np.zeros(shape=(512,512,3),dtype=np.uint8)+255

# pts1 = np.array([[100,100],[200,100],[200,200],[100,200]])
# pts2 = np.array([[300,200],[400,100],[400,200]])

# cv2.fillConvexPoly(img,pts1,(colorpick1[2],colorpick1[1],colorpick1[0]))
# cv2.fillPoly(img,[pts2],(colorpick2[2],colorpick2[1],colorpick2[0]))

# cv2.imshow('img',img)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 3.9 문자열 출력

# img = np.zeros(shape=(512,512,3),dtype=np.uint8)+255
# text = 'OpenCV Programming'
# org = (50,100)
# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img,text,org,font,1,(255,0,0),2)

# size,baseLine = cv2.getTextSize(text,font,1,2)
# cv2.rectangle(img,org,(org[0]+size[0],org[1]-size[1]),(0,0,255))
# cv2.circle(img,org,3,(0,255,0),2)

# cv2.imshow('img',img)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 3.10 키보드 이벤트 처리

# w, h = 512, 512
# x, y, R = 256, 256, 50
# direction = 0   # right

# while True:
#     key = cv2.waitKeyEx(30)
#     if key == 0x1B:
#         break;

#     # 방향키
#     elif key == 0x270000:    # right
#         direction = 0
#     elif key == 0x280000:    # down
#         direction = 1
#     elif key == 0x250000:    # left
#         direction = 2
#     elif key == 0x260000:    # up
#         direction = 3
    
#     # 방향이동
#     if direction == 0:      # right
#         x += 10
#     elif direction == 1:    # down
#         y += 10
#     elif direction == 2:    # left
#         x -= 10
#     else:                   # up
#         y -= 10

#     # 경계 확인
#     if x < R:
#         x = R
#         direction = 0
#     if x > w - R:
#         x = w - R
#         direction = 2
#     if y < R:
#         y = R
#         direction = 1
#     if y > h - R:
#         y = h - R
#         direction = 3

# # 지우고 그리기
#     img = np.zeros((w,h,3),np.uint8)+255
#     cv2.circle(img,(x,y),R,(0,0,255),-1)
#     cv2.imshow('img',img)

# cv2.destroyAllWindows()





# # 3.11 마우스 이벤트 처리

# def onMouse(event,x,y,flags,param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         if flags & cv2.EVENT_FLAG_SHIFTKEY:
#             cv2.rectangle(param[0],(x-5, y-5),(x+5,y-5),(255,0,0))
#         else:
#             cv2.circle(param[0],(x,y),5,(0,0,255),3)
#     elif event == cv2.EVENT_LBUTTONDOWN:
#         cv2.circle(param[0],(x,y),5,(255,0,0),3)
#     elif event == cv2.EVENT_LBUTTONDBLCLK:
#         param[0] = np.zeros((512,512,3),np.uint8)+255
#     cv2.imshow("img",param[0])

# img = np.zeros((512,512,3),np.uint8)+255
# cv2.imshow('img',img)
# cv2.setMouseCallback('img',onMouse,[img])
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 3.12 트랙바 이벤트 처리

# def onChange(pos):
#     global img
#     r = cv2.getTrackbarPos('R','img')
#     g = cv2.getTrackbarPos('G','img')
#     b = cv2.getTrackbarPos('B','img')
#     img[:] = (b,g,r)
#     cv2.imshow('img',img)

# img = np.zeros((512,512,3),np.uint8)
# cv2.imshow('img',img)

# # 트랙바 정의
# cv2.createTrackbar('R', 'img',0,255,onChange)
# cv2.createTrackbar('G', 'img',0,255,onChange)
# cv2.createTrackbar('B', 'img',0,255,onChange)

# # 위치 초기화
# #cv2.setTrackbarPos('R','img',0)
# #cv2.setTrackbarPos('G','img',0)
# cv2.setTrackbarPos('B','img',255)

# cv2.waitKey()
# cv2.destroyAllWindows()







# # 4.1 영상 속성 1: 모양과 자료형

# img = cv2.imread('resoure3.jpg')   # cv2.IMREAD_COLOR와 동일

# print('img.ndim = ', img.ndim)
# print('img.shape = ', img.shape)
# print('img.dtype = ', img.dtype)

# img = img.astype(np.int32)
# print('img.dtype=',img.dtype)

# img = np.uint8(img)
# print('img.dtype=',img.dtype)





# # 4.2 영상 속성 2: 모양 변경하기
# img = cv2.imread('resoure3.jpg', cv2.IMREAD_GRAYSCALE)
# print('img.shape=',img.shape)

# img = img.flatten()             # 다차원 배열을 1차원으로
# print('img.shape=',img.shape)
# img = img.reshape(-1,813,1220)
# print('img.shape=',img.shape)

# cv2.imshow('img',img[0])        # 그레이스케일 출력
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 4.3 화소 접근 1: 그레이스케일 영상
# # 응용: roi 이미지 따로 저장해서 출력하기

# img = cv2.imread('resoure3.jpg', cv2.IMREAD_GRAYSCALE)
# roi_img = cv2.imread('resoure3.jpg', cv2.IMREAD_GRAYSCALE)
# img[100,200] = 0                # 화솟값 (밝기, 그레이스테일) 바꾸기 
# # roi_img[100,200] = 0                # 화솟값 (밝기, 그레이스테일) 바꾸기 
# print(img[100:110, 200:210])    # ROI 정의 후 접근

# # roi_img = img[100:400, 200:300].copy()
# img[100:400, 200:300] = 0       # ROI 접근

# # cv2.imshow('roi',roi_img)
# cv2.imshow('img',img)        # 그레이스케일 출력
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 4.4 화소 접근 2: 컬러 영상 (BGR)
# # 응용: 이진화 한 ROI 개별 창에 출력

# import sys

# img = cv2.imread('resoure3.jpg')
# roi_img = cv2.imread('resoure3.jpg')
# roi_img[100,200] = 0                # 화솟값 (밝기, 그레이스테일) 바꾸기 
# img[100,200] = [255,0,0]    # 빨간색으로 BGR 값 변경
# print(img[100,200:210])     # ROI에 접근

# roi_img = img[100:700, 200:500].copy()  # ROI 가져오기
# roi_img = cv2.cvtColor(roi_img, cv2.COLOR_BGR2GRAY)     # ROI부분 그레이스케일
# roi_img = cv2.adaptiveThreshold(roi_img,255,
#             cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,5,4)   # 적응형 이진화
# img[100:700, 200:500] = [255,0,0]       # ROI 부분 파란색으로

# cv2.imshow('roi',roi_img)
# cv2.imshow('img',img)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 4.5 화소 접근 3: 컬러 영상 (채널 접근)

# img = cv2.imread('resoure3.jpg')

# img[100:400, 200:300, 0] = 255      # B채널 255로
# img[100:400, 300:400, 1] = 255      # G채널 255로
# img[100:400, 400:500, 2] = 255      # R채널 255로

# cv2.imshow('img',img)
# cv2.waitKey()
# cv2.destroyAllWindows()







# # 관심 영역과 ROI
# # 4.6 ROI에 의한 블록 평균 영상

# src = cv2.imread('img\resoure3.jpg', cv2.IMREAD_GRAYSCALE)
# dst = np.zeros(src.shape, dtype=src.dtype)

# N = 64
# height,width = src.shape

# h = height // N
# w = width // N

# for i in range(N):
#     for j in range(N):
#         y = i * h
#         x = j * w
#         roi = src[y:y+h, x:x+w]
#         dst[y:y+h, x:x+w] = cv2.mean(roi)[0]

# cv2.imshow('dst', dst)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 4.7 마우스로 ROI 영역 지정

# src = cv2.imread('resource2.jpg')
# roi = cv2.selectROI(src)
# print('roi =', roi)

# if roi != (0,0,0,0):
#     img = src[roi[1]:roi[1]+roi[3], roi[0]:roi[0]+roi[2]]

#     cv2.imshow('Img',img)
#     cv2.waitKey()

# cv2.destroyAllWindows()





# # 4.8 마우스로 다중 ROI 영역 지정: cv2.selectROIs()

# src = cv2.imread('img\resource2.jpg')
# rects = cv2.selectROIs('src', src, False, True)
# print('rects = ', rects)

# for r in rects:
#     cv2.rectangle(src, (r[0],r[1]), (r[0]+r[2], r[1] + r[3]), 255)

# cv2.imshow('src',src)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 4.9 영상 복사 1

# src = cv2.imread('img\resource2.jpg')

# dst = src.copy()
# dst[100:400,200:300] = 0

# cv2.imshow('dst',dst)
# cv2.imshow('src',src)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 4.10 영상 복사 2

# src = cv2.imread('img\resource2.jpg', cv2.IMREAD_GRAYSCALE)
# shape = src.shape[0], src.shape[1], 3
# dst = np.zeros(shape, dtype=np.uint8)

# dst[:, :, 0] = src    # B채널

# dst[100:400, 200:300, :] = [255,255,255]

# cv2.imshow('src',src)
# cv2.imshow('dst',dst)
# cv2.waitKey()
# cv2.destroyAllWindows()








# # 4. 영상 채널 분리 및 병합
# # 4.11 채널 분리

# src = cv2.imread('img\rgb.jpg')
# dst = cv2.split(src)
# print(type(dst))
# print(type(dst)[0])

# cv2.imshow('source',src)
# cv2.imshow('b',dst[0])
# cv2.imshow('G',dst[1])
# cv2.imshow('R',dst[2])
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 4.12 채널 병합

# src = cv2.imread('img\resource2.jpg')
# b,g,r = cv2.split(src)

# # RGB 분리
# dst = cv2.split(src)
# cv2.imshow('b',dst[0])
# cv2.imshow('G',dst[1])
# cv2.imshow('R',dst[2])

# # 병합
# dst = cv2.merge([b,g,r])
# cv2.imshow('dst',dst)

# print(type(dst))
# print(dst.shape)
# cv2.waitKey()
# cv2.destroyAllWindows()








# # 5. 컬러 공간변환
# # 4.13 컬러 변환

# src = cv2.imread('img\resource3.jpg')

# gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
# yCrCv = cv2.cvtColor(src,cv2.COLOR_BGR2YCrCb)
# hsv = cv2.cvtColor(src,cv2.COLOR_BGR2HSV)

# cv2.imshow('gray', gray)
# cv2.imshow('yCrCv', yCrCv)
# cv2.imshow('hsv', hsv)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 6. 영상의 크기 변환과 회전
# # 4.14 영상 크기 변환

# src = cv2.imread('img\resource3.jpg')

# dst = cv2.resize(src, dsize=(320,240))
# dst2  = cv2.resize(src, dsize=(0,0), fx=1.5, fy=1.5)

# cv2.imshow('dst', dst)
# cv2.imshow('dst2', dst2)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 4.15 cv2.rotate() 영상 회전

# src = cv2.imread('img\resource3.jpg')

# dst1 = cv2.rotate(src, cv2.ROTATE_90_CLOCKWISE)
# dst2 = cv2.rotate(src, cv2.ROTATE_90_COUNTERCLOCKWISE)
# cv2.imshow('dst1', dst1)
# cv2.imshow('dst2', dst2)
# cv2.waitKey(100)
# cv2.destroyAllWindows()


# while True:
#     dst1 = cv2.rotate(dst1, cv2.ROTATE_90_COUNTERCLOCKWISE)
#     dst2 = cv2.rotate(dst2, cv2.ROTATE_90_CLOCKWISE)
#     cv2.imshow('dst1', dst1)
#     cv2.imshow('dst2', dst2)
#     cv2.waitKey(100)
#     cv2.destroyAllWindows()

#     dst1 = cv2.rotate(dst1, cv2.ROTATE_90_CLOCKWISE)
#     dst2 = cv2.rotate(dst2, cv2.ROTATE_90_COUNTERCLOCKWISE)
#     cv2.imshow('dst1', dst1)
#     cv2.imshow('dst2', dst2)
#     cv2.waitKey(100)
#     cv2.destroyAllWindows()





# # 4.16 영상 어파인 변환 (확대/축소, 회전)

# src = cv2.imread('img\resource2.jpg')

# rows, cols, channels = src.shape
# M1 = cv2.getRotationMatrix2D((rows/2,cols/2),45,0.5)
# M2 = cv2.getRotationMatrix2D((rows/2,cols/2),-45,1.0)

# dst1 = cv2.warpAffine(src, M1, (rows,cols))
# dst2 = cv2.warpAffine(src, M2, (rows,cols))

# cv2.imshow('dst1', dst1)
# cv2.imshow('dst2', dst2)
# cv2.waitKey()
# cv2.destroyAllWindows()








# # 7. 산술연산, 비트연산, 비교범위, 수치연산 함수
# # 4.17 영상 연산 1: 영상 덧셈

# src1 = cv2.imread('IMG_9109.jpg', cv2.IMREAD_GRAYSCALE)
# src2 = cv2.imread('IMG_9805_1.jpg', cv2.IMREAD_GRAYSCALE)

# dst1 = src1 + src2
# dst2 = cv2.add(src1, src2)

# cv2.imshow('dst1', dst1)
# cv2.imshow('dst2', dst2)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 4.18 영상 연산 2: 비트연산

# src1 = cv2.imread('IMG_9109.jpg')
# src2 = cv2.imread('IMG_9805_1.jpg')

# # src2 전체에 대한 src1 영역 roi에 저장
# rows, cols, channels = src2.shape
# roi = src1[0:rows,0:cols]

# gray = cv2.cvtColor(src2, cv2.COLOR_BGR2GRAY)
# ret, mask = cv2.threshold(gray,160,255,cv2.THRESH_BINARY)   # 이진 영상 mask
# mask_inv = cv2.bitwise_not(mask)        # 비트 반전 영상 mask_inv
# cv2.imshow('mask', mask)
# cv2.imshow('mask_inv', mask_inv)

# src1_bg = cv2.bitwise_and(roi, roi, mask = mask)    # 흰색영역만 src1배경 복사
# cv2.imshow('src1_bg', src1_bg)                      # 전경 검은색영역 src1_bg생성     

# # src2 전경영역을 src2_fg에 복사
# src2_fg = cv2.bitwise_and(src2, src2, mask = mask_inv)
# cv2.imshow('src2_bg', src2_fg)

# dst = cv2.bitwise_or(src1_bg, src2_fg)      # 비트 OR 연산으로 dst 생성
# cv2.imshow('dst',dst)

# src1[0:rows, 0:cols] = dst      # 결과 영상 생성

# cv2.imshow('result', src1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()





# # 4.19 반전 영상

# src1 = cv2.imread('IMG_9109.jpg', cv2.IMREAD_GRAYSCALE)
# src2 = cv2.imread('IMG_9805_1.jpg', cv2.IMREAD_GRAYSCALE)

# dst1 = 255 - src1
# dst2 = cv2.subtract(src2, src1)
# dst3 = cv2.compare(dst1, dst2, cv2.CMP_NE)
# n    = cv2.countNonZero(dst3)
# print('n = ', n)

# cv2.imshow('dst1',dst1)
# cv2.imshow('dst2',dst2)
# cv2.waitKey()
# cv2.destroyAllWindows()







# # 8. 수학 및 통계 함수
# # 4.20 cv2.normalize()에 의한 영상 정규화

# src = cv2.imread('img\resource2.jpg', cv2.IMREAD_GRAYSCALE)

# minVal, maxVal, minLoc, masLoc = cv2.minMaxLoc(src)
# print('src:',minVal, maxVal, minLoc, masLoc)

# dst = cv2.normalize(src, None,100,200,cv2.NORM_MINMAX)
# minVal, maxVal, minLoc, masLoc = cv2.minMaxLoc(dst)
# print('dst:',minVal, maxVal, minLoc, masLoc)

# cv2.imshow('dst', dst)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 4.21 cv2.ranndu()에 의한 2차원 균등분포 난수 좌표

# import time
# dst = np.full((512, 512, 3), (255,255,255), dtype=np.uint8)
# nPoints = 100
# pts = np.zeros((1, nPoints, 2), dtype=np.uint16)
# cv2.setRNGSeed(int(time.time()))    # 난수 생성 초기화
# cv2.randu(pts, (0,0),(512,512))     # 1 x nPoint, 2채널 pts배열에 균등분포난수 생성

# # 점찍기
# for k in range(nPoints):
#     x,y = pts[0,k][:]       # 채널 데이터 저장
#     cv2.circle(dst, (x,y), radius=5,color=(0,0,255),thickness=-1)

# cv2.imshow('dst', dst)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 4.22 cv2.randn()에 의한 2차원 정규분포 난수 좌표

# import time

# dst = np.full((512,512,3),(255,255,255), dtype=np.uint8)
# nPoints = 100
# pts = np.zeros((1,nPoints, 2), dtype=np.uint16)

# cv2.setRNGSeed(int(time.time()))
# cv2.randn(pts,mean=(256,256),stddev=(50,50))

# # 점찍기
# for k in range(nPoints):
#     x,y = pts[0][k,:]
#     cv2.circle(dst,(x,y),radius=5,color=(0,0,255),thickness=-1)

# cv2.imshow('dst',dst)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 4.23 cv2.Mahalanobis()에 의한 통계적 거리 계산

# X = np.array([[0,0,0,100,100,150,-100,-150],[0,50,-50,0,30,100,-20,-100]],dtype=np.float64)
# X = X.transpose()

# # cov는 2x2, mean은 열벡터
# cov, mean = cv2.calcCovarMatrix(X,mean=None,flags=cv2.COVAR_NORMAL+cv2.COVAR_ROWS)

# print('mean = ',mean)
# print('cov=',cov)

# ret, icov = cv2.invert(cov)
# print('icov=',icov)

# v1 = np.array([[0],[0]],dtype=np.float64)
# v2 = np.array([[0],[50]],dtype=np.float64)

# dst = cv2.Mahalanobis(v1,v2,icov)
# print('dst=',dst)

# cv2.waitKey()
# cv2.destroyAllWindows()





# # 4.24 통계적 거리 계산, 공분산 행렬의 고유값과 고유 벡터

# X = np.array([[0,0,0,100,100,150,-100,-150],[0,50,-50,0,30,100,-20,-100]],
#               dtype=np.float64)
# X = X.transpose()       # 각 행에 2차원 좌표 위치

# cov, mean = cv2.calcCovarMatrix(X,mean=None,flags=cv2.COVAR_NORMAL+cv2.COVAR_ROWS)
# ret, icov = cv2.invert(cov)

# dst = np.full((512,512,3),(255,255,255),dtype=np.uint8)
# rows, cols, channel = dst.shape
# centerX = cols // 2
# centerY = rows // 2

# v2 = np.zeros((1,2),dtype=np.float64)

# FLIP_Y = lambda y: rows - 1 - y

# for y in range(rows):
#     for x in range(cols):
#         v2[0,0] = x - centerX
#         v2[0,1] = FLIP_Y(y) - centerY   # y축 뒤집기
#         dist = cv2.Mahalanobis(mean, v2, icov)
#         if dist < 0.1:
#             dst[y,x] = [50,50,50]
#         elif dist < 0.3:
#             dst[y,x] = [100,100,100]
#         elif dist < 0.8:
#             dst[y,x] = [200,200,200]
#         else:
#             dst[y,x] = [250,250,250] 

# for k in range(X.shape[0]):
#     x,y = X[k,:]
#     cx = int(x+centerX)
#     cy = int(y+centerY)
#     cy = FLIP_Y(cy)
#     cv2.circle(dst,(cx,cy),radius=5,color=(0,0,255),thickness=-1)

# # X축, Y축 그리기
# cv2.line(dst,(0,256),(cols-1,256),(0,0,0))
# cv2.line(dst,(256,0),(256,rows),(0,0,0))

# # 고유 벡터 계산
# ret, eVals, eVects = cv2.eigen(cov)
# print('eVals=', eVals)
# print('eVects=', eVects)

# def ptsEigenVector(eVal, eVect):
#     scale = np.sqrt(eVal)
#     x1 = scale * eVect[0]
#     y1 = scale * eVect[1]
#     x2, y2 = -x1, -y1

#     x1 += mean[0,0] + centerX
#     y1 += mean[0,1] + centerY
#     x2 += mean[0,0] + centerX
#     y2 += mean[0,1] + centerY
#     y1 = FLIP_Y(y1)
#     y2 = FLIP_Y(y2)
#     return int(x1), int(y1), int(x2), int(y2)

# # eVects[0] 그리기
# x1, y1, x2, y2 = ptsEigenVector(eVals[0], eVects[0])
# cv2.line(dst, (x1, y1), (x2, y2), (255,0,0),2)

# # eVects[1] 그리기
# x1, y1, x2, y2 = ptsEigenVector(eVals[1], eVects[1])
# cv2.line(dst, (x1, y1), (x2, y2), (255,0,0),2)

# cv2.imshow('dst', dst)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 4.25 PCA투영, 역투영

# X = np.array([[0,0,0,100,100,150,-100,-150],[0,50,-50,0,30,100,-20,-100]],
#               dtype=np.float64)
# X = X.transpose()

# mean, eVects = cv2.PCACompute(X, mean=None)
# print('mean = ', mean)
# print('eVects = ', eVects)

# Y = cv2.PCAProject(X, mean, eVects)         # 고유벡터, 평균으로 주성분 공간으로 투영
# print('Y = , Y')

# X2 = cv2.PCABackProject(Y, mean, eVects)    # Y를 PCA 역투영하여 X 복구
# print('X2 = ', X2)
# print(np.allclose(X,X2))
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 4.26 3채널 컬러 영상의 PCA 투영

# #src = cv2.imread('img\resource2.jpg')
# src = cv2.imread('img\rgb.jpg')
# b,g,r = cv2.split(src)      # src를 b g r 에 채널 분리
# cv2.imshow('b',b)
# cv2.imshow('g',g)
# cv2.imshow('r',r)

# X = src.reshape(-1,3)       # 모양 재조정하여 X의 각 행에 화소의 컬러값 배분
# print('X.shape=', X.shape)

# mean, eVects = cv2.PCACompute(X, mean = None)   # X의 평균 백터 mean, 공분산 행렬의 고유 벡터 계산
# print('mean = ', mean)
# print('eVects = ', eVects)

# Y = cv2.PCAProject(X, mean, eVects)     # 고유 백터 eVect로 X를 Y에 PCA 투영
# Y = Y.reshape(src.shape)                # Y의 모양을 src와 동일하게 재조정
# print('Y.shape=', Y.shape)

# eImage = list(cv2.split(Y))             # Y를 eImage에 채널 분리
# for i in range(3):
#     cv2.normalize(eImage[i], eImage[i], 0, 255, cv2.NORM_MINMAX)    # 각 채널 eImgae[i] 값 정규화
#     eImage[i] = eImage[i].astype(np.uint8)      # 8비트 영상으로 변환

# cv2.imshow('eImage[0]', eImage[0])
# cv2.imshow('eImage[1]', eImage[1])
# cv2.imshow('eImage[2]', eImage[2])
# cv2.waitKey()
# cv2.destroyAllWindows()








# # 5. 임계값과 히스토그램 처리
# # 5.1 임계값 영상

# src = cv2.imread('img\resource2.jpg', cv2.IMREAD_GRAYSCALE)
# cv2.imshow('src', src)

# ret, dst = cv2.threshold(src, 120, 255, cv2.THRESH_BINARY)      # input에 맞게 임계값 적용
# print('ret=', ret)
# cv2.imshow('dst', dst)

# ret2, dst2 = cv2.threshold(src, 200, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# print('ret2=', ret2)
# cv2.imshow('dst2',dst2)

# cv2.waitKey()
# cv2.destroyAllWindows()





# # 5.2 적응형 임계값 영상
# src = cv2.imread('img\resource2.jpg', cv2.IMREAD_GRAYSCALE)
# cv2.imshow('src', src)

# ret, dst = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# cv2.imshow('dst', dst)

# dst2 = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
#                                       cv2.THRESH_BINARY, 51, 7)
# cv2.imshow('dst2',dst2)

# dst3 = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#                                       cv2.THRESH_BINARY, 51, 7)
# cv2.imshow('dst3',dst3)

# cv2.waitKey()
# cv2.destroyAllWindows()





# # 5.3 히스토그램 계산

# src  = np.array([[0,0,0,0],
#                 [1,1,3,5],
#                 [6,1,1,3],
#                 [4,3,1,7]], dtype=np.uint8)

# hist1 = cv2.calcHist(images=[src],channels=[0],mask=None,
#                      histSize=[4],ranges=[0,8])
# print('hist1=',hist1)

# hist2 = cv2.calcHist(images=[src],channels=[0],mask=None,
#                      histSize=[4],ranges=[0,4])
# print('hist2=',hist2)







# # 5.4 히스토그램 계산 2: 그레이스케일 영상
# src = cv2.imread('img\resource2.jpg', cv2.IMREAD_GRAYSCALE)

# hist1 = cv2.calcHist(images=[src],channels=[0],mask=None,
#                      histSize=[32],ranges=[0,256])
# hist2 = cv2.calcHist(images=[src],channels=[0],mask=None,
#                      histSize=[256],ranges=[0,256])

# # 1차원 행 배열로 변환
# hist1 = hist1.flatten()
# hist2 = hist2.flatten()

# plt.title('hist1: binX = np.arange(32)')
# plt.plot(hist1, color='r')                      # 꺾은선그래프
# binX = np.arange(32)

# plt.bar(binX, hist1, width=1, color='b')        # 막대그래프
# plt.show()

# plt.title('hist1: binX=np.arange(32)*8')    
# binX = np.arange(32)*8                          # 각 빈에 카운트된 값의 범위 정보
# plt.plot(binX,hist1,color='r')                  # 꺾은선그래프
# plt.bar(binX,hist1,width=8,color='b')           # 막대그래프 (너비 8)
# plt.show()

# plt.title('hist2: binX=np.arange(256)')
# plt.plot(hist2, color='r')                      # 꺾은선그래프
# binX = np.arange(256)                           # 각 빈의 인덱스
# plt.bar(binX,hist2,width=1,color='b')           # 막대그래프 (너비 1)
# plt.show()





# # 5.5 히스토그램 계산 3: 컬러 영상

# src = cv2.imread('img\resource2.jpg')
# histColor = ('b', 'g', 'r')
# for i in range(3):
#     hist = cv2.calcHist(images=[src],channels=[i],mask=None,
#                         histSize=[256],ranges=[0,256])
#     plt.plot(hist,color=histColor[i])
# plt.show()





# # 5.6 히스토그램 계산 4: 컬러 영상의 2채널 히스토그램

# bgr = cv2.imread('resource2.jpg')
# # hsv =  cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

# hist1 = cv2.calcHist([bgr],[0,1],None,[32,32],[0,256,0,256])    # 범위 256
# plt.title('hist1')
# plt.ylim(0,31)
# plt.imshow(hist1,interpolation="nearest")
# plt.show()

# hist2 = cv2.calcHist([bgr],[0,2],None,[32,32],[0,256,0,256])    # 범위 256
# plt.title('hist2')
# plt.ylim(0,31)
# plt.imshow(hist2,interpolation="nearest")
# plt.show()

# hist12 = cv2.calcHist([bgr],[1,2],None,[32,32],[0,256,0,256])    # 범위 256
# plt.title('hist12')
# plt.ylim(0,31)
# plt.imshow(hist2,interpolation="nearest")
# plt.show()





# # 5.7 영상 속성 1: 모양과 자료형

# src = np.array([[0,0,0,0],
#                 [1,1,3,5],
#                 [6,1,1,3],
#                 [4,3,1,7]], dtype=np.uint8)

# hist = cv2.calcHist(images=[src],channels=[0],mask=None,
#                     histSize=[4],ranges=[0,8])      # 0~7의 히스토그램
# print('hist=',hist)

# backP = cv2.calcBackProject([src],[0],hist,[0,8],scale=1)   # hist를 이용해 역투영 히스토그램 계산
# print('backP=',backP)





# # 5.8 Hue-채널의 히스토그램 역투영

# hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
# h,s,v = cv2.split(hsv)      # hsv 채널 분리

# roi = cv2.selectROI(src)    # roi 지정
# print('roi=',roi)
# roi_h = h[roi[1]:roi[1] + roi[3], roi[0]:roi[0] + roi[2]]
# hist = cv2.calcHist([roi_h], [0], None, [64], [0,256])      # h채널 roi에서 64빈으로 히스토그램 계산
# backP = cv2.calcBackProject([h.astype(np.float32)], [0], hist, [0,256], scale=1.0)      # hist를 역투영한 backP 계산

# hist = cv2.sort(hist, cv2.SORT_EVERY_COLUMN+cv2.SORT_DESCENDING)    # hist 각 열을 내림차순으로 정렬
# k = 1
# T = hist[k][0] - 1
# print('T = ', T)
# ret, dst = cv2.threshold(backP, T, 255, cv2.THRESH_BINARY)          # 이진 영상 계산

# cv2.imshow('dst',dst)
# cv2.waitKey()
# cv2.destroyAllWindows()








# # 5.9 cv2.compareHist(): 1차원 히스토그램 비교

# nPoints = 100000

# # 정규분포 난수 생성
# pts1 = np.zeros((nPoints, 1), dtype=np.uint16)
# pts2 = np.zeros((nPoints, 1), dtype=np.uint16)

# cv2.setRNGSeed(int(time.time()))
# cv2.randn(pts1,mean=(128),stddev=(10))
# cv2.randn(pts2,mean=(110),stddev=(20))

# H1 = cv2.calcHist(images=[pts1],channels=[0],mask=None,
#                   histSize=[256],ranges=[0,256])
# cv2.normalize(H1, H1, 1, 0, cv2.NORM_L1)
# plt.plot(H1,color='r',label='H1')

# H2 = cv2.calcHist(images=[pts2],channels=[0],mask=None,
#                   histSize=[256],ranges=[0,256])
# cv2.normalize(H2, H2, 1, 0, cv2.NORM_L1)

# # 히스토그램 H1, H2를 4가지 방법으로 계산
# d1 = cv2.compareHist(H1, H2, cv2.HISTCMP_CORREL)
# d2 = cv2.compareHist(H1, H2, cv2.HISTCMP_CHISQR)
# d3 = cv2.compareHist(H1, H2, cv2.HISTCMP_INTERSECT)
# d4 = cv2.compareHist(H1, H2, cv2.HISTCMP_BHATTACHARYYA)
# print('d1(H1, H2, CORREL)=', d1)
# print('d2(H1, H2, CHISQR)=', d2)
# print('d3(H1, H2, INTERSECT)=', d3)
# print('d4(H1, H2, BHATTACHARYYA)=', d4)

# plt.plot(H2, color='b', label='H2')
# plt.legend(loc='best')
# plt.show()





# # 5.10 cv2.EMD(): 1차원 히스토그램 비교

# nPoints = 100000

# # 정규분포 난수 생성
# pts1 = np.zeros((nPoints, 1), dtype=np.uint16)
# pts2 = np.zeros((nPoints, 1), dtype=np.uint16)

# cv2.setRNGSeed(int(time.time()))
# cv2.randn(pts1,mean=(128),stddev=(10))
# cv2.randn(pts2,mean=(110),stddev=(20))

# # pts1의 히스토그램을 H1에 계산
# H1 = cv2.calcHist(images=[pts1],channels=[0],mask=None,
#                   histSize=[256],ranges=[0,256])
# cv2.normalize(H1, H1, 1, 0, cv2.NORM_L1)
# plt.plot(H1,color='r',label='H1')

# # pts2의 히스토그램을 H2에 계산
# H2 = cv2.calcHist(images=[pts2],channels=[0],mask=None,
#                   histSize=[256],ranges=[0,256])
# cv2.normalize(H2, H2, 1, 0, cv2.NORM_L1)

# S1 = np.zeros((H1.shape[0], 2), dtype=np.float32)
# S2 = np.zeros((H1.shape[0], 2), dtype=np.float32)

# for i in range(S1.shape[0]):
#     S1[i,0] = H1[i,0]
#     S2[i,0] = H2[i,0]
#     S1[i,1] = i
#     S2[i,1] = i

# emd1, lowerbound, flow = cv2.EMD(S1, S2, cv2.DIST_L1)
# print('EMD(S1, S2, DIST_L2)')
# emd2, lowerbound, flow = cv2.EMD(S1, S2, cv2.DIST_L2)
# print('EMD(S1, S2, DIST_L2)')
# emd3, lowerbound, flow = cv2.EMD(S1, S2, cv2.C)
# print('EMD(S1, S2, DIST_C)')

# plt.plot(H1, color='r',label='H1')
# plt.plot(H2, color='b',label='H2')
# plt.legend(loc='best')
# plt.show()





# # 5.11 배열의 히스토그램 평활화

# # 배열 범위 좀음 -> 어두운영상
# src = np.array([[2,2,4,4],
#                 [2,2,4,4],
#                 [4,4,4,4],
#                 [4,4,4,4]],dtype=np.uint8)

# dst = cv2.equalizeHist(src)     # 평활화 영상은 범위 [0,255]의 밝은영상
# print('dst=',dst) 

# '''
# ref: https://docs.opencv.org/master/d5/daf/tutorial_py_histogram_equalization.html
# '''

# # 평활화 알고리즘 직접 구현
# hist, bins = np.histogram(src.flatten(),256,[0,256])
# cdf = hist.cumsum()
# cdf_m = np.ma.masked_equal(cdf,0)           # cdf에 0을 True마스킹
# T = (cdf_m - cdf_m.min())*255/(cdf_m.max - cdf_m.min())
# T = np.ma.filled(T,0).astype('uint8')       # 마스킹 0으로 채우기
# dst2 = T[src]





# # 5.12 그레이스케일 영상의 히스토그램 평할화

# dst = cv2.equalizeHist(src)
# cv2.imshow('dst',dst)
# cv2.waitKey()
# cv2.destroyAllWindows()

# plt.title('Grayscale histogram')

# hist1 = cv2.calcHist(images=[src],channels=[0],mask=None,
#                      histSize=[256],ranges=[0,256])
# plt.plot(hist1,color='b',label='hist1 in src')

# hist2 = cv2.calcHist(images=[src],channels=[0],mask=None,
#                      histSize=[256],ranges=[0,256])
# plt.plot(hist2,color='r',alpha=0.7,label='hist2 in dst')
# plt.legend(loc='best')
# plt.show()





# # 5.13 컬러 영상의 히스토그램 평활화

# cv2.imshow('src', src)

# hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
# h,s,v = cv2.split(hsv)              # 채널 분리

# v2 = cv2.equalizeHist(v)
# hsv2 = cv2.merge([h,s,v2])          # 채널 합성
# dst = cv2.cvtColor(hsv2, cv2.COLOR_HSV2BGR)
# cv2.imshow('dst',dst)

# yCrCv = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
# y, Cr, Cv = cv2.split(yCrCv)        # 채널 분리

# y2 = cv2.equalizeHist(y)
# yCrCv2 = cv2.merge([y2, Cr, Cv])    # 채널 병합
# dst2 = cv2.cvtColor(yCrCv2, cv2.COLOR_YCrCb2BGR)

# cv2.imshow('dst2',dst2)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 5.14 CLAHE 히스토그램 평활화

# src = np.array([[2,2,2,2,0,0,0,0],
#                 [2,1,1,2,0,0,0,0],
#                 [2,1,1,2,0,0,0,0],
#                 [0,0,0,0,255,255,255,255],
#                 [0,0,0,0,255,1,1,255],
#                 [0,0,0,0,255,1,1,255],
#                 [0,0,0,0,255,255,255,255]],dtype=np.uint8)

# clahe = cv2.createCLAHE(clipLimit=40,tileGridSize=(1,1))    # 객체 생성
# dst = clahe.apply(src)      # dst에 평활화, clipLimit=40*64/256=10
# print("dst=\n", dst)

# clahe2 = cv2.createCLAHE(clipLimit=40,tileGridSize=(2,2))   # 객체 생성
# dst2 = clahe2.apply(src)    # dst2에 평활화
# print("dst2=\n", dst2)





# # 5.15 CLAHE 구현

# # 패딩 없이 히스토그램 계산, 히스토그램 재분배 한 번만 수행
# src = np.array([[2,2,2,2,0,0,0,0],
#                 [2,1,1,2,0,0,0,0],
#                 [2,1,1,2,0,0,0,0],
#                 [0,0,0,0,255,255,255,255],
#                 [0,0,0,0,255,1,1,255],
#                 [0,0,0,0,255,1,1,255],
#                 [0,0,0,0,255,255,255,255]],dtype=np.uint8)

# # sub_image를 dst에 양선형 보간
# def interpolate(sub_image, UL, UR, BL, BR):
#     dst = np.zeros(sub_image.shape)
#     sY, sX = sub_image.shape
#     area = sX * sY

#     for y in range(sY):
#         invY = sY-y
#         for x in range(sX):
#             invX = sX-x
#             val = sub_image[y,x].astype(int)
#             dst[y,x] = np.floor((invY * (invX * UL[val] + x * UR[val]) +
#                                 y * (invX * BL[val] + x * BR[val])) / area)
    
#     return dst

# def CLAHE(src, cliplimit=40.0, tileX=8, tileY=8):
#     histSize = 256
#     tileSizeX = src.shape[1] // tileX
#     tileSizeY = src.shape[0] // tileY
#     tileArea = tileSizeX * tileSizeY
#     cliplimit = max(cliplimit * tileArea / histSize, 1)
#     lutScale = (histSize - 1) / tileArea
#     print("clipLimit=", cliplimit)

#     LUT = np.zeros((tileY, tileX, histSize))
#     dst = np.zeros_like(src)

# # sublocks, tiles
#     for iy in range(tileY):
#         for ix in range(tileX):
#             y = iy * tileSizeY
#             x = ix * tileSizeX
#             roi = src[y:y+tileSizeY, x:x+tileSizeX]     # title
#             tileHist, bins = np.histogram(roi, histSize, [0, 256])

#             if cliplimit > 0:   # clip histogram
#                 clipped = 0
#                 for i in range(histSize):
#                     if tileHist[i] > cliplimit:
#                         clipped += tileHist[i] - cliplimit
#                         tileHist[i] = cliplimit

#             # 평활화한 픽셀 재분배
#             redistBatch = int(clipped / histSize)
#             residual = clipped - redistBatch * histSize

#             for i in range(histSize):
#                 tileHist[i] += redistBatch
#             if residual != 0:
#                 residualStep = max(int(histSize / residual),1)
#                 for i in range(0, histSize, residualStep):
#                     if residual > 0:
#                         tileHist[i] += 1
#                         residual -= 1

# # calculate Lookup Table for equalizing
#             cdf = tileHist.cumsum()
#             tileLut = np.round(cdf*lutScale)
#             LUT[iy, ix] = tileLut
    
#     # 양선형 보강
#     y = 0
#     for i in range(tileY + 1):
#         if i == 0:
#             subY = int(tileSizeY / 2)
#             yU = yB = 0
#         elif i == tileY:
#             subY = int(tileSizeY / 2)
#             yU = yB = tileY - 1
#         else:
#             subY = tileSizeY
#             yU = i - 1
#             yB = i

#         x = 0
#         for j in range(tileX+1):
#             if j == 0:
#                 subX = tileSizeX // 2
#                 xL = xR = 0
#             elif j == tileX:
#                 subX = tileSizeX // 2
#                 xL = xR = tileX - 1
#             else:
#                 subX = tileSizeX
#                 xL = j - 1
#                 xR = j
        
#             UL = LUT[yU, xL]
#             UR = LUT[yU, xR]
#             BL = LUT[yB, xL]
#             BR = LUT[yB, xR]

#             roi = src[y:y+subY, x:x+subX]
#             dst[y:y+subY, x:x+subX] = interpolate(roi, UL, UR, BL, BR)
#             x += subX
#         y += subY
#     return dst

# dst2 = CLAHE(src, cliplimit=40.0, tileX=1, tileY=2)
# print("dst=\n", dst2)





# # 5.16 히스토그램 평활화 비교

# cv2.imshow('src',src)

# dst = cv2.equalizeHist(src)     # 영상 전체에 하나의 히스토그램 이용
# cv2.imshow('dst',dst)

# clahe2 = cv2.createCLAHE(clipLimit=40,tileGridSize=(8,8))
# dst2 = clahe2.apply(src)        # dst와 비슷함
# cv2.imshow('dst2', dst2)

# clahe3 = cv2.createCLAHE(clipLimit=40, tileGridSize=(8,8))
# dst3 = clahe3.apply(src)        # (8,8)개의 타일로 평활화
# cv2.imshow('dst3', dst3)

# cv2.waitKey()
# cv2.destroyAllWindows()








# # 6. 영상 공간 필터링
# # 6.1 박스 필터와 양방향 필터

# # 박스 필터
# dst1 = cv2.boxFilter(src, ddepth=-1, ksize=(11,11))
# dst2 = cv2.boxFilter(src, ddepth=-1, ksize=(21,21))
# # 양방향 필터
# dst3 = cv2.bilateralFilter(src, d=11, sigmaColor=10, sigmaSpace=10)
# dst4 = cv2.bilateralFilter(src, d=-1, sigmaColor=10, sigmaSpace=10)

# cv2.imshow('dst1', dst1)
# cv2.imshow('dst2', dst2)
# cv2.imshow('dst3', dst3)
# cv2.imshow('dst4', dst4)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 6.2 미디안 필터, 블러, 가우시안 필터

# dst1 = cv2.medianBlur(src, ksize=7)     # 미디안 필터
# dst2 = cv2.blur(src, ksize=(7,7))       # 블러

# # 가우시안 필터
# dst3 = cv2.GaussianBlur(src, ksize=(7,7), sigmaX=0.0)
# dst4 = cv2.GaussianBlur(src, ksize=(7,7), sigmaX=10.0)

# cv2.imshow('dst1', dst1)
# cv2.imshow('dst2', dst2)
# cv2.imshow('dst3', dst3)
# cv2.imshow('dst4', dst4)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 6.3 Sobel 필터

# # 입력 영상의 기울기를 소벨 함수로 계산
# gx = cv2.Sobel(src, cv2.CV_32F,1,0,ksize=3)
# gy = cv2.Sobel(src, cv2.CV_32F,0,1,ksize=3)

# dstX = cv2.sqrt(np.abs(gx))                 # gx의 절대값의 제곱근
# dstX = cv2.normalize(dstX, None, 0, 255,    # 최소값 0, 최대값 255로 dstX에 정규화
#                       cv2.NORM_MINMAX, dtype=cv2.CV_8U)

# dstY = cv2.sqrt(np.abs(gy))                 # gy의 절대값의 제곱근
# dstY = cv2.normalize(dstY, None, 0, 255,    # 최소값 0, 최대값 255로 dstY에 정규화
#                       cv2.NORM_MINMAX, dtype=cv2.CV_8U)

# mag = cv2.magnitude(gx, gy)     # 기울기를 mag에 계산
# minVal,maxVal,minLoc,maxLoc = cv2.minMaxLoc(mag)    # 기울기가 큰 화소가 에지
# print('mag:',minVal,maxVal,minLoc,maxLoc)
# dstM = cv2.normalize(mag, None, 0, 255,     # 최소값 0, 최대값 255로 dstM에 정규화
#                      cv2.NORM_MINMAX, dtype=cv2.CV_8U) 

# cv2.imshow('src', src)
# cv2.imshow('dstX', dstX)
# cv2.imshow('dstY', dstY)
# cv2.imshow('dstM', dstM)
# cv2.waitKey()
# cv2.destroyAllWindows()






# # 6.4 Sodel 필터 2: 에지 그래디언트 방향

# cv2.imshow('src', src)

# # 입력 영상의 기울기를 소벨 함수로 계산
# gx = cv2.Sobel(src, cv2.CV_32F,1,0,ksize=3)
# gy = cv2.Sobel(src, cv2.CV_32F,0,1,ksize=3)

# mag, angle = cv2.cartToPolar(gx, gy, angleInDegrees=True)   # 기울기 크기, 각도
# minVal,maxVal,minLoc,maxLoc = cv2.minMaxLoc(angle)    # 기울기가 큰 화소가 에지
# print('mag:',minVal,maxVal,minLoc,maxLoc)

# ret, edge = cv2.threshold(mag, 100, 255, cv2.THRESH_BINARY)     # 임계삾 100으로 이진 영상 edge 계산
# edge = edge.astype(np.uint8)        # 화소 자료형 변경
# cv2.imshow('edge', edge)

# h, w = mag.shape[:2]
# angleM = np.full((h,w,3),(255,255,255), dtype=np.uint8)     # 배경 흰색 3채널컬러영상
# for y in range(h):
#     for x in range(w):
#         if edge[y,x] != 0:
#             # 기울기 각도별로 색 저장
#             if edge[y,x] == 0:
#                 angleM[y,x] = (0,0,255)         # R
#             elif edge[y,x] == 90:
#                 angleM[y,x] = (0,255,0)         # G
#             elif edge[y,x] == 180:
#                 angleM[y,x] = (255,0,0)         # B
#             elif edge[y,x] == 270:
#                 angleM[y,x] = (0,255,255)       # Y
#             else:
#                 angleM[y,x] = (128,128,128)     # gray
# cv2.imshow('angleM', angleM)

# hist = cv2.calcHist(images=[angle],channels=[0],mask=edge,      # angel 히스토그램
#                     histSize=[360],ranges=[0,360])
# hist = hist.flatten()
# plt.plot(hist, color = 'r')
# binX = np.arange(360)
# plt.bar(binX, hist, width=1, color='b')
# plt.show()





# # 6.5 Laplacian 필터

# blur = cv2.GaussianBlur(src, ksize=(7,7), sigmaX=0.0)
# cv2.imshow('src', src)
# cv2.imshow('blur', blur)

# lap = cv2.Laplacian(src,cv2.CV_32F)
# minVal, maxVal, minLoc, masLoc = cv2.minMaxLoc(lap)
# print('src:',minVal, maxVal, minLoc, masLoc)
# dst = cv2.convertScaleAbs(lap)
# dst = cv2.normalize(dst,None,0,255,cv2.NORM_MINMAX)
# cv2.imshow('lsp', lap)
# cv2.imshow('dst', dst)

# lap2 = cv2.Laplacian(blur,cv2.CV_32F)
# minVal, maxVal, minLoc, masLoc = cv2.minMaxLoc(lap2)
# print('src:',minVal, maxVal, minLoc, masLoc)
# dst2 = cv2.convertScaleAbs(lap2)
# dst2 = cv2.normalize(dst2,None,0,255,cv2.NORM_MINMAX)
# cv2.imshow('lsp2', lap2)
# cv2.imshow('dst2', dst2)

# cv2.waitKey()
# cv2.destroyAllWindows()





# # 6.6 Laplacian 필터 2: 0-교차

# blur = cv2.GaussianBlur(src, ksize=(7,7), sigmaX=0.0)
# lap = cv2.Laplacian(blur,cv2.CV_32F,3)

# def SGN(x):
#     if x >= 0:
#         sign = 1
#     else:
#         sign = -1
#     return sign

# def zeroCrossing(lap):
#     h, w = lap.shape
#     Z = np.zeros(lap.shape,dtype=np.uint8)
#     for y in range(1, h-1):
#         for x in range(1, w-1):
#             neighbors=[lap[y-1,x], lap[y+1,x],
#                         lap[y,x-1], lap[y,x+1],
#                         lap[y-1,x-1],lap[y-1,x+1],
#                         lap[y+1,x-1], lap[y+1,x+1]]
#             mValue = min(neighbors)
#             if SGN(lap[y,x]) != SGN(mValue):
#                 Z[y,x] = 255
#     return Z
# edgeZ = zeroCrossing(lap)
# cv2.imshow('Zero crossing', edgeZ)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 6.7 cv2.filter2D()와 cv2.sepFilter2D()에 의한 에지 검출

# kx, ky = cv2.getDerivKernels(1,0,ksize=3)
# sobelX = ky.dot(kx.T)
# print('kx=', kx)
# print('ky=', ky)
# print('sobelX=', sobelX)
# gx = cv2.filter2D(src, cv2.CV_32F, sobelX)

# kx, ky = cv2.getDerivKernels(0,1,ksize=3)
# sobelY = ky.dot(ky.T)
# print('kx=', kx)
# print('ky=', ky)
# print('sobelY=', sobelY)
# gy = cv2.filter2D(src, cv2.CV_32F, sobelY)

# mag = cv2.magnitude(gx, gy)
# ret, edge = cv2.threshold(mag, 100, 255, cv2.THRESH_BINARY)

# cv2.imshow('edge', edge)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 6.8 LoG 필터링, 0-교차 에지 영상

# def logFilter(ksize=7):
#     k2 = ksize // 2
#     sigma = 0.3*(k2-1)+0.8
#     print('sigma',sigma)
#     LoG = np.zeros((ksize, ksize), dtype=np.float32)
#     for y in range(-k2, k2+1):
#         for x in range(-k2,k2+1):
#             g = -(x*x+y*y)/(2.0*sigma**2.0)
#             LoG[y+k2, x+k2] = -(1.0+g)*np.exp(g)/(np.pi*sigma**4.0)
#     return LoG

# kernel = logFilter()
# LoG = cv2.filter2D(src, cv2.CV_32F, kernel)
# cv2.imshow('LoG', LoG)

# def zeroCrossing2(lap, thresh=0.01):
#     h, w = lap.shape
#     Z = np.zeros(lap.shape, dtype=np.uint8)
#     for y in range(1, h-1):
#         for x in range(1, w-1):
#             neighbors=[lap[y-1,x], lap[y+1,x],
#                         lap[y,x-1], lap[y,x+1],
#                         lap[y-1,x-1],lap[y-1,x+1],
#                         lap[y+1,x-1], lap[y+1,x+1]]
#             pos = 0
#             neg = 0
#             for value in neighbors:
#                 if value > -thresh:
#                     pos += 1
#                 if value < -thresh:
#                     neg += 1
#             if pos >0 and neg > 0:
#                 Z[y,x] = 255
#     return Z

# edgeZ = zeroCrossing2(LoG)
# cv2.imshow('Zero Crossing2', edgeZ)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 6.9 erode()와 dilate() 모폴로지 연산 1

# kernel = cv2.getStructuringElement(shape=cv2.MORPH_RECT, ksize=(3,3))
# erode = cv2.erode(src,kernel,iterations=5)
# dilate = cv2.dilate(src,kernel,iterations=5)
# erode2 = cv2.erode(src,kernel,iterations=7)
# cv2.imshow('src',src)
# cv2.imshow('erode',erode)
# cv2.imshow('dilate',dilate)
# cv2.imshow('erode2',erode2)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 6.10 morphologyEx() 모폴로지 연산

# kernel = cv2.getStructuringElement(shape=cv2.MORPH_RECT,ksize=(3,3))
# closing = cv2.morphologyEx(src, cv2.MORPH_CLOSE, kernel, iterations=5)
# opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel, iterations=5)
# gradient = cv2.morphologyEx(opening, cv2.MORPH_GRADIENT, kernel)
# tophat = cv2.morphologyEx(src, cv2.MORPH_TOPHAT, kernel, iterations=5)
# balckhat = cv2.morphologyEx(src, cv2.MORPH_BLACKHAT, kernel, iterations=5)

# cv2.imshow('opening',opening)
# cv2.imshow('closing',closing)
# cv2.imshow('gradient',gradient)
# cv2.imshow('tophat',tophat)
# cv2.imshow('balckhat',balckhat)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 6.11 모폴로지 연산 골격화

# ret, A = cv2.threshold(src, 128, 255, cv2.THRESH_BINARY)
# skel_dst = np.zeros(src.shape, np.uint8)
# B = cv2.getStructuringElement(shape=cv2.MORPH_RECT, ksize=(3,3))
# done = True
# while done:
#     erode = cv2.erode(A, B)
#     opening = cv2.morphologyEx(erode, cv2.MORPH_OPEN, B)
#     tmp = cv2.subtract(erode, opening)
#     skel_dst = cv2.bitwise_or(skel_dst, tmp)
#     A = erode.copy()
#     done = cv2.countNonZero(A) != 0

# cv2.imshow('src', src)
# cv2.imshow('skel_dst', skel_dst)
# cv2.waitKey()
# cv2.destroyAllWindows()





# 6.12 cv2.matchTemplate() 템플릿 매칭








# # 7. 영상 분할
# # 7.1 에지 검출: cv2.Canny()

# edges1 = cv2.Canny(src, 50, 100)
# edges2 = cv2.Canny(src, 50, 200)

# cv2.imshow('edges1', edges1)
# cv2.imshow('edges2', edges2)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 7.2 직선 김출: cv2.HoughLines()

# gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# edges = cv2.Canny(gray, 50, 100)
# lines = cv2.HoughLines(edges, rho=1, theta=np.pi/180.0, threshold=89)
# print('lines.shape', lines.shape)

# for line in lines:
#     rho, theta = line[0]
#     c = np.cos(theta)
#     s = np.sin(theta)
#     x0 = c * rho
#     y0 = s * rho
#     x1 = int(x0 + 1000 * (-s))
#     y1 = int(y0 + 1000 * (c))
#     x2 = int(x0 - 1000 * (-s))
#     y2 = int(y0 - 1000 * (c))
#     cv2.line(src, (x1, y1), (x2, y2), (0,0,255),2)

# cv2.imshow('edges', edges)
# cv2.imshow('src', src)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 7.4 원 검출: cv2.HoughCircles()

# src1 = cv2.imread('circle1.png')
# gray1 = cv2.cvtColor(src1,cv2.COLOR_BGR2GRAY)
# circles1 = cv2.HoughCircles(gray1, method=cv2.HOUGH_GRADIENT, 
#                            dp=1, minDist=50, param2=15)

# circles1 = np.int32(circles1)
# print('circles.shape=', circles1.shape)
# for circle in circles1[0,:]:
#     cx, cy, r = circle
#     cv2.circle(src1, (cx, cy), r, (0,0,255), 2)
# cv2.imshow('src1', src1)

# src2 = cv2.imread('circle2.png')
# gray2 = cv2.cvtColor(src2, cv2.COLOR_BGR2GRAY)
# circles2 = cv2.HoughCircles(gray2, method = cv2.HOUGH_GRADIENT,
#                             dp=1, minDist=50, param2=15,
#                             minRadius=30, maxRadius=100)

# circles2 = np.int32(circles2)
# print('circles2.shape=', circles2.shape)
# for circle in circles2[0,:]:
#     cx, cy, r = circle
#     cv2.circle(src2, (cx, cy), r, (0,0,255), 2)

# cv2.imshow('src2', src2)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 7.5 컬러 영역 검출: cv2.inRange()

# src1 = cv2.imread('resource2.jpg')
# hsv1 = cv2.cvtColor(src1, cv2.COLOR_BGR2HSV)
# lowerb1 = (0,0,0)           # HSV 최소  
# upperb1 = (179,255,255)     # HSV 최대
# dst1 = cv2.inRange(hsv1, lowerb1, upperb1)

# src2 = cv2.imread('shape.png')
# hsv2 = cv2.cvtColor(src2, cv2.COLOR_BGR2HSV)
# lowerb2 = (0,0,0)           # HSV 최소  
# upperb2 = (180,255,255)     # HSV 최대
# dst2 = cv2.inRange(hsv2, lowerb2, upperb2)

# cv2.imshow('src1',src1)
# cv2.imshow('dst1',dst1)
# cv2.imshow('src2',src2)
# cv2.imshow('dst2',dst2)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 7.6 운곽선 검출 및 그리기 1: mode = cv2.RETR_EXTERNAL

# src = np.zeros(shape=(512,512,3),dtype=np.uint8)
# cv2.rectangle(src, (50,100), (450,400), (255,255,255),-1)
# cv2.rectangle(src, (100,150), (400,350), (0,0,0), -1)
# cv2.rectangle(src, (200,200), (300,300), (255,255,255),-1)
# gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# mode = cv2.RETR_EXTERNAL
# method = cv2.CHAIN_APPROX_SIMPLE
# contours, hierarchy = cv2.findContours(gray, mode, method)
# print('type(contours)=', type(contours))
# print('type(contours)[0]=', type(contours[0]))
# print('len(contours)=', len(contours))
# print('contours[0].shape=', type(contours[0].shape))
# print('contours[0]=', contours[0])
# cv2.drawContours(src, contours, -1, (255,0,0),3)    # 모든 윤곽선

# for pt in contours[0][:]:
#     cv2.circle(src, (pt[0][0], pt[0][1]),5,(0,0,255),-1)

# cv2.imshow('src',src)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 7.7 윤곽선 검출 및 그리기 2: mode = cv2. RETR LIST

# src = np.zeros(shape=(512,512,3),dtype=np.uint8)
# cv2.rectangle(src, (50,100), (450,400), (255,255,255),-1)
# cv2.rectangle(src, (100,150), (400,350), (0,0,0), -1)
# cv2.rectangle(src, (200,200), (300,300), (255,255,255),-1)
# gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# mode = cv2.RETR_LIST
# method = cv2.CHAIN_APPROX_SIMPLE
# contours, hierarchy = cv2.findContours(gray, mode, method)

# print('len(contours)=', len(contours))
# print('contours[0].shape=', type(contours[0].shape))
# print('contours=', contours)

# for cnt in contours:
#     cv2.drawContours(src, [cnt], 0, (255,0,0),3)

#     for pt in cnt:
#         cv2.circle(src, (pt[0][0], pt[0][1]), 5, (0,0,255),-1)
        
# cv2.imshow('src',src)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 7.8 cv2.floodFill() 영역 채우기

# src = np.zeros(shape=(512,512,3),dtype=np.uint8)
# cv2.rectangle(src, (50,50), (200,200), (0,0,255),2)
# cv2.circle(src,(300,300),100,(0,0,255),2)

# dst = src.copy()
# cv2.floodFill(dst, mask=None, seedPoint=(100,100), newVal=(255,0,0))

# retval, dst2, mask, rect = cv2.floodFill(dst, mask=None,seedPoint=(300,300),
#                                          newVal=(0,255,0))

# print('rect',rect)
# x,y,w,h = rect
# cv2.rectangle(dst2,(x,y),(x+w, y+h),(255,0,0),2)

# cv2.imshow('src',src)
# cv2.imshow('dst',dst)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 7.9 cv2.distanceTreansform() 거리 계산

# src = np.zeros(shape=(512,512),dtype=np.uint8)
# cv2.rectangle(src, (50,200),(450,300),(255,255,255),-1)

# # dist에 거리 계산
# dist = cv2.distanceTransform(src, distanceType=cv2.DIST_L1,maskSize=3)
# minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(dist)    # 최대값
# print('src:', minVal, maxVal, minLoc, maxLoc)

# # [0,255] 범위로 정규화
# dst = cv2.normalize(dist, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
# # dst2에 임계값 적용
# ret, dst2 = cv2.threshold(dist, maxVal-1, 255, cv2.THRESH_BINARY)

# # 그래디언트 계산
# gx = cv2.Sobel(dist, cv2.CV_32F, 1, 0, ksize=3)
# gy = cv2.Sobel(dist, cv2.CV_32F, 0, 1, ksize=3)
# mag = cv2.magnitude(gx, gy)     # 크기 mag 생성
# minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(mag)
# print('src:', minVal, maxVal, minLoc, maxLoc)
# ret, dst3 = cv2.threshold(mag, maxVal-2, 255, cv2.THRESH_BINARY_INV)    # 임계값 적용

# cv2.imshow('src', src)
# cv2.imshow('dst', dst)
# cv2.imshow('dst2', dst2)
# cv2.imshow('dst3', dst3)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 7.10 cv2.watershed() 영상 분할

# mask = np.zeros(shape = src.shape[:2], dtype=np.uint8)
# markers = np.zeros(shape = src.shape[:2], dtype=np.int32)
# dst = src.copy()
# cv2.imshow('dst', dst)

# def onMouse(event, x, y, flags, param):
#     if event == cv2.EVENT_MOUSEMOVE:
#         if flags & cv2.EVENT_FLAG_LBUTTON:
#             cv2.circle(param[0],(x,y),5,(255,255,255),-1)
#             cv2.circle(param[1],(x,y),5,(255,255,255),-1)
#     cv2.imshow('dst',param[1])

# mode = cv2.RETR_EXTERNAL
# method = cv2.CHAIN_APPROX_SIMPLE
# while True:
#     cv2.setMouseCallback('dst', onMouse, [mask, dst])
#     key = cv2.waitKey(30)

#     if key == 0x1B:
#         break;
#     elif key == ord('r'):
#         mask[:,:] = 0
#         dst = src.copy()
#         cv2.imshow('dst',dst)
#     elif key == ord(' '):
#         contours, hierarchy = cv2.findContours(mask,mode,method)
#         print('len(contours)=', len(contours))
#         markers[:,:] = 0
#         for i, cnt in enumerate(contours):
#             cv2.drawContours(markers, [cnt], 0, i+1), -1
#         cv2.watershed(src, markers)

#         dst = src.copy()
#         dst[markers == -1] = [0,0,255]
#         for i in range(len(contours)):
#             r = np.random.randint(256)
#             g = np.random.randint(256)
#             b = np.random.randint(256)
#             dst[markers==i+1] = [b,g,r]

#         dst = cv2.addWeighted(src,0.4,dst,0.6,0)
#         cv2.imshow('dst',dst)

# cv2.destroyAllWindows()





# # 7.11 cv2.distanceTransform(), cv2.watershed() 영상 분할

# gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# ret,bImage = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
# dist = cv2.distanceTransform(bImage, cv2.DIST_L1, 3)
# # 8비트 영상 변환
# dist8 = cv2.normalize(dist, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
# cv2.imshow('bImage', bImage)
# cv2.imshow('dist8',dist8)

# minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(dist)
# print('dist:', minVal, maxVal, minLoc, maxLoc)
# mask = (dist > maxVal * 0.5).astype(np.uint8)*255   # 최대값으로 8비트 마스크 계산
# cv2.imshow('mask',mask)

# mode = cv2.RETR_EXTERNAL
# method = cv2.CHAIN_APPROX_SIMPLE
# contours, hierarchy = cv2.findContours(mask, mode, method)  # mask에서 윤곽선검출
# print('len(contours)', len(contours))

# markers = np.zeros(shape=src.shape[:2], dtype=np.int32)
# for i, cnt in enumerate(contours):
#     cv2.drawContours(markers, [cnt], 0, i+1, -1)    # 마커 생성

# dst = src.copy()
# cv2.watershed(src, markers)

# dst[markers == -1] = [0,0,255]      # 빨간색 경계선
# for i in range(len(contours)):      # 분할 영역에 임의의 색 지정
#     r = np.random.randint(256)
#     g = np.random.randint(256)
#     b = np.random.randint(256)
#     dst[markers==i+1] = [b,g,r]
# dst = cv2.addWeighted(src,0.4,dst,0.6,0)    # src*0.4 + dst*0.6 혼합해서 dst

# cv2.imshow('dst',dst)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 7.12 cv2.pyrDown(), cv2.pyrUp() 피라미드 영상

# down2 = cv2.pyrDown(src)
# down4 = cv2.pyrUp(down2)
# print('down2.shape=',down2.shape)
# print('down4.shape=',down4.shape)

# up2 = cv2.pyrUp(src)
# up4 = cv2.pyrUp(up2)
# print('up2.shape=',up2.shape)
# print('up4.shape=',up4.shape)

# cv2.imshow('down2',down2)
# cv2.imshow('up2',up2)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 7.13 cv2.pyrMeanShiftFiltering
# def floodFliSoptProcess(src, diff=(2,2,2)):
#     img = src.copy()
#     rows, cols = img.shape[:2]
#     mask = np.zeros(shape=(rows+2,cols+2),dtype=np.uint8)
#     for y in range(rows):
#         for x in range(cols):
#             if mask[y+1,x+1] == 0:
#                 r = np.random.randint(256)
#                 g = np.random.randint(256)
#                 b = np.random.randint(256)
#                 cv2.floodFill(img, mask, (x,y), (b,g,r), diff, diff)
#     return img

# hsv = cv2.cvtColor(src, cv2.COLOR_RGB2HSV)
# dst = floodFliSoptProcess(src)
# dst2 = floodFliSoptProcess(dst)
# cv2.imshow('src',src)
# cv2.imshow('hsv',hsv)
# cv2.imshow('dst',dst)
# cv2.imshow('dst2',dst2)

# res = cv2.pyrMeanShiftFiltering(src, sp=5,sr=20,maxLevel=4)
# dst3 = floodFliSoptProcess(res)

# term_crit = (cv2.TERM_CRITERIA_EPS+cv2.TermCriteria_MAX_ITER,10,2)
# res2 = cv2.pyrMeanShiftFiltering(hsv,sp=5,sr=20,maxLevel=4,termcrit=term_crit)
# dst4 = floodFliSoptProcess(res2)

# cv2.imshow('res',res)
# cv2.imshow('res2',res2)
# cv2.imshow('dst3',dst3)
# cv2.imshow('dst4',dst4)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 7.14 cv2.kmeans() 컬러 클러스터링 영역 검출

# hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
# data = src.reshape((-1,3)).astype(np.float32)

# K = 2
# term_crit = (cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,10,1.0)
# ret, labels, centers = cv2.kmeans(data,K,None,term_crit,
#                                   5,cv2.KMEANS_RANDOM_CENTERS)
# print('centers.shape=',centers.shape)
# print('labels.shape=',labels.shape)
# print('ret=',ret)

# centers = np.uint8(centers)
# res = centers[labels.flatten()]
# dst = res.reshape(src.shape)

# cv2.imshow('dst',dst)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 7.15 레이블링 1(임계값 이진 영상)

# gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# # 임게값 128 이진화
# ret, res = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)

# ret, labels = cv2.connectedComponents(res)  # 이진 영상 레이블링
# print('ret=', ret)

# dst = np.zeros(src.shape,dtype=src.dtype)
# for i in range(1,ret):      # 레이블링 한 영역별로 색상 다르게 표시 (배경제외)
#     r = np.random.randint(256)
#     g = np.random.randint(256)
#     b = np.random.randint(256)
#     dst[labels == i+1] = [b,g,r]

# cv2.imshow('res',res)
# cv2.imshow('dst',dst)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 7.16 cv2.connectedCompentsWithStats() 레이블링

# gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
# ret, res = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)

# # 레이블링 후 레이블 개수, 정보, 통계정보, 중심점 계산
# ret, labels, stats, centroids = cv2.connectedComponentsWithStats(res)

# print('ret=', ret)
# print('stats=', stats)
# print('centroids=', centroids)

# dst = np.zeros(src.shape, dtype=src.dtype)
# for i in range(1, int(ret)):    # 배경 제외한 레이블영역 난수로 채우기
#     r = np.random.randint(256)
#     g = np.random.randint(256)
#     b = np.random.randint(256)
#     dst[labels==i] = [b,g,r]

# for i in range(1, int(ret)):
#     x, y, width, height, area = stats[i]    # 레이블 i의 통계정보
#     cv2.rectangle(dst, (x,y), (x+width, y+height), (0,0,255),2)     # 바운딩사각형 생성

#     cx, cy = centroids[i]   # 중심점
#     cv2.circle(dst, (int(cx), int(cy)), 5, (255,0,0),-1)    # 중심점표시

# cv2.imshow('src', src)
# cv2.imshow('res', res)
# cv2.imshow('dst', dst)
# cv2.waitKey()
# cv2.destroyAllWindows()









# # 8. 영상 특징 검출
# # 8.1 cv2.preCornerDetect() 코너점 검출

# def findLocalMaxima(src):
#     kernel = cv2.getStructuringElement(shape=cv2.MORPH_RECT,ksize=(15,15))
#     dilate = cv2.dilate(src,kernel)     # 각 픽셀을 주변 15×15 영역의 최댓값으로 적용
#     localMax = (src == dilate)          # 해당 픽셀이 주변에서 가장 큰 경우 True

#     erode = cv2.erode(src,kernel)       # 각 픽셀을 주변 15×15 영역의 최솟값으로
#     localMax2 = src > erode             # 최댓값 찾기
#     localMax &= localMax2               # 모두 만족하는 결과 지정
#     points = np.argwhere(localMax == True)      # 좌표 형태 변환
#     points[:,[0,1]] = points[:,[1,0]]   # 열 교환
#     return points

# gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# res = cv2.preCornerDetect(gray, ksize=3)     # 코너 검출 전처리
# ret, res2 = cv2.threshold(np.abs(res),0.1,0,cv2.THRESH_TOZERO)  # res에서 임계값보다 작은 값의 픽셀 삭제
# corners = findLocalMaxima(res2)         # 적용된 이미지에 함수 적용
# print('corners.shape=',corners.shape)   # 코너점 개수

# dst = src.copy()
# for x,y in corners:     # 원으로 코너점 표시
#     cv2.circle(dst, (x,y),5,(0,0,255),2)

# cv2.imshow('dst',dst)
# cv2.waitKey()
# cv2.destroyAllWindows()

# # 이미지 픽셀의 밝기/대비에 따라 임계값 달라짐
# # 응답값 정규화 필요 있음
# # 노란 사각형:  엣지 픽셀값 차이 ≈ 230 - 200 = ~30   (노랑 ↔ 흰색)
# # 검은 사각형:  엣지 픽셀값 차이 ≈ 255 - 0   = 255   (흰색 ↔ 검정)






# # 8.2 코너점 검출: cornerEigenValsAndVecs()

# gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# res = cv2.cornerEigenValsAndVecs(gray, blockSize=5, ksize=3)
# print('res.shape', res.shape)
# eigen = cv2.split(res)

# T = 0.2
# ret, edge = cv2.threshold(eigen[0],T,255,cv2.THRESH_BINARY)
# edge = edge.astype(np.uint8)

# corners = np.argwhere(eigen[1]>T)
# corners[:,[0,1]] = corners[:,[1,0]]
# print('len(corners)=', len(corners))

# dst = src.copy()
# for x,y in corners:
#     cv2.circle(dst, (x,y), 5, (0,0,255),2)

# cv2.imshow('edge',edge)
# cv2.imshow('dst',dst)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 8.3 코너점 검출 1: cv2.conerMinigernVal()

# gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# eigen = cv2.cornerMinEigenVal(gray, blockSize=5)    # 행렬로부터 계산한 최소 고유값 저장
# print('eigen.shape=', eigen.shape)

# T = 0.2
# corners = np.argwhere(eigen > T)        # 조건 해당 좌표를 코너점 배열에 검출
# corners[:,[0,1]] = corners[:,[1,0]]     # 좌표순서 열,행으로 변환
# print('len(corners)=',len(corners))
# dst = src.copy()
# for x,y in corners:
#     cv2.circle(dst,(x,y),3,(0,0,255),2)

# cv2.imshow('dst',dst)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 8.4 코너점 검출 2: cv2.cornerHarris(), cv2.cornerSubPix()

# def findLocalMaxima(src):
#     kernel = cv2.getStructuringElement(shape=cv2.MORPH_RECT,ksize=(11,11))
#     dilate = cv2.dilate(src,kernel)     # local max if kernel=None, 3x3
#     localMax = (src == dilate)

#     erode = cv2.erode(src,kernel)       # local min if kernel=None, 3x3
#     localMax2 = src > erode
#     localMax &= localMax2
#     points = np.argwhere(localMax == True)
#     points[:,[0,1]] = points[:,[1,0]]   # x,y 스위치
#     return points

# gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# res = cv2.cornerHarris(gray,blockSize=5,ksize=3,k=0.01)         # 공분산행렬의 Harris값
# ret, res = cv2.threshold(np.abs(res),0.02,0,cv2.THRESH_TOZERO)  # 절대값에서 이진화적용
# res8 = cv2.normalize(res,None,0,255,cv2.NORM_MINMAX,dtype=cv2.CV_8U)    # [0,255]범위 정규화
# cv2.imshow('res8',res8)

# corners = findLocalMaxima(res)      # res에서 코너점 탐색 (정수좌표)
# print('corners=', corners)

# corners = corners.astype(np.float32, order='C')     # np.float32 자료형 변환
# term_crit = (cv2.TERM_CRITERIA_MAX_ITER+cv2.TERM_CRITERIA_EPS,10,0.01)
# corners2 = cv2.cornerSubPix(gray,corners,(5,5),(-1,-1),term_crit)   # 부화소 수준으로 코너점 계산
# print('corners2=', corners2)

# dst = src.copy()
# for x,y in np.int32(corners2):
#     cv2.circle(dst,(x,y),3,(0,0,255),2)
# cv2.imshow('dst',dst)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 8.5 코너점 검출 2: cv2.cornerHarris(), cv2.cornerSubPix()

# gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# res = cv2.cornerHarris(gray,blockSize=5,ksize=3,k=0.01)     # 공분산행렬의 Harris값

# res = cv2.dilate(res, None)     # 팽창연산, 3x3 직사각형 kernel
# ret, res = cv2.threshold(res,0.01*res.max(),255,cv2.THRESH_BINARY)  # 이진화
# res8 = np.uint8(res)            # 반응값의 자료형 변환
# cv2.imshow('res8',res8)

# ret, labels, stats, centroids = cv2.connectedComponentsWithStats(res8)      # 이진영상 레이블링
# print('centroids.shape=',centroids.shape)
# print('centroids=',centroids)
# centroids = np.float32(centroids)       # centroids 자료형 변환

# term_crit = (cv2.TERM_CRITERIA_MAX_ITER+cv2.TERM_CRITERIA_EPS,10,0.001)     # 종료조건 설정(10회반복,조기종료 임계값 0.001)
# corners = cv2.cornerSubPix(gray,centroids,(5,5),(-1,-1),term_crit)      # centroids 부화소 수준 계산
# print('corners=',corners)

# corners = np.round(corners)     # 반올림
# dst = src.copy()
# for x,y in corners[1:]:     # 코너점 위치 지정
#     cv2.circle(dst,(int(x),int(y)),5,(0,0,255),2)

# cv2.imshow('dst',dst)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 8.7 체스보드 패턴 코너점 검출: cv2.findChessboradCorners()

# src = cv2.imread('img\chess.png')
# gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# patternSize = (14,14)       # 체스보드 패턴 내부 코너점
# found, corners = cv2.findChessboardCorners(src,patternSize)     # 14x14 코너점 검출
# print('corners.shape=',corners.shape)

# term_crit = (cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,10,0.01)  # 종료조건 설정(10회반복,조기종료 임계값 0.001)
# corners2 =cv2.cornerSubPix(gray,corners,(5,5),(-1,-1),term_crit)    # centroids 부화소 수준 계산

# dst = src.copy()
# cv2.drawChessboardCorners(dst,patternSize,corners2,found)   # 체스보드 코너점 그리기

# cv2.imshow('dst',dst)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 8.8 원 패턴 중심점 검출

# src = cv2.imread('img\circle_pat.png')
# gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# patternSize = (11,7)       # 원 개수
# found, centers = cv2.findCirclesGrid(src, patternSize)  # 원 종심 centers에 검출
# print('centers.shape=', centers.shape)

# term_crit = (cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,10,0.01)  # 종료조건 설정(10회반복,조기종료 임계값 0.001)
# centers2 = cv2.cornerSubPix(gray,centers,(5,5),(-1,-1),term_crit)    # centroids 부화소 수준 계산

# dst = src.copy()
# cv2.drawChessboardCorners(dst,patternSize,centers2,found)   # 검출된 centers2 표시

# cv2.imshow('dst',dst)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 8.9 영상 모멘트: cv2.moments()

# gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)     # 그레이스케일
# ret, bImage = cv2.threshold(gray,128,255,cv2.THRESH_BINARY)     # 이진 영상

# M = cv2.moments(bImage, True)       # 영상 모멘트 계산
# for key, value in M.items():        # 모멘트 출력
#     print('{}={}'.format(key,value))

# cx = int(M['m10']/M['m00'])         # 중심 x좌표
# cy = int(M['m01']/M['m00'])         # 중심 y좌표
# dst = src.copy()
# cv2.circle(dst,(cx,cy),5,(0,0,255),2)

# cv2.imshow('dst',dst)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 8.10 cv2.monents() 경계선 모멘트

# gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)     # 그레이스케일
# ret, bImage = cv2.threshold(gray,128,255,cv2.THRESH_BINARY_INV)     # 반전 이진 영상

# mode = cv2.RETR_EXTERNAL    # 가장 바깥쪽 contour만
# method = cv2.CHAIN_APPROX_SIMPLE    # 윤곽점 끝점만
# contours, hierarchy = cv2.findContours(bImage,mode,method)  # 윤곽선 검출

# dst = src.copy()
# cv2.drawContours(dst,contours,-1,(0,0,0),3)   # 모든 윤곽선

# for cnt in contours:
#     M = cv2.moments(cnt, True)          # 윤곽선 cnt moment를 M에 계산
#     cx = int(M['m10']/M['m00'])         # 중심 x좌표
#     cy = int(M['m01']/M['m00'])         # 중심 y좌표
#     cv2.circle(dst,(cx,cy),5,(0,0,255),2)   # 좌표 표시

# cv2.imshow('dst',dst)
# cv2.waitKey()
# cv2.destroyAllWindows()





# # 8.11 Hu의 불변 모멘트


# gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)     # 그레이스케일
# ret, bImage = cv2.threshold(gray,128,255,cv2.THRESH_BINARY)     # 이진 영상

# mode = cv2.RETR_EXTERNAL    # 가장 바깥쪽 contour만
# method = cv2.CHAIN_APPROX_SIMPLE    # 윤곽점 끝점만
# contours, hierarchy = cv2.findContours(bImage,mode,method)  # 윤곽선 검출

# dst = src.copy()
# cnt = contours[0]
# cv2.drawContours(dst,[cnt],0,(0,0,0),3)   # 윤곽선 그리기

# M = cv2.moments(cnt)    # 윤곽선의 경계선 모멘트
# hu = cv2.HuMoments(M)   # Hu의 모멘트를 계산
# print('hu.shape=',hu.shape)
# print('hu=',hu)

# angle = 45.0
# scale = 0.2
# cx = int(M['m10']/M['m00'])         # 중심 x좌표
# cy = int(M['m01']/M['m00'])         # 중심 y좌표
# center = (cx,cy)        # 중심 좌표 정의
# t = (20,30)
# A = cv2.getRotationMatrix2D(center,angle,scale)
# A[:,2] += t     # Affine 변환
# print('A=', A)
# cnt2 = cv2.transform(cnt, A)    # 변환 윤곽선 cnt2
# cv2.drawContours(dst,[cnt2],0,(0,255,0),2)  # 초록 윤곽선
# cv2.imshow('dst',dst)

# M2 = cv2.moments(cnt2)      # 윤곽선 cnt2의 경계선 모멘트
# hu2 = cv2.HuMoments(M2)     # Hu의 모멘트
# print('hu2.shape=',hu2.shape)
# print('hu2=',hu)

# diffSum = np.sum(cv2.absdiff(hu,hu2))   # 배경 차분
# print('diffSum=',diffSum)   

# cv2.waitKey()
# cv2.destroyAllWindows()





# # 8.12 길이, 면적, 바운딩 사각형, 최소 면적 사각형, 최소 면적 원

# gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)     # 그레이스케일
# ret, bImage = cv2.threshold(gray,128,255,cv2.THRESH_BINARY_INV)     # 이진 영상
# bImage = cv2.dilate(bImage, None)
# cv2.imshow('bImage', bImage)

# mode = cv2.RETR_EXTERNAL    # 가장 바깥쪽 contour만
# method = cv2.CHAIN_APPROX_SIMPLE    # 윤곽점 끝점만
# contours, hierarchy = cv2.findContours(bImage, mode, method)    # bImage 윤곽선 검출
# print('len(contours)=', len(contours))

# maxLength = 0
# k = 0
# for i, cnt in enumerate(contours):
#     perimeter = cv2.arcLength(cnt, closed=True)     # 둘레 길이
#     if perimeter > maxLength:    # 길이 가장 긴 윤곽선 검출
#         maxLength = perimeter
#         k = i   # 반복횟수저장

# print('maxLength=', maxLength)
# cnt = contours[k]
# dst2 = src.copy()
# cv2.drawContours(dst2, [cnt], 0, (255,0,0),3)

# area = cv2.contourArea(cnt)     # cnt 면적계산
# print('area=', area)
# x, y, width, height = cv2.boundingRect(cnt)     # 바운딩 사각형 설정
# dst3 = dst2.copy()
# cv2.rectangle(dst3, (x,y), (x+width, y+height), (0,0,255),2)    # 바운딩 사각형 표시
# cv2.imshow('dst3', dst3)

# rect = cv2.minAreaRect(cnt)     # cnt의 최소면적사각형
# box = cv2.boxPoints(rect)       # rect 꼭짓점 좌표
# box = np.int32(box)             # int32 타입의 배열로 변환
# print('box=', box)
# dst4 = dst2.copy()
# cv2.drawContours(dst4, [box], 0, (0,0,255),2)   # 사각형 표시
# cv2.imshow('dst4',dst4)

# (x,y), radius = cv2.minEnclosingCircle(cnt)     # 최소면적 원
# dst5 = dst2.copy()
# cv2.circle(dst5, (int(x),int(y)), int(radius), (0,0,255),2)
# cv2.imshow('dst5', dst5)

# cv2.waitKey()
# cv2.destroyAllWindows()






# 8.13 직선, 다각형, 타원 근사 및 내부 점 확인

gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)     # 그레이스케일
ret, bImage = cv2.threshold(gray,128,255,cv2.THRESH_BINARY_INV)     # 이진 영상
bImage = cv2.dilate(bImage, None)

mode = cv2.RETR_EXTERNAL    # 가장 바깥쪽 contour만
method = cv2.CHAIN_APPROX_SIMPLE    # 윤곽점 끝점만
contours, hierarchy = cv2.findContours(bImage, mode, method)    # bImage 윤곽선 검출

dst = src.copy()
cnt = contours[0]
cv2.drawContours(dst, [cnt], 0, (255,0,0),3)   # 윤괵선 표시

dst2 = dst.copy()
rows, cols = dst2.shape[:2]
[vx, vy, x, y] = cv2.fitLine(cnt, cv2.DIST_L2,0, 0.01, 0.01)    # cnt를 직선으로 근사
y1 = int((-x*vy/vx)+y)          # x1=0, x2=col-1에서의 y1
y2 = int(((cols-x)*vy/vx)+y)    # x1=0, x2=col-1에서의 y2
cv2.line(dst2,(0,y1),(cols-1,y2),(0,0,255),2)   # 구한 점으로 직선 그리기
cv2.imshow('dst2',dst2)

ellipse = cv2.fitEllipse(cnt)   # cnt 타원에 복사
dst3 = dst.copy()
cv2.ellipse(dst3, ellipse, (0,0,255),2)     # dst3에 타원 생성
cv2.imshow('dst3',dst3)

poly = cv2.approxPolyDP(cnt, epsilon=20, closed=True)   # cnt를 다각형으로 근사
dst4 = dst.copy()
cv2.drawContours(dst4, [poly], 0, (0,0,255),2)      # 다각형 그리기
cv2.imshow('dst4',dst4)

dst5 = dst.copy()
for y in range(rows):
    for x in range(cols):
        if cv2.pointPolygonTest(cnt, (x,y),False)>0:    # 점이 다각형 위에 있을 때
            dst5[y,x] = (0,255,0)       # 다각형에 근사
cv2.imshow('dst5',dst5)

cv2.waitKey()
cv2.destroyAllWindows()