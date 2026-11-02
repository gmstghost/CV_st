# ORB 알고리즘을 활용한 이미지 특징점 매칭

import cv2
import numpy as np

src = cv2.imread('.\\img\\resource2.jpg')
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
target = cv2.imread('.\\img\\amon_blondina.png')

# orb 객체
orb = cv2.ORB_create(
    nfeatures=40000,                    # 최대 피처 수
    scaleFactor=1.2,                    # 스케일 계수
    nlevels=8,                          # 피라미드 레벨
    edgeThreshold=31,                   # 엣지 임곗값
    firstLevel=0,                       # 시작 피라미드 레벨
    WTA_K=2,                            # 비교점
    scoreType=cv2.ORB_HARRIS_SCORE,     # 점수 방식
    patchSize=31,                       # 패치 크기
    fastThreshold=20,                   # FAST 임곗값
)

# 특징점 및 기술자 계산
kp1, des1 = orb.detectAndCompute(gray, None)
kp2, des2 = orb.detectAndCompute(target, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)   # 전수 조사 매칭으로 객체 인식
matches = bf.match(des1, des2)                          # 최적의 매칭 검출
matches = sorted(matches, key=lambda x: x.distance)     # 거리 값 낮은순 정렬

# 상위 100개만 표시
for i in matches[:100]:
    idx = i.queryIdx
    x1, y1 = kp1[idx].pt
    cv2.circle(src, (int(x1), int(y1)), 3, (255,0,0), 3)

cv2.imshow("src", src)
cv2.waitKey()