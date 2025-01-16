###
# Calculates arithmetic mean of two integer numbers
#
def mean(x, y):
    return (x + y) / 2

# takes two numbers from the keyboard
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

# calculates arithmetic mean and prints result
result = mean(n1, n2)
print(f'The arithmetic mean of the numbers {n1} and {n2} is {result}')
