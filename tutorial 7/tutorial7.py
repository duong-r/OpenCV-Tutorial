import numpy as np
import cv2

img = cv2.imread('assets/soccer_practice.jpg', 0)
template = cv2.imread('assets/ball.PNG', 0)
img2 = img.copy()
h, w = template.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,]