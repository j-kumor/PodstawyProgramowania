# Define the 2D array
array = [[-38, 19], [5, 40], [-7, 11], [29, 16]]

# Initialize variables to store the smallest and largest values and their positions
smallest_value = float('inf')
largest_value = float('-inf')
smallest_pos = (-1, -1)
largest_pos = (-1, -1)

# Loop through each element in the array to find the smallest and largest values
for i in range(len(array)):
    for j in range(len(array[i])):
        # Check for smallest value
        if array[i][j] < smallest_value:
            smallest_value = array[i][j]
            smallest_pos = (i, j)
        # Check for largest value
        if array[i][j] > largest_value:
            largest_value = array[i][j]
            largest_pos = (i, j)

print(f"Smallest value: {smallest_value} at row {smallest_pos[0]}, column {smallest_pos[1]}")
print(f"Largest value: {largest_value} at row {largest_pos[0]}, column {largest_pos[1]}")