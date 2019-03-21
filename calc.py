import re

print('calculator')
print('Type \'quit\' to exit\n')

previous = 0
run = True


def performMath():
    global run  # makes the run variable global
    global previous
    equation = ""
    if previous == 0:
        equation = input('enter equation:')
    else:
        equation = input(str(previous))

    if equation == 'quit':
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)
        if previous == 0:
            previous = eval(equation)
            fp = open("equations.txt", "w")
            fp.write(str(previous))
            fp.close()
        else:
            previous = eval(str(previous) + equation)
            fp = open("equations.txt", "w")
            fp.write(str(previous)+)
            fp.close()


while run:
    performMath()
