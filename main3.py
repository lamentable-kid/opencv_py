import cv2
import numpy as np

img = cv2.imread('photos/castle.jpg')
img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
new_img = np.ones(img.shape, dtype='uint8')

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (5, 5), 0)
img = cv2.Canny(img, 100, 140)

con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(new_img, con, -1, (230, 111, 148), thickness=1)

# r, g, b = cv2.split(img)
# img = cv2.merge([r, g, b])

cv2.imshow('Photo', new_img)
cv2.waitKey(0)
