def any_negative(*args):
    return any(arg < 0 for arg in args)


def all_non_negative(*args):
    return all(not arg < 0 for arg in args)
    # === all(arg >= 0 for ...)


def sum_of(prices, quantities):
    return sum(p*q for p, q in zip(prices, quantities))


# other prime examples are in 21_control_flow_stmts_II.py
def calc_primes_3(n):
    return [
        i
        for i in range(2, n)
        if not any(i % j == 0 for j in range(2, i))
    ]


def input_a_list():
    # numbers_str: '1 2 3'
    numbers_str = input('Please input numbers separated with space: ')
    # number_strs: ['1', '2', '3']
    number_strs = numbers_str.split(' ')
    # number_str: '1'
    return [int(number_str) for number_str in number_strs]


if __name__ == '__main__':

    print(any_negative(0, 1, 2))
    print(any_negative(0, -1, 2))
    print(any_negative())
    print()

    print(all_non_negative(0, 1, 2))
    print(all_non_negative(0, -1, 2))
    print(all_non_negative())
    print()

    print(sum_of(
        prices=[100, 200, 300],
        quantities=[1, 2, 3]
    ))
    print()

    print(calc_primes_3(10))
    print()

    print(input_a_list())
