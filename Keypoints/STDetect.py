# 시와 토마시 코너 검출

import cv2
import numpy as np

img = cv2.imread('.\\img\\tiger.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# (src, 코너 개수, 스레시홀드, 코너간 최소거리)
cnrs = cv2.goodFeaturesToTrack(gray, 150, 0.01, 10)      
cnrs = np.int32(cnrs)

for cnr in cnrs:
    x, y = cnr[0]
    cv2.circle(img, (x, y), 5, (255,0,0), 1, cv2.LINE_AA)

cv2.imshow("goodFeaturesToTrack", img)
cv2.waitKey()
cv2.destroyAllWindows()