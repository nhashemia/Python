import re

print("Our magical calculator")
print("Type 'quit' to exit \n")
memory = 0
run = True

def performMath():
    global run
    global memory
    equation = ""
    if memory == 0:
        equation = input("Enter equation: ")
    else:
        equation = input(str(memory))
    if equation == "quit":
        run = False
    else:
        equation = re.sub('[a-zA-Z,.$#@~:()""]','',equation)
        if memory == 0:
            memory = eval(equation)
        else:
            memory = eval(str(memory)+equation)

while run:
    performMath();


