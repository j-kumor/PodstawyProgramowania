###
# A program that checks if the number is in range <x, y>
#

import number_in_range

num = int(input('Enter a number: '))
x = 2
y = 15

print(f'Number {num} in the range <{x}, {y}>: {number_in_range.num_in_range(num, x, y)}')
