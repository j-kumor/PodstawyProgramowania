# Define the 2D array
array = [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8, 7, 1, 1, 5]
]

# Initialize a variable to hold the sum of the last column
sum_last_column = 0

# Loop through each row of the array and add the value from the last column
for row in array:
    sum_last_column += row[-1]

# Print the result
print("Sum of values in the last column:", sum_last_column)