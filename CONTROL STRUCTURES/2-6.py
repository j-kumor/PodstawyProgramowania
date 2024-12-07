# Program that checks the number entered from the keyboard
# and prints if it is positive, negative, or zero.

number = float(input('Enter a number: '))

if number > 0:
    print(f'Number {number} is positive')
elif number < 0:
    print(f'Number {number} is negative')
else:
    print('Number is 0')