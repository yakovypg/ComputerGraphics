import cv2
import numpy as np

kernelSize = (5, 5)
kernel = np.ones(kernelSize, np.uint8)

source = cv2.imread('cat.jpg')
dilation = cv2.dilate(source, kernel, iterations = 1)

cv2.imwrite('result.jpg', dilation)

cv2.imshow("Source", source)
cv2.imshow('Dilation', dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()
