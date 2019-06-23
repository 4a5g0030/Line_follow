import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('img_06.jpg')
step_w = 50
step_h = 50

(windos_w,windos_h) = (100, 50)

for x in np.arange(0, img.shape[1]-windos_w, step_h):
    for y in np.arange(0, img.shape[0]-windos_h, step_h):
        cv.rectangle(img, (x, y), (x+windos_w, y+windos_h), (255,0,0), 2)

plt.imshow(img)
