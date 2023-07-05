import cv2
import numpy as np

img = cv2.imread('photos/castle.jpg')
print(img.shape)
img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.Canny(img, 100, 100)  # нахождение углов(обводка)

kernel = np.ones((5, 5), np.uint8)  # установка точек
img = cv2.dilate(img, kernel, iterations=1)  # сильнее обводка

img = cv2.erode(img, kernel, iterations=3)  # уменьшить контур (верхнее нужно чтобы эти контуры просто найти)

cv2.imshow('Result', img)

cv2.waitKey(0)

# cap = cv2.VideoCapture('videos/1.mp4')
# cap.set(3, 500)
# cap.set(4, 300)
# while True:
#     success, img = cap.read()
#     cv2.imshow('Result', img)
#
#     if cv2.waitKey(20) & 0xFF == ord('q'):
#         break
