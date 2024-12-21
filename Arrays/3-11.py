def bubblesort(array):
    n = len(array)
    
    # Traverse through all elements of the array
    for i in range(n):
        swapped = False # Flag to check if any swap is made in this pass
        
        # Last i elements are already sorted, so don't need to check them
        for j in range(0, n-i-1):
            # Compare adjacent elements
            if array[j] > array[j+1]:
                # Swap if the element is greater than the next element
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        
        # If no two elements were swapped in the inner loop, the array is sorted
        if not swapped:
            break

    return array

array1 = [5, 3, 8, 4, 2]
array2 = [12, 45, 2, 8, 23, 1]
array3 = [7, 9, 1, 5, 6, 3]

sorted_array1 = bubblesort(array1)
sorted_array2 = bubblesort(array2)
sorted_array3 = bubblesort(array3)

print("Sorted array 1:", sorted_array1)
print("Sorted array 2:", sorted_array2)
print("Sorted array 3:", sorted_array3)
