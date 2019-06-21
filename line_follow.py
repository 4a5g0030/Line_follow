import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('img_06.jpg')
gary = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
re, th = cv.threshold(gary, 0, 255, cv.THRESH_OTSU)
Otsu = cv.cvtColor(th, cv.COLOR_BGR2RGB)
plt.imshow(Otsu)
h, w = Otsu.shape[:2]

for i in np.arange(0, h, 100):
    cv.line(Otsu, (0, i), (w, i), (0, 0, 0), 2)
for i in np.arange(0, w, 100):
    cv.line(Otsu, (i, 0), (i, h), (0, 0, 0), 2)
plt.imshow(Otsu)

Otsu = cv.cvtColor(th, cv.COLOR_BGR2RGB)
median = cv.medianBlur(Otsu, 55)
plt.imshow(median)
