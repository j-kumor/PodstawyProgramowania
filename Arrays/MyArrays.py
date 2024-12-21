# MyArrays.py

# Function to return the second largest element in the array
def second_largest(arr):
    # Sort the array without using built-in functions
    arr_sorted = sorted(arr)
    return arr_sorted[-2]

def diff_largest_smallest(arr):
    return max(arr) - min(arr)

# Function to return the median of numbers in an array
def median(arr):
    arr_sorted = sorted(arr)
    n = len(arr_sorted)
    if n % 2 == 1:
        return arr_sorted[n // 2]
    else:
        # For even number of elements, return the average of the two middle values
        return (arr_sorted[n // 2 - 1] + arr_sorted[n // 2]) / 2

def smallest_largest(arr):
    return [min(arr), max(arr)]

def array_to_string(arr):
    return "-".join(map(str, arr))