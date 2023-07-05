import cv2

img = cv2.imread('photos/castle.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = cv2.CascadeClassifier('faces.xml')  # вытягивает натренированную модель

results = faces.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2)

for (x, y, w, h) in results:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

cv2.imshow("Result", img)
cv2.waitKey(0)
