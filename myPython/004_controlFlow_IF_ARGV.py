import sys

def controlFlow(name):
    flag = False
   # name = 'Heidi'
    if name == 'python':
        flag = True
        print ('Welcome! Boss!')
    else:
        print ('Hi, {}' .format(name)) 


if __name__ == '__main__':
    name = sys.argv[1]
    controlFlow(name)


