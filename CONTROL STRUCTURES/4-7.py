# Calculates the sum of even numbers in the range <1,10>

sum = 0

for i in range(1, 11):  # This generates numbers from 1 to 10 (inclusive)
    if i % 2 != 0:  # Check if the number is not even
        continue  # Skip odd numbers
    sum += i  # Add even number to sum

print(f'Sum of even numbers in the range <1,10> is {sum}')