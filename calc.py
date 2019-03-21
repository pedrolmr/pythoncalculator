import re

print("calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True

def performMath():
    global run #makes the run variable global

    equation = input("enter equation:")
    if equation == "quit":
        run = False
    else:
        print("You typed", equation)

while run:
    performMath()

    