###
# A program that prints sum of the even digits when number is even
# and sum of the odd digits when number is odd
#

def sum_of_digits(number, even):
    sum_number = 0
    str_num = str(number)
    if even:
        for i in str_num:
            if int(i) % 2 == 0:
                sum_number += int(i)
    else:
        for i in str_num:
            if not int(i) % 2 == 0:
                sum_number += int(i)
    return sum_number


print(sum_of_digits(3124, True))
print(sum_of_digits(3124, False))
print(sum_of_digits(20576, False))
print(sum_of_digits(20567, True))
print(sum_of_digits(13115, True))
