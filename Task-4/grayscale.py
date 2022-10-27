import cv2

colorImage = cv2.imread('cat.jpg')
grayImage = cv2.cvtColor(colorImage, cv2.COLOR_BGR2GRAY)

cv2.imwrite('result.jpg', grayImage)

cv2.imshow('Color image', colorImage)       
cv2.imshow('Gray image', grayImage)

cv2.waitKey(0)
cv2.destroyAllWindows()
