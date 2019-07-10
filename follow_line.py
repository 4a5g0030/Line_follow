import matplotlib.pyplot as plt
import numpy as np
import cv2

class linefollow:
    def __init__(self, path):
        self.orgimg = cv2.imread(path)
        self.size()
        self.set_()


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


    def flip_(self):
        return cv2.flip(self.median(), -1)

    def set_(self):
        self.msk_w = round(self.w/3)
        self.msk_h = round(self.h/6)
        self.flip = self.flip_()


    def windows(self):
        pass


class planA(linefollow):
    def windows(self):
        show = cv2.flip(self.orgimg, -1)
        for y in range(2):
            loc = 0
            max = 0
            for x in range(0, self.w - self.msk_w, round(self.msk_w / 2)):
                win = self.flip[(y*self.msk_h):(y*self.msk_h)+self.msk_h, x:x+self.msk_w]
                win = list(np.concatenate(win))
                if(max < win.count(0)):
                    max = win.count(0)
                    loc = x
            cv2.rectangle(show, (loc, (y*self.msk_h)), (loc+self.msk_w, (y*self.msk_h)+self.msk_h), (255, 0, 0), 5)
        return cv2.flip(show, -1)


class planB(linefollow):
    def windows(self):
        show = cv2.flip(self.orgimg, -1)
        loc = 0
        max = 0
        for y in range(0, self.h - self.msk_h, round(self.msk_h / 2)):
            win = self.flip[y:y+self.msk_h, 0:0+self.msk_w]
            win = list(np.concatenate(win))
            if(max < win.count(0)):
                max = win.count(0)
                loc = y
        cv2.rectangle(show, (0, loc), (0, loc + self.msk_h), (255, 0, 0), 5)
        plt.imshow(cv2.flip(show, -1))



def main():
    img = planB("img02.jpg")
    img.windows()

if __name__ == '__main__':
    main()
