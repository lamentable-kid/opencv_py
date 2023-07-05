import cv2
import numpy as np
import imutils
import easyocr
from matplotlib import pyplot as pl

img = cv2.imread('photos/plate_1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_filter = cv2.bilateralFilter(gray, 11, 15, 15)  # удаление шумов
edges = cv2.Canny(img_filter, 30, 200)

cont = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cont = imutils.grab_contours(cont)
cont = sorted(cont, key=cv2.contourArea, reverse=True)

position = None
for c in cont:
    approx = cv2.approxPolyDP(c, 20, True)
    if len(approx) == 4:
        position = approx
        break

mask = np.zeros(gray.shape, np.uint8)
new_img = cv2.drawContours(mask, [position], 0, 255, cv2.FILLED)
bitwise_img = cv2.bitwise_and(img, img, mask=mask)

x, y = np.where(mask == 255)
x1, y1 = np.min(x), np.min(y)
x2, y2 = np.max(x), np.max(y)
crop = gray[x1:x2, y1:y2]  # обрезание номера

text = easyocr.Reader(['en'])
text = text.readtext(crop)  # считывание текста
print(text[1][1])
final_image = cv2.putText(img, text[1][1], (x1, y2 + 60), cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 255), thickness=3)
final_image = cv2.rectangle(img, (x1, x2), (y1, y2), (0, 255, 0), thickness=3)

pl.imshow(cv2.cvtColor(final_image, cv2.COLOR_BGR2RGB))
pl.show()
