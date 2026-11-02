import cv2
import numpy as np

src = cv2.imread('img\\circle1.png')

hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

lower_blue = np.array([96, 73, 234])     
upper_blue = np.array([97, 88, 238]) 

mask = cv2.inRange(hsv, lower_blue, upper_blue)
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    if cv2.contourArea(cnt) > 200:
        cv2.drawContours(src, [cnt], -1, (255, 0, 0), 2)

cv2.imshow("Mask", mask)
cv2.imshow("Result", src)
cv2.waitKey()
cv2.destroyAllWindows()