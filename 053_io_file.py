import sys


PATH = 'output.txt'


def write_input_into_file():

    # with
    # https://docs.python.org/3/reference/compound_stmts.html#the-with-statement
    # open(...)
    # https://docs.python.org/3/library/functions.html#open
    with open(PATH, 'w') as f:

        while True:

            line = input('| ')
            if line == '':
                break

            # f -> io.TextIOWrapper
            # https://docs.python.org/3/library/io.html#io.TextIOWrapper
            # https://docs.python.org/3/library/io.html#io.TextIOBase
            # https://docs.python.org/3/library/io.html#io.IOBase
            f.write(line)
            f.write('\n')


def read_file_into_stdout():

    with open(PATH) as f:

        for line in f:
            print(line, end='')


def pstderr(*args, **argd):
    print(*args, file=sys.stderr, **argd)


def main():

    if len(sys.argv) < 2:
        pstderr("Need a command: write or read")
        sys.exit(1)

    command = sys.argv[1]
    try:

        if command == 'write':
            print('Enter blank line to exit.')
            write_input_into_file()

        elif command == 'read':
            read_file_into_stdout()

        else:
            pstderr('No such command:', command)
            sys.exit(1)

    except IOError as e:
        pstderr('Error:', e)
        sys.exit(1)


if __name__ == '__main__':
    main()
