def show_me_variable():

    count = 0
    print('count:', count)

    count = count+1
    print('count:', count)

    # `+=` is one of “delimter”s
    # https://docs.python.org/3/reference/lexical_analysis.html#delimiters
    count += 1
    print('count:', count)

    count += 1
    print('count:', count)
    print()


def show_me_is():

    a = '*'*10
    b = '*'*10

    print('a:', repr(a))
    print('b:', repr(b))
    print('a is b?', a is b)
    print('a == b?', a == b)
    print()


if __name__ == '__main__':

    show_me_variable()
    show_me_is()
