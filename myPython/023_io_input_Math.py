import sys


def add(a, b):
    return a+b


def pstderr(*args, **argd):
    print(*args, file=sys.stderr, **argd)


def ask_int():
    while True:
        try:
            return int(input('Please enter an integer: '))
        except ValueError as e:
            pstderr('Error:', e)


def main():
    print(add(
        ask_int(),
        ask_int()
    ))


if __name__ == '__main__':
    main()
