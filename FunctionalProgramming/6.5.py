# List of numbers from 1 to 20
numbers = list(range(1, 21))

# Use filter() and lambda function to get numbers divisible by both 2 and 3
divisible_by_2_and_3 = list(filter(lambda x: x % 2 == 0 and x % 3 == 0, numbers))

# Display the result
print(divisible_by_2_and_3)
