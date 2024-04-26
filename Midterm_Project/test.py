# 가우시안 필터링 -> 히스토그램 스트레칭 -> 캐니 필터

import cv2
import numpy as np

image = cv2.imread('image3.png')

gaussian = cv2.GaussianBlur(image, (5, 5), 0)
gray = cv2.cvtColor(gaussian, cv2.COLOR_BGR2GRAY)
stretching = cv2.normalize(gray, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
canny = cv2.Canny(stretching, 100, 200)

cv2.imshow('Original', image)
cv2.imshow('Gaussian Filter', gaussian)
cv2.imshow('Histogram Stretching', stretching)
cv2.imshow('Canny Filter', canny)

cv2.imwrite('original.png', image)
cv2.imwrite('gaussian.png', gaussian)
cv2.imwrite('histogram Stretching.png', stretching)
cv2.imwrite('canny1.png', canny)

cv2.waitKey(0)
cv2.destroyAllWindows()




# 가우시안 필터링 -> 히스토그램 스트레칭 -> LoG 필터

import cv2
import numpy as np

image = cv2.imread('image3.png')

gaussian = cv2.GaussianBlur(image, (5, 5), 0)
gray = cv2.cvtColor(gaussian, cv2.COLOR_BGR2GRAY)
stretching = cv2.normalize(gray, None, 0, 255, cv2.NORM_MINMAX)
log = cv2.Laplacian(stretching, cv2.CV_64F)

cv2.imshow('Original', image)
cv2.imshow('Gaussian Filter', gaussian)
cv2.imshow('Histogram Stretching', stretching)
cv2.imshow('LoG Filter', log)

cv2.imwrite('histogram Stretching.png', stretching)
cv2.imwrite('log1.png', log)

cv2.waitKey(0)
cv2.destroyAllWindows()




# 가우시안 필터링 -> 히스토그램 평활화 -> 캐니 필터

import cv2
import numpy as np

image = cv2.imread('image3.png')

gaussian = cv2.GaussianBlur(image, (5, 5), 0)
gray = cv2.cvtColor(gaussian, cv2.COLOR_BGR2GRAY)
equalization = cv2.equalizeHist(gray)
canny = cv2.Canny(equalization, 100, 200)

cv2.imshow('Original', image)
cv2.imshow('Gaussian Filter', gaussian)
cv2.imshow('Histogram Equalization', equalization)
cv2.imshow('Canny  Filter', canny)

cv2.imwrite('equalization.png', equalization)
cv2.imwrite('canny2.png', canny)

cv2.waitKey(0)
cv2.destroyAllWindows()




# 가우시안 필터링 -> 히스토그램 평활화 -> LoG 필터

import cv2
import numpy as np

image = cv2.imread('image3.png')

gaussian = cv2.GaussianBlur(image, (5, 5), 0)
gray = cv2.cvtColor(gaussian, cv2.COLOR_BGR2GRAY)
equalization = cv2.equalizeHist(gray)
log = cv2.Laplacian(equalization, cv2.CV_64F)

cv2.imshow('Original', image)
cv2.imshow('Gaussian Filter', gaussian)
cv2.imshow('Histogram Equalization', equalization)
cv2.imshow('LoG Filter' , log)

cv2.imwrite('log2.png', log)

cv2.waitKey(0)
cv2.destroyAllWindows()
