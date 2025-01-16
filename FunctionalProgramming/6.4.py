# List of numbers from 1 to 20
numbers = list(range(1, 21))

# Use map() and lambda function to calculate the third power of each number
third_powers = list(map(lambda x: x ** 3, numbers))

# Display the result
print(third_powers)
