# Harris 코너 검출

import cv2
import numpy as np

img = cv2.imread('.\\img\\tiger.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# (src, 이웃 픽셀 범위, 소벨 필터 크기, 코너 검출 상수, 결과, 외곽 보정 형식)
cnr = cv2.cornerHarris(gray, 2, 3, 0.04)        # gray에 대해 Harris 코너 검출
crd = np.where(cnr>0.1*cnr.max())               # 최댓값 10% 이상 좌표
crd = np.stack((crd[1], crd[0]), axis=-1)       # (y,x) 좌표 교환

# 전체 코너에 대해 화면 출력
for x,y in crd:
    cv2.circle(img, (x,y), 5, (255,0,0), 1, cv2.LINE_AA)

cnr_nrm = cv2.normalize(cnr, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)      # 0~255 정규화

cnr_nrm = cv2.cvtColor(cnr_nrm, cv2.COLOR_GRAY2BGR)         # 전체 검출 결과
mgd = np.hstack((cnr_nrm,img))          # 모두 표시하도록 머지
cv2.imshow("Harriscorner", mgd)
cv2.waitKey()
cv2.destroyAllWindows()