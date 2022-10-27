import cv2
import numpy as np

kernelSize = (5, 5)
kernel = np.ones(kernelSize, np.uint8)

source = cv2.imread('cat.jpg')
erosion = cv2.erode(source, kernel, iterations = 1)

cv2.imwrite('result.jpg', erosion)

cv2.imshow("Source", source)
cv2.imshow('Erosion', erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()
