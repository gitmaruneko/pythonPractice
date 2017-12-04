from PIL import Image


def showPic():
    image = Image.open('hw.png')
    image.show()

if __name__ == '__main__':
    showPic()


