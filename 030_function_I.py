def inc(x, delta=1):
    return x+delta


def print_n_add(a, b):

    print('a  :', a)
    print('b  :', b)
    print('a+b:', a+b)
    print()

    return a+b


if __name__ == '__main__':

    # default argument values

    print(inc(0))
    print(inc(0, 2))
    print()

    # keyword arguments

    print_n_add(1, 2)
    print_n_add(b=2, a=1)
    print_n_add(1, b=2)
    print()

    # unpacking argument list

    seq = [1, 2]
    print_n_add(*seq)
    d = {'a': 1, 'b': 2}
    print_n_add(**d)

    # dynamic typing

    print_n_add(1, 2)
    print_n_add(1., 2.)
    print_n_add('a', 'b')
