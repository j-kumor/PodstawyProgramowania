# Define a 3x5 array with integer values
array = [
    [7, 3, 1, 9, 5],
    [2, 8, 4, 6, 7],
    [9, 5, 0, 3, 2]
]

# Print the original array
print("Original array:")
for row in array:
    print(" ".join(map(str, row)))

# Swap the first and last columns
for row in array:
    row[0], row[4] = row[4], row[0]

# Print the array after swapping the first and last columns
print("\nArray after swapping the first and last columns:")
for row in array:
    print(" ".join(map(str, row)))