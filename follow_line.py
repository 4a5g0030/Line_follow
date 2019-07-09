import matplotlib.pyplot as plt
import numpy as np
import cv2

class linefollow:
    def __init__(self, path):
        self.orgimg = cv2.imread(path +".jpg")
        self.size()


    def size(self):
        self.h , self.w = self.orgimg.shape[:2]


    def gary(self):
        return cv2.cvtColor(self.orgimg, cv2.COLOR_BGR2GRAY)


    def otsu(self):
        re, th = cv2.threshold(self.gary(), 0, 255, cv2.THRESH_OTSU)
        return th


    def median(self):
        msksize = round(self.h / 10)
        if msksize % 2 == 0 : msksize += 1
        return cv2.medianBlur(self.otsu(), msksize)
