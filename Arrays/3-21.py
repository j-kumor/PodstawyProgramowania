def is_subset(arr1, arr2):
    for element in arr1:
        if element not in arr2:  # If any element of arr1 is not in arr2, return False
            return False
    return True  # If all elements of arr1 are found in arr2, return True

arr1 = [1, 3, 5]
arr2 = [5, 1, 3, 7, 8]

if is_subset(arr1, arr2):
    print("The first array is a subset of the second one.")
else:
    print("The first array is not a subset of the second one.")
