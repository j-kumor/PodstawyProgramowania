numbers = [15, 8, 31, 47, 2, 19]

total_sum = 0
index = 0

# Use a while loop to sum the elements in the array
while index < len(numbers):
    total_sum += numbers[index]
    index += 1

mean = total_sum / len(numbers)

print("Array:", numbers)
print("Arithmetic mean:", mean)
