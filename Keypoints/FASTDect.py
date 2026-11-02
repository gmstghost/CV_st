# FAST로 특징점 검출

import cv2
import numpy as np

img = cv2.imread('.\\img\\tiger.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

fast = cv2.FastFeatureDetector_create(50)           # 검출기 객체 생성
keypoints = fast.detect(gray, None)                 # 특징점 검출
img = cv2.drawKeypoints(img, keypoints, None)       # 특징점 그리기

cv2.imshow('FAST', img)
cv2.waitKey()
cv2.destroyAllWindows()