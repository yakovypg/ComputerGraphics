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

camera = cv2.VideoCapture(0)
result, image = camera.read()

if result:
    result = increaseBrightness(image, 90)
    
    cv2.imwrite('camera.jpg', image)
    cv2.imwrite('result.jpg', result)

    cv2.imshow('Camera', image)
    cv2.imshow('Result', result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print('No image detected.')
