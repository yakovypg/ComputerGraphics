import cv2

sourceImage = cv2.imread('cat.jpg')
hsvImage = cv2.cvtColor(sourceImage, cv2.COLOR_BGR2HSV)

cv2.imwrite('result.jpg', hsvImage)

cv2.imshow('Source image', sourceImage)       
cv2.imshow('HSV image', hsvImage)

cv2.waitKey(0)
cv2.destroyAllWindows()
