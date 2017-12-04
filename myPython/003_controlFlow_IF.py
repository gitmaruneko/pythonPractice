def controlFlow(name):
    flag = False
   # name = 'Heidi'
    if name == 'python':
        flag = True
        print ('Welcome! Boss!')
    else:
        print ('Hi, {}' .format(name)) 


if __name__ == '__main__':
    name = input('Please enter name: ')
    controlFlow(name)


