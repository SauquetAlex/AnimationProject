# imports
import cv2
import numpy as np

original = cv2.imread('Input\cone.png')
dim = (16, 16)

f = open("image.txt", "w+")

while 1:
    image = cv2.resize(original, dim, interpolation=cv2.INTER_AREA)
    for i in range(0, dim[0]):
        for j in range(0, dim[1]):
            f.write("#%02x%02x%02x" %
                    (image[i][j][0], image[i][j][1], image[i][j][2]))
            if (i != dim[0] - 1 or j != dim[1] - 1):
                f.write(" ")
    image = cv2.resize(image, (500, 500), interpolation=cv2.INTER_AREA)
    cv2.imshow('Image', image)
    if cv2.waitKey(100000) & 0xFF == ord('q'):
        break
