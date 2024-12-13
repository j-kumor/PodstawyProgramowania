def factorial(n):

# 0! = 1, 1! = 1
    if n == 0 or n == 1:
        return 1

# n! = n * (n-1)!
    if n > 1:
        return n * factorial(n-1)


number = int(input('Enter a number: '))
print(f'{number}! = {factorial(number)}')
