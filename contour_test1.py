# -*- coding: utf-8 -*-

import numpy as np
import cv2

#cv2.NamedWindow("window_a", cv.CV_WINDOW_AUTOSIZE)
im = cv2.imread('test.jpg')
out = np.zeros(im.shape, np.uint8)

imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(im, contours, -1, (0, 255, 0), 3)

cv2.imshow('im', im)
#cv2.imshow('out', out)
cv2.waitKey(0)
