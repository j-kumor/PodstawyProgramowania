def count_greater_than(arr, value):
    count = 0
    for num in arr:
        if num > value:
            count += 1
    return count

# Example array of real numbers
numbers = [12.5, 1.3, 19.8, 7.8]

value = float(input("Enter a value: "))

result = count_greater_than(numbers, value)

print(f"Number of elements greater than {value}: {result}")
