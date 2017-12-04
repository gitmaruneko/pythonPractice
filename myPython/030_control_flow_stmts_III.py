def calc_bmi(height_cm, weight_kg):

    if height_cm <= 0:
        print('height_cm must be larger than zero.')
        return 0

    if weight_kg <= 0:
        print('weight_kg must be larger than zero.')
        return 0

    # https://en.wikipedia.org/wiki/Body_mass_index
    return weight_kg / (height_cm/100)**2


def calc_bmi_3(height_cm, weight_kg):

    if height_cm <= 0:
        raise ValueError('height_cm must > 0')

    if weight_kg <= 0:
        raise ValueError('weight_kg must > 0')

    # https://en.wikipedia.org/wiki/Body_mass_index
    return weight_kg / (height_cm/100)**2


def print_bmi_report_3(height_cm, weight_kg):
    print('height_cm: {}'.format(height_cm))
    print('weight_kg: {}'.format(weight_kg))
    print('BMI: {:.2f}'.format(calc_bmi_3(height_cm, weight_kg)))


def ask_int():
    return int(input())



if __name__ == '__main__':

    print('Please enter height: ')
    height_cm = ask_int()
    print('Please enter weight: ')
    weight_kg = ask_int()
    print_bmi_report_3(height_cm, weight_kg)
