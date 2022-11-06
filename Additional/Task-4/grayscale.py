import cv2

camera = cv2.VideoCapture(0)
result, image = camera.read()

if result:
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imwrite('camera.jpg', image)
    cv2.imwrite('result.jpg', grayImage)

    cv2.imshow('Camera', image)       
    cv2.imshow('Gray image', grayImage)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print('No image detected.')
    