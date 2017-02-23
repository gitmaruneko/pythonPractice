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


def print_bmi_report_2(height_cm, weight_kg):

    print('height_cm: {}'.format(height_cm))
    print('weight_kg: {}'.format(weight_kg))

    try:
        # more format string syntax:
        # https://docs.python.org/3/library/string.html#formatstrings
        print('BMI: {:.2f}'.format(calc_bmi(height_cm, weight_kg)))
    except TypeError as e:
        print('Please check the argument: {}.'.format(e))

    print()


def calc_bmi_3(height_cm, weight_kg):

    if height_cm <= 0:
        # more built-in exceptions:
        # https://docs.python.org/3/library/exceptions.html#exception-hierarchy
        raise ValueError('height_cm must > 0')

    if weight_kg <= 0:
        raise ValueError('weight_kg must > 0')

    # https://en.wikipedia.org/wiki/Body_mass_index
    return weight_kg / (height_cm/100)**2


def print_bmi_report_3(height_cm, weight_kg):

    print('height_cm: {}'.format(height_cm))
    print('weight_kg: {}'.format(weight_kg))

    try:
        print('BMI: {:.2f}'.format(calc_bmi_3(height_cm, weight_kg)))
    except (TypeError, ValueError) as e:
        print('Please check the argument: {}.'.format(e))

    print()


if __name__ == '__main__':

    height_cm = '165'
    weight_kg = '50'
    print_bmi_report_2(height_cm, weight_kg)

    height_cm = 0
    weight_kg = 0
    print_bmi_report_3(height_cm, weight_kg)
