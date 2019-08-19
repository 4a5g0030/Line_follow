import cv2
import glob
import follow_line as fl
import time
import numba as nb

def func_time(func):
    def ft():
        s = time.clock()
        func()
        e = time.clock()
        print('use time :', e - s)
    return ft()

@nb.jit
@func_time
def main():
    img_in_root = 'test_data/image/'
    img_out_root = 'test_data/output/'
    img_count = len(glob.glob(img_in_root + '*jpg'))

    for x in range(img_count):
        img = fl.planA(img_in_root + str(x).zfill(3) + '.jpg')
        img = img.windows()
        # cv2.imwrite(img_out_root + str(x).zfill(3) + '.jpg', img)
        print('{:.2%}'.format(x / img_count))
    print('100%')


if __name__ == '__main__':
    main
