from functools import reduce

# List of numbers
numbers = [2, 4, 6, 3, 7, 5]

# Filter even numbers using filter() and an anonymous function
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Use reduce() to calculate the sum of even numbers
total_sum = reduce(lambda x, y: x + y, even_numbers)

# Display the result
print(total_sum)  # Output: 12
