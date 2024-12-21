numbers = [34, 7, 19, 4, 21, 8]

even_count = 0
i = 0

while i < len(numbers):
    if numbers[i] % 2 == 0:
        even_count += 1  
    i += 1  

print("Number of even numbers:", even_count)
