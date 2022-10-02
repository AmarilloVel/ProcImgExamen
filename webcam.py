import cv2
from tkinter.filedialog import * 

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    cv2.imshow('Input', frame)

    c = cv2.waitKey(1)
    if c == 27:
        break


photo = askopenfilename()
img = cv2.imread(photo)
res = cv2.resize(img, dsize=(400,400), interpolation=cv2.INTER_CUBIC)

gris = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)
gris = cv2.medianBlur (gris, 3)
bordes = cv2.adaptiveThreshold (gris, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

color = cv2.bilateralFilter(img, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=bordes)

cv2.imshow("images", img)
cv2.imshow("Cartoonize lineas", bordes)

cap.release()
cv2.destroyAllWindows()