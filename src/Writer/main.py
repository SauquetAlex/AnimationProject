# imports
import cv2
import numpy as np

# Write the name of the video file here (must be in the same folder as the script) and its FPS
cap = cv2.VideoCapture('Input\Rick.mp4')
# make the fps higher if you want to speed up the framing process
fps = 1000

# LED Matrix size
dim = (16, 16)

# Output file
f = open("frames.txt", "w+")

# Imported code from https://stackoverflow.com/questions/13538748/crop-black-edges-with-opencv


def autocrop(image, threshold=0):
    """Crops any edges below or equal to threshold
    Crops blank image to 1x1.
    Returns cropped image.
    """
    if len(image.shape) == 3:
        flatImage = np.max(image, 2)
    else:
        flatImage = image
    assert len(flatImage.shape) == 2

    rows = np.where(np.max(flatImage, 0) > threshold)[0]
    if rows.size:
        cols = np.where(np.max(flatImage, 1) > threshold)[0]
        image = image[cols[0]: cols[-1] + 1, rows[0]: rows[-1] + 1]
    else:
        image = image[:1, :1]
    return image


while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imshow('Original', frame)
    # If there are black borders, crop them here, otherwise comment this out
    frame = autocrop(frame, 50)
    image = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
    for i in range(0, dim[0]):
        for j in range(0, dim[1]):
            f.write("#%02x%02x%02x" %
                    (image[i][j][0], image[i][j][1], image[i][j][2]))
            if (i != dim[0] - 1 or j != dim[1] - 1):
                f.write(" ")
    f.write("\n")
    image = cv2.resize(image, (500, 500), interpolation=cv2.INTER_AREA)
    cv2.imshow('Video2', image)
    if cv2.waitKey(1000//fps) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


# AS
