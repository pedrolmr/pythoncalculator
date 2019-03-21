import re

print('calculator')
print('Type \'quit\' to exit\n')

previous = 0
run = True

def performMath():
    global run #makes the run variable global
    global previous

    equation = input('enter equation:')
    if equation == 'quit':
        run = False
    else:
        previous = eval(equation)

        print('You typed', previous)

while run:
    performMath()

    