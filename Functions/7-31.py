###
# A function that calculates x to the power of n
#

def power(x, n):
    if n == 1:
        return x

    if n > 1:
        return x * power(x, n - 1)


print(power(5, 3))
