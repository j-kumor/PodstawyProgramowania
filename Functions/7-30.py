###
# A function that calculates the sum of all natural numbers between 1 and n
#

def sum_natural(n):
    if n == 1:
        return 1
    else:
        return n + sum_natural(n - 1)


print(sum_natural(10))
