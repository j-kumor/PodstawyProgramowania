# Create a 5x5 array initialized to zeros
array = [[0 for _ in range(5)] for _ in range(5)]

# Modify the array to create a multiplication table
for i in range(5):
    for j in range(5):
        array[i][j] = (i + 1) * (j + 1)

# Print the multiplication table
for row in array:
    print(" ".join(map(str, row)))