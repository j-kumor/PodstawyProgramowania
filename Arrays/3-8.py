# Define the function star that returns a string of n asterisks
def star(n):
    return '*' * n

numbers = [2, 6, 4, 9, 7]

for num in numbers:
    print(f"{num}: {star(num)}")
