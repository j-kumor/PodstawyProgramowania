###
# A function that returns the value of the expression
#

def f(expression):
    operator = '+'
    if expression[0] == '-':
        operator = '-'
    result = 0
    number = 0

    for i in expression:
        if i == '+':
            operator = '+'
            continue
        if i == '-':
            operator = '-'
            continue
        if int(i) in range(0, 10):
            number = int(i)
        if operator == '+':
            result += number
            operator = ''
        if operator == '-':
            result -= number
            operator = ''
    return result

print(f("2+3"))
print(f("3+8+1"))
print(f("2+3-4+5-0"))
