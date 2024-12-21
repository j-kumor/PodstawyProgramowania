def convert_2d_to_1d(array_2d):
    # Flatten the 2D array into a 1D list
    return [element for row in array_2d for element in row]

# First 2D array
array1 = [
    [2, 3],
    [1, 5]
]

# Second 2D array
array2 = [
    [5, 0, 3, 7, 5],
    [9, 0, 9, 1, 2]
]

# Third 2D array
array3 = [
    [2, 1],
    [3, 5],
    [7, 4],
    [2, 6]
]

# Convert and print the results
print("1D array from first 2D array:", convert_2d_to_1d(array1))
print("1D array from second 2D array:", convert_2d_to_1d(array2))
print("1D array from third 2D array:", convert_2d_to_1d(array3))
