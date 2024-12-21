# Function to separate even and odd numbers in an array
def separate_even_odd(arr):
    # Lists to store even and odd numbers
    even_numbers = []
    odd_numbers = []
    
    # separate even and odd numbers
    for num in arr:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    
    
    return even_numbers + odd_numbers

arr = [7, 9, 2, 4, 5, 6]

arr = separate_even_odd(arr)

print("arr =", arr)
