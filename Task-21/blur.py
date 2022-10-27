import cv2

source = cv2.imread('cat.jpg')

kernel = (5, 5)
averaging = cv2.blur(source, kernel)
gausBlur = cv2.GaussianBlur(source, kernel, 0)

cv2.imwrite('averaging.jpg', averaging)
cv2.imwrite('gausBlur.jpg', gausBlur)

cv2.imshow("Source", source)
cv2.imshow('Averaging', averaging)
cv2.imshow('Gaussian Blurring', gausBlur)

cv2.waitKey(0)
cv2.destroyAllWindows()
