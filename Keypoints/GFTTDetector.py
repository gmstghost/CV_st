# GFTTDetector를 활용한 특징점 검출

import cv2
import numpy as np

img = cv2.imread('.\\img\\tiger.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gfft = cv2.GFTTDetector_create()               # 검출기 객체 생성
keylst = gfft.detect(gray, None)               # gray에 대한 특징점 검출
dst = cv2.drawKeypoints(img, keylst, None)     # 검출된 특징점 모두 그리기

cv2.imshow('GFTTDectector', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()