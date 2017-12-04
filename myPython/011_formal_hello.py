# -*- coding: UTF-8 -*-
def say_hello(name):
    print('Hello, {}!'.format(name))
    print('{1} {0} {1}!'.format(name, "Hello"))
    print("Activity： {name}, Location : {locate}".format(name="Pair Programming", locate="WWC"))


if __name__ == '__main__':
    say_hello('Heidi')
