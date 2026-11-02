import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread('img\\20260607_174237.png', cv2.IMREAD_GRAYSCALE)

img_norm = cv2.normalize(img, None, 30, 150, cv2.NORM_MINMAX)
cv2.imshow('cv2.normalize()', img_norm)
cv2.waitKey()
cv2.destroyAllWindows()