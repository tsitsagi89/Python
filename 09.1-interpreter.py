#Math Interpreter
#version 1
expression = input("Expression: ")
x, y, z = expression.split(" ")

x = float(x)
z = float(z)

if y == '+':
    print(x+z)
elif y == '-':
    print(x-y)
elif y == '*':
    print(x*y)
elif y == '/':
    if z != 0:
        print(x/z)
    else:
        print("Division by 0 is not vali.")


#version 2

try:
    expression = input("Expression: ")
    expression = float(eval(expression))
    print(expression)
except:
    print("Division by 0 is not valid")
