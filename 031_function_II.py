'''The Examples for The Function II Section

It demonstrates arbitrary argument list, keyword-only argument, and lambda.

Use `$ pydoc3 <module_name>` or `>>> help(module)` to see this doc.
'''


def print_args(a, *t, k, **d):

    # t and d: arbitrary argument list
    # k: keyword-only argument

    print('a:', a)
    print('t:', t)
    print('k:', k)
    print('d:', d)
    print()


def show_me_lambda():

    items = ['Python', 'Ruby', 'JavaScript']

    items.sort()
    print(items)

    items.sort(key=len)
    print(items)

    item_weight_map = {'Python': -90, 'Ruby': -50}
    items.sort(key=lambda item: item_weight_map.get(item, 0))
    print(items)


def sum_vars(*args):
    '''Sum variables.

    The arg can be any object which supports += delimiter.
    '''

    # https://docs.python.org/3/library/stdtypes.html#iterator-types
    args_it = iter(args)
    ret_val = next(args_it)
    for arg in args_it:
        ret_val += arg

    return ret_val


if __name__ == '__main__':

    print_args('a', 't1', 't2', k='k', dk='dv')
    show_me_lambda()

    print(sum_vars(1, 2, 3))
    print(sum_vars('a', 'b', 'c'))
    print()
