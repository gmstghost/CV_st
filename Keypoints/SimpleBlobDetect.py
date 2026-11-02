# SimpleBolbDetector 

import cv2
import numpy as np
 
img = cv2.imread('.\\img\\tiger.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

params = cv2.SimpleBlobDetector_Params()            # 필터 파라미터 생성

# Threshold 조정
params.minThreshold = 10
params.maxThreshold = 240
params.thresholdStep = 5

params.filterByArea = True      # 면적 필터 켜기
params.minArea = 200            # 필터 최소값 지정

# 컬러, 볼록 비율, 원형비율 필터 옵션 끄기
params.filterByColor = False
params.filterByConvexity = False
params.filterByInertia = False
params.filterByCircularity = False 

detector = cv2.SimpleBlobDetector_create()           # detector 객체 생성
keypoints = detector.detect(gray)                    # 특징점 검출
img = cv2.drawKeypoints(img, keypoints, None, (255,0,0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow("SimpleBlob", img)
cv2.waitKey()
cv2.destroyAllWindows()