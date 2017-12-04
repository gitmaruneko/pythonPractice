import sys


def show(name):
    print('Hi, {}' .format(name))


if __name__ == '__main__':
    name = sys.argv[1]
    show(name)
