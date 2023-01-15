import cv2
import numpy as np
import pickle

cap = cv2.VideoCapture('CHARGED UP presented by Haas Teaser.mp4')

# play video with a second between each frame
dim = (22, 22)

f = open("frames.txt", "w+")
while (cap.isOpened()):
    ret, frame = cap.read()
    frameRGB = []
    if ret == False:
        break
    image = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
    f.write("{")
    for i in range(0, dim[0]):
        for j in range(0, dim[1]):
            f.write(
                "{" + f"{str(image[i][j][0])},{str(image[i][j][1])},{str(image[i][j][2])}" + "}")
            if (i != dim[0] - 1 or j != dim[1] - 1):
                f.write(",")
    f.write("}")
    f.write("\n")
    image = cv2.resize(image, (500, 500), interpolation=cv2.INTER_AREA)
    cv2.imshow('image', image)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


# Made by Alexandre Sauquet :)
