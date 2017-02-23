def show_me_list():

    numbers = [1, 2, 3]
    print('numbers:', numbers)
    numbers.append(4)
    print('numbers:', numbers)
    print()

    # more operations:
    # https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types
    print('numbers[0]:', numbers[0])
    print('numbers[-1]:', numbers[-1])
    print('numbers[1:3]:', numbers[1:3])
    print('numbers[::-1]:', numbers[::-1])
    print()

    numbers[0] = 100
    print('numbers:', numbers)
    numbers.sort()
    print('numbers:', numbers)
    print()

    numbers2 = numbers
    numbers2[0] = 200
    print('numbers:', numbers)
    print('numbers2:', numbers2)
    print()

    numbers3 = numbers.copy()
    numbers3[0] = 2000
    print('numbers:', numbers)
    print('numbers3:', numbers3)
    print()

    mixed_list = ['x', 'y', 1]
    print('mixed_list:', mixed_list)
    mixed_list.append(2)
    print('mixed_list:', mixed_list)
    print()

    # range(3) -> range object
    # https://docs.python.org/3/library/stdtypes.html#ranges
    print('list(range(3)):', list(range(3)))
    print('list(range(1, 3)):', list(range(1, 3)))
    print('list(range(1, 3+1)):', list(range(1, 3+1)))
    print('list(range(0, 10, 2)):', list(range(0, 10, 2)))
    print()


def show_me_dict():

    id_name_map = {
        'mosky.liu': 'Mosky Liu',
        # the final comma is optional
        'mosky.bot': 'Mosky Bot',
    }
    print('id_name_map:', id_name_map)

    print('.keys():', id_name_map.keys())
    print('.values():', id_name_map.values())
    print('.items():', id_name_map.items())
    print()

    print(".get('x', 'id doesn\'t exist'):",
        id_name_map.get('x', 'id doesn\'t exist')
    )
    print()

    # more operations:
    # https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
    id_name_map['yiyu.liu'] = 'Yi-Yu Liu'
    print('id_name_map:', id_name_map)
    print()


def show_me_tuple():

    print('single:', (1, ))

    xypair_item_map = {
        (10, 20): '$100'
    }
    print('xypair_item_map:', xypair_item_map)
    print()

    pair = (1, 2)
    a, b = pair
    print('pair:', pair)
    print('a:', a)
    print('b:', b)
    print()

    # a, b actually makes a tuple
    b, a = a, b
    print('a:', a)
    print('b:', b)
    print()

    # all seqs (including list and range object) can be unpacked
    head, *bodies, tail = range(4)
    print('head:', head)
    print('bodies:', bodies)
    print('tail:', tail)
    print()


def show_me_set():

    print(set('apple'))
    print()

    banned_ips = {
        '192.168.0.1',
        '192.168.0.1',
        '192.168.0.2',
        '192.168.0.3',
    }
    print('banned_ips:', banned_ips)
    print("Is '192.168.0.1' in banned_ips?", '192.168.0.1' in banned_ips)
    print()

    # more operations:
    # https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
    print(set('apple') & set('orange'))
    print()

if __name__ == '__main__':

    show_me_list()
    show_me_dict()
    show_me_tuple()
    show_me_set()
