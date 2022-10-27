import cv2

def increaseBrightness(img, value):
    hsvImage = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsvImage)

    limit = 255 - value
    v[v > limit] = 255
    v[v <= limit] += value

    resultHsv = cv2.merge((h, s, v))
    result = cv2.cvtColor(resultHsv, cv2.COLOR_HSV2BGR)
    
    return result

source = cv2.imread('cat.jpg')
result60 = increaseBrightness(source, 60)
result90 = increaseBrightness(source, 90)

cv2.imwrite('result60.jpg', result60)
cv2.imwrite('result90.jpg', result90)

cv2.imshow("Source", source)
cv2.imshow('Result 60', result60)
cv2.imshow('Result 90', result90)

cv2.waitKey(0)
cv2.destroyAllWindows()
