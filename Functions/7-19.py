###
# A function that returns the sum of repeated digits in a number.
#

def f(number):
    digits = []
    first_repeat = []
    sum_of_repeated = 0
    for i in str(number):
        if i in digits:
            sum_of_repeated += int(i)  # adding repeated digit to sum (doesn't add the first number found)
            if i not in first_repeat:
                # work once when a repeated digit is found for the first time
                first_repeat += i
                sum_of_repeated += int(i)
        else:
            digits.append(str(i))

    return sum_of_repeated


print(f(1027))
print(f(230335))
print(f(513553007))