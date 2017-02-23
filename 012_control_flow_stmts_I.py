def say_hello(name=None):

    if name is None:
        print('Hello!')
    elif name == 'Mosky':
        print('Hello, Miss {}!'.format(name))
    elif name == 'Mosky Liu':
        print('Hello, Miss {}!'.format(name))
    else:
        print('Hello, {}!'.format(name))


def calc_bmi(height_cm, weight_kg):

    if height_cm <= 0:
        print('height_cm must be larger than zero.')
        return 0

    if weight_kg <= 0:
        print('weight_kg must be larger than zero.')
        return 0

    # https://en.wikipedia.org/wiki/Body_mass_index
    return weight_kg / (height_cm/100)**2


def print_bmi_report(height_cm, weight_kg):
    print('height_cm: {}'.format(height_cm))
    print('weight_kg: {}'.format(weight_kg))
    print('BMI: {:.2f}'.format(calc_bmi(height_cm, weight_kg)))
    print()


def count_down():

    current_no = 3
    while current_no:
        print('current_no:', current_no)
        current_no -= 1
    print()


if __name__ == '__main__':

    say_hello()
    say_hello('Mosky')
    say_hello('Mosky Liu')
    say_hello('Apple')
    print()

    height_cm = 0
    weight_kg = 0
    print_bmi_report(height_cm, weight_kg)

    height_cm = 165
    weight_kg = 50
    print_bmi_report(height_cm, weight_kg)

    count_down()
