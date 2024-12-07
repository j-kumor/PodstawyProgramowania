###
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 
number1 = float(input('Enter the first number: '))
number2 = float(input('Enter the second number: '))
operator = input('Enter the mathematical operator (+, -, *, /): ')

if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '*':
    result = number1 * number2
elif operator == '/':
    if number2 != 0:
        result = number1 / number2
    else:
        result = 'Undefined (division by zero)'
else:
    result = 'Invalid operator'

print(f'{number1} {operator} {number2} = {result}')