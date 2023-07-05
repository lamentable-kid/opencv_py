import cv2
import numpy as np

photo = np.zeros((300, 300, 3), dtype='uint8')
photo[30:70, 40:50] = 255, 0, 0  # BGR

cv2.rectangle(photo, (100, 100), (200, 200), (119, 201, 105), thickness=cv2.FILLED)
cv2.line(photo, (90, 150), (210, 150), (223, 232, 53), thickness=3)
cv2.putText(photo, 'photo', (200, 200), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 255, 0), thickness=1)

photo = cv2.flip(photo, 0)  # 0 or 1 or -1  mirror

cv2.imshow('Photo', photo)
cv2.waitKey(0)
