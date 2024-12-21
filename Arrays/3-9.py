def compare(array1, array2):
    if len(array1) != len(array2):
        return False
    
    # Compare each corresponding element
    for i in range(len(array1)):
        if array1[i] != array2[i]:
            return False
    
    # If all checks pass, the arrays are the same
    return True

array1_1 = ["water", "book", "sky"]
array2_1 = ["water", "book", "sky"]

array1_2 = [True, False]
array2_2 = [True, False, True]

array1_3 = [5, 3, 1]
array2_3 = [5, 3, 1]

array1_4 = [3, 2, 1]
array2_4 = [3, 2]

arrays_to_compare = [
    (array1_1, array2_1),
    (array1_2, array2_2),
    (array1_3, array2_3),
    (array1_4, array2_4)
]

for array1, array2 in arrays_to_compare:
    print(f"Array1: {' '.join(map(str, array1))}")
    print(f"Array2: {' '.join(map(str, array2))}")
    
    if compare(array1, array2):
        print("Comparison: arrays are the same")
    else:
        print("Comparison: arrays are not the same")
    print()  
