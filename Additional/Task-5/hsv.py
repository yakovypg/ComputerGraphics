import cv2

camera = cv2.VideoCapture(0)
result, image = camera.read()

if result:
    hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    cv2.imwrite('camera.jpg', image)
    cv2.imwrite('result.jpg', hsvImage)

    cv2.imshow('Camera', image)
    cv2.imshow('HSV image', hsvImage)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print('No image detected.')
