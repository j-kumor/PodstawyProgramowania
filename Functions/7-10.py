###
# A program that print number of negative even numbers in the range <x, y>
#

def neg_even(x, y):
    counter = 0
    if x < 0:
        while x < 0 and x <= y:
            if x % 2 == 0:
                x += 1
                counter += 1
            else:
                x += 1
    else:
        return 0
    return counter


print(neg_even(-7, 8))
print(neg_even(-1, 11))
print(neg_even(-10, -3))
