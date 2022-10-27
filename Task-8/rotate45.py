import cv2
import numpy as np

def rotateImage(image, angle):
    center = tuple(np.array(image.shape[1::-1]) / 2)
    rotationMatrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    result = cv2.warpAffine(image, rotationMatrix, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  
    return result

def rotateImageWithoutCuttingSides(image, angle):
    height, width = image.shape[:2]
    imageCenter = (width / 2, height / 2)

    rotationMatrix = cv2.getRotationMatrix2D(imageCenter, angle, 1.)

    absCos = abs(rotationMatrix[0,0]) 
    absSin = abs(rotationMatrix[0,1])

    boundWidth = int(height * absSin + width * absCos)
    boundHeight = int(height * absCos + width * absSin)
    boundSize = (boundWidth, boundHeight)

    rotationMatrix[0, 2] += boundWidth / 2 - imageCenter[0]
    rotationMatrix[1, 2] += boundHeight / 2 - imageCenter[1]

    return cv2.warpAffine(image, rotationMatrix, boundSize)

angle = 45

source = cv2.imread('cat.jpg')
result = rotateImage(source, angle)
resultWithoutCuttingSides = rotateImageWithoutCuttingSides(source, angle)

cv2.imwrite('result.jpg', result)
cv2.imwrite('resultWithoutCuttingSides.jpg', resultWithoutCuttingSides)

cv2.imshow('Source', source)       
cv2.imshow('Result', result)
cv2.imshow('Result without cutting sides', resultWithoutCuttingSides)

cv2.waitKey(0)
cv2.destroyAllWindows()
