def make_a_list():
    a_list = []
    for i in range(10):
        print('preparing', i)
        a_list.append(i)
    return a_list


def make_a_gen():
    for i in range(10):
        print('preparing', i)
        yield i


if __name__ == '__main__':

    print('Make a List:')
    print()
    a_list = make_a_list()
    print(a_list)
    print()

    print('Make a Generator:')
    print()
    a_gen = make_a_gen()
    print(a_gen)
    print()

    print('Make a List With Loop:')
    print()
    for i in make_a_list():
        print(i)
    print()

    print('Make a Generator With Loop:')
    print()
    for i in make_a_gen():
        print(i)
    print()
