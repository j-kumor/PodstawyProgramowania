numbers = [-15, 8, -31, 47, -2, 19]

# Start by assuming the first element is both the maximum and minimum
max_num = numbers[0]
min_num = numbers[0]

# Iterate through the array and update the max and min values as needed
for num in numbers:
    if num > max_num:
        max_num = num  # Update max_num if a larger number is found
    if num < min_num:
        min_num = num  # Update min_num if a smaller number is found

print("Maximum number:", max_num)
print("Minimum number:", min_num)
