from fractions import gcd
from operator import add
from functools import reduce, partial


def show_me_map():
    print(
        map(int, ['1', '2', '3'])
    )
    print(
        list(map(int, ['1', '2', '3']))
    )


def show_me_filter():
    print(
        filter(lambda i: i % 2 == 0, range(10))
    )
    print(
        list(filter(lambda i: i % 2 == 0, range(10)))
    )


def show_me_reduce():

    print(add(1, 2))
    print(reduce(add, [1, 2, 3]))
    print()

    # 154 = 2*7*11
    # 3003 = 3*7*11*13
    print(gcd(154, 3003))
    print(reduce(gcd, [7, 154, 3003]))


def show_me_partial():
    my_gcd = partial(reduce, gcd)
    print(my_gcd([154, 3003]))
    print(my_gcd([7, 154, 3003]))


if __name__ == '__main__':

    show_me_map()
    print()

    show_me_filter()
    print()

    show_me_reduce()
    print()

    show_me_partial()
