from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Using reduce with an anonymous function (lambda) to sum the numbers
result = reduce(lambda x, y: x + y, numbers)

# Display the result
print(result)  # Output: 15
