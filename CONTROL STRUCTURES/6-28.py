# First two Fibonacci numbers
a, b = 0, 1

# Print the first 20 Fibonacci numbers
for _ in range(20):
    print(a, end=' ')
    a, b = b, a + b  # Update a and b to the next two numbers in the sequence
