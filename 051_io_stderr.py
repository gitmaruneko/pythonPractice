import sys


def add(a, b):
    return a+b


def pstderr(*args, **argd):
    print(*args, file=sys.stderr, **argd)


def main():
    try:
        print(
            add(
                int(sys.argv[1]),
                int(sys.argv[2])
            )
        )
    except (IndexError, ValueError) as e:
        pstderr('Error:', e)
        sys.exit(1)


if __name__ == '__main__':
    main()
