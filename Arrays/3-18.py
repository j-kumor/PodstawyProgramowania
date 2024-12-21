# Import the MyArrays module
import MyArrays

numbers = [7, 3, 8, 5, 2]

print(f"Numbers: {', '.join(map(str, numbers))}")

second_largest = MyArrays.second_largest(numbers)
print(f"Second largest number: {second_largest}")

median_value = MyArrays.median(numbers)
print(f"Median: {median_value}")

smallest_largest_values = MyArrays.smallest_largest(numbers)
print(f"Smallest and largest number: {smallest_largest_values[0]},{smallest_largest_values[1]}")

array_as_string = MyArrays.array_to_string(numbers)
print(f"Numbers as a string: {array_as_string}")