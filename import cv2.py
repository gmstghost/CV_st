import cv2
img_color = cv2.imread("EpGpT0AUYAI4U7s_1.jpg", cv2.IMREAD_COLOR)
cv2.namedWindow("tmp1")
cv2.imshow("tmp1",img_color)

cv2.resizeWindow("tmp1", 1, 1)
cv2.waitKey(0)
cv2.destroyAllWindows()