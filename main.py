import matplotlib.pyplot as plt
import follow_line as fl


def main():
    path = "img03.jpg"
    imgA = fl.planA(path)
    imgB = fl.planB(path)
    plt.figure()
    plt.subplot(1, 2, 1)
    plt.imshow(imgA.windows())
    plt.subplot(1, 2, 2)
    plt.imshow(imgB.windows())
    plt.show()


if __name__ == '__main__':
    main()
