# Define the 2x4 two-dimensional array
array = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]

# Loop through the rows of the array
for row in array:
    # Print each row of the array
    print(" ".join(map(str, row)))