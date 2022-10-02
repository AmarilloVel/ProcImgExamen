import cv2
from tkinter.filedialog import * 

photo = askopenfilename()
img = cv2.imread(photo)
res = cv2.resize(img, dsize=(400,400), interpolation=cv2.INTER_CUBIC)

gris = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)
gris = cv2.medianBlur (gris, 3)
bordes = cv2.adaptiveThreshold (gris, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

color = cv2.bilateralFilter(img, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=bordes)

cv2.imshow("images", img)
cv2.imshow("Bordes", bordes)
cv2.imwrite('/Users/hvela/Desktop/7mo/ProcImg/examen1eraParcial/examenPicBordes.jpg',bordes)
cv2.imshow("Cartoon", cartoon)
cv2.imwrite('/Users/hvela/Desktop/7mo/ProcImg/examen1eraParcial/examenPicCartoon.jpg',cartoon)

cv2.waitKey(0)
cv2.destroyAllWindows()
