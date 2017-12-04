# same the func in as 012_control_flow_stmts.py
def calc_bmi(height_cm, weight_kg):
    return weight_kg / (height_cm/100)**2

def ask_int():
    while True:
        try:
            return int(input())
        except ValueError as e:
            pstderr('Error:', e)

if __name__ == '__main__':
  
    print('Please enter height: ')
    height_cm = ask_int()
    print('Please enter weight: ')
    weight_kg = ask_int()
    print('You BMI is : {}' .format(calc_bmi(height_cm, weight_kg)))

