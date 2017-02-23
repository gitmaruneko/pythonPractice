def print_pyramid(n):

    # __*
    # _***
    # *****

    # n=3
    # i=0; count of _ -> 2; count of * -> 1
    # i=1; count of _ -> 1; count of * -> 3
    # i=2; count of _ -> 0; count of * -> 5
    # ...
    # count of _ -> n-i-1, count of * -> i*2-1

    for i in range(n):
        print(' '*(n-i-1) + '*'*(i*2-1))
    print()


# variable in upper case to warn other shall not change the content
NAME_TITLE_MAP = {
    'Mosky'    : 'Miss ',
    'Mosky Liu': 'Miss ',
}


def say_hello_to_people(names):

    for name in names:

        if name is None:
            print('Hello!')
            # go back to the `for`
            continue

        print('Hello, {}{}!'.format(
            NAME_TITLE_MAP.get(name, ''),
            name,
        ))

    print()


def print_the_dict():
    for name in NAME_TITLE_MAP:
        print('{} -> {}'.format(name, NAME_TITLE_MAP[name]))
    print()


def print_the_seqs():

    for item in range(3):
        print(item)
    print()

    # https://docs.python.org/3/library/functions.html#zip
    for i, c in zip(range(3), 'abc'):
        print(i, c)
    print()

    # https://docs.python.org/3/library/functions.html#enumerate
    for i, c in enumerate('abc'):
        print(i, c)
    print()


def calc_primes(until_n):

    primes = []
    # 2, 3, 4, ..., until_n
    for n in range(2, until_n):
        # 2, ..., n
        for i in range(2, n):
            if n % i == 0:
                # leave the for-loop
                break
        else:
            # if the loop didn't be broken
            primes.append(n)

    return primes


# https://en.wikipedia.org/wiki/Prime_number
def is_prime(n):

    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def calc_primes_2(until_n):

    primes = []
    for i in range(until_n):
        if is_prime(i):
            primes.append(i)

    return primes


# same the func in as 012_control_flow_stmts.py
def calc_bmi(height_cm, weight_kg):

    if height_cm <= 0:
        print('height_cm must be larger than zero.')
        return 0

    if weight_kg <= 0:
        print('weight_kg must be larger than zero.')
        return 0

    # https://en.wikipedia.org/wiki/Body_mass_index
    return weight_kg / (height_cm/100)**2


# same the func in as 012_control_flow_stmts.py
def print_bmi_report(height_cm, weight_kg):
    print('height_cm: {}'.format(height_cm))
    print('weight_kg: {}'.format(weight_kg))
    print('BMI: {:.2f}'.format(calc_bmi(height_cm, weight_kg)))
    print()


if __name__ == '__main__':

    print_pyramid(5)
    say_hello_to_people([None, 'Mosky', 'Mosky Liu', 'Apple'])
    print_the_dict()
    print_the_seqs()

    print(calc_primes(10))
    print(calc_primes_2(10))
    print()

    height_cm = '165'
    weight_kg = '50'
    print('--- The below traceback is expected ---')
    print_bmi_report(height_cm, weight_kg)

    print("This line won't be printed.")
