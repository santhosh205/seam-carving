import numpy as np
import cv2
import math

img = cv2.imread("copy.jpg", 1)
w, h = len(img), len(img[0])

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# check output by changing the kernel size to (3, 3), (7, 7) and (9, 9)
blur = cv2.GaussianBlur(gray, (5, 5), 0)

laplacian = cv2.Laplacian(blur, cv2.CV_64F)

# implement the dynamic programming technique described in wikipedia on laplacian

cv2.imshow('img', img)
cv2.imshow('gray', gray)
cv2.imshow('blur', blur)
cv2.imshow('laplacian', laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()