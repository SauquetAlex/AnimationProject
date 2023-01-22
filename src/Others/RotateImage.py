import cv2

# open cone.png and rotate it by 180 degrees and saves it
img = cv2.imread('input/cone.png')
img = cv2.rotate(img, cv2.ROTATE_180)
cv2.imwrite('input/RotatiedCone.png', img)
