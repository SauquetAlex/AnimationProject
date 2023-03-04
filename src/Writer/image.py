# imports
import cv2
import numpy as np

name = "cone.png"
original = cv2.imread('Input\\'+name)
dim = (16, 16)

f = open("image.txt", "w+")

f.write(f"{dim[0]} {dim[1]}\n")
image = cv2.resize(original, dim, interpolation=cv2.INTER_AREA)
cv2.imwrite('Output\\images\\' + name, image)
    #for i in range(0, dim[0]):
    #    for j in range(0, dim[1]):
    #        f.write("#%02x%02x%02x" %
    #                (image[i][j][0], image[i][j][1], image[i][j][2]))
    #        if (i != dim[0] - 1 or j != dim[1] - 1):
    #            f.write(" ")
    #image = cv2.resize(image, (500, 500), interpolation=cv2.INTER_AREA)
    #cv2.imshow('Image', image)
