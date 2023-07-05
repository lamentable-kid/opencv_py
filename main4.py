import cv2
import numpy as np

"""Побитовые операции и маски"""

photo = cv2.imread("photos/castle.jpg")
img = np.zeros(photo.shape[:2], dtype='uint8')

circle = cv2.circle(img.copy(), (300, 300), 80, 255, thickness=cv2.FILLED)
square = cv2.rectangle(img.copy(), (25, 25), (250, 350), 255, thickness=cv2.FILLED)

img = cv2.bitwise_and(photo, photo, mask=circle)
# img = cv2.bitwise_or(circle, square)
# img = cv2.bitwise_xor(circle, square)
# img = cv2.bitwise_not(circle)

cv2.imshow("Photo", img)
cv2.waitKey(0)
