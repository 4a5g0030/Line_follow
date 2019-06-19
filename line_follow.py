import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('img_06.jpg')
gary = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
re, th = cv.threshold(gary, 0, 255, cv.THRESH_OTSU)
Otsu = cv.cvtColor(th, cv.COLOR_BGR2RGB)
plt.imshow(Otsu)
