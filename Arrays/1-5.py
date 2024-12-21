###
# Prints some array elements
#
arr = [1, 2, 3, 4, 5]

# Print the original array
print('Array:', arr)

# Subtract one from the first element of the array
arr[0] -= 1
print('Array:', arr)

# Increase the last array element by 4
arr[len(arr) - 1] += 4
print('Array:', arr)

# Multiply the middle array element by 2
middle_index = len(arr) // 2
arr[middle_index] *= 2
print('Array:', arr)