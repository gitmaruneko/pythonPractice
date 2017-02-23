def show_me_a_int():
    # the spaces are just for clear
    # more operations:
    # https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
    print(10**2 + 2*10 + 2*(3-1)-1)


def show_me_a_big_int():
    print(10**50)


def show_me_a_float():
    print(1 + .2 + 0.03)


def show_me_some_strings():

    # more escapes seqs like \n:
    # https://docs.python.org/3/reference/lexical_analysis.html#strings
    print('I am a string.\n<- There is a newline char.')
    print()

    print('''Fun with triple single-quote pair.
<- There is a newline char.''')
    print()

    print('''\
Escape the newline char
<- There is a newline char.''')
    print()

    print("A double-quote pair works like a singe-quote pair.")
    print()

    print("A string's method: {}.".format('format'))
    print()


def show_diff_between_string_n_bytes():

    print('abc')
    print(b'abc')
    print()

    print('一串字串')
    print(bytes('位元組們', 'utf-8'))
    print()

    # the newline in parentheses will be ignore by Python
    # but it let reader easier to understand
    print("The length of b'一串字串' ->", len('一串字串'))
    print("The length of b'位元組們' ->", len(
        bytes('位元組們', 'utf-8'))
    )
    print()


def show_me_bools():

    print(True)
    print(False)
    print()

    print('Is 100 > 10?', 100 > 10)
    print('Is 100 <= 10?', 100 <= 10)
    print('Is 100 is equal to 100?', 100 == 100)
    print("Is 'Mosky' is equal to 'mosky'?", 'Mosky' == 'mosky')
    print("Is 'Mosky' is not equal to 'mosky'?", 'Mosky' != 'mosky')
    print("Is 'm' is in 'mosky'?", 'm' in 'mosky')
    print()

    # about truth value testing:
    # https://docs.python.org/3/library/stdtypes.html#truth-value-testing
    print('bool(-1):', bool(-1))
    print('bool(0):', bool(0))
    print('bool(1):', bool(1))
    print("bool(''):", bool(''))
    print("bool('apple'):", bool('apple'))
    print()


def show_me_none():

    print(None)
    print()

    print('Is None == 0?', None == 0)
    print('Is None == True?', None == True)
    print('Is None == False?', None == False)
    print('Is None == None?', None == None)
    print()

    print('Usually we use None is None:', None is None)
    print()


if __name__ == '__main__':

    show_me_a_int()
    show_me_a_big_int()
    show_me_a_float()
    print()

    show_me_some_strings()
    show_diff_between_string_n_bytes()

    show_me_bools()
    show_me_none()
