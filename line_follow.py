import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('img_06.jpg')
show_img = cv.flip(img, -1)
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

flip = cv.flip(median, -1)
plt.imshow(flip)

windos = flip[0:51, 0:51, 1]
windos = list(np.concatenate(windos))
plt.imshow(flip[0:51, 0:51, :])

mx = []
my = []
for y in range(0, h, 50):
    max = 0
    loc = 0
    windos_list = []
    for x in np.arange(0,w,10):
        windos = flip[y:y+51, x:x+51, 1]
        windos = list(np.concatenate(windos))
        windos_list.append(windos.count(0))
        if(windos.count(0)>max):
            loc = x
            max = windos.count(0)
    if(max>500):
        cv.rectangle(show_img, (loc, y), (loc+51, y+51), (255,0,0), 2)
        mx.append(loc+26)
        my.append(y+26)

for n in np.arange(mx.__len__()-1):
    cv.line(show_img, (mx[n], my[n]), (mx[n+1], my[n+1]), (0,255,0), 2)

plt.imshow(cv.flip(show_img, -1))
