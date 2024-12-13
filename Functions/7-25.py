###
# A function that returns the sum of numbers in the range <x, y>
# that are completely divisible by 2 and 3 and not divisible by 4
#

def f(x, y):
    result = 0
    for i in range(x, y + 1):
        if i % 6 == 0 and not i % 4 == 0:
            result += i
    return result


print(f(1,20))
print(f(10,30))
