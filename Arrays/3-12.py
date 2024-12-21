def find_unique_elements(array):
   
    frequency = {} # store the frequency of each element
    
    for element in array:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1
    
    unique_elements = [element for element, count in frequency.items() if count == 1]
    
    return unique_elements

array = [2, 3, 2, 5, 8, 1, 9, 8]

unique_elements = find_unique_elements(array)

print("Array:", ' '.join(map(str, array)))
print("Unique elements:", ' '.join(map(str, unique_elements)))
