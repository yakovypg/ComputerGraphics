import cv2
import numpy as np
  
source = cv2.imread('cat.jpg')

height, width = source.shape[:2]
size = (width, height)

quarterHeight, quarterWidth = 0, 10
  
translationMatrix = np.float32([[1, 0, quarterWidth], [0, 1, quarterHeight]])
result = cv2.warpAffine(source, translationMatrix, size)

cv2.imwrite('result.jpg', result)
  
cv2.imshow("Source", source)
cv2.imshow('Result', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
