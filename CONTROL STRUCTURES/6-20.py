# Read decimal number from the user
decimal_number = int(input("Enter decimal number: "))

# Initialize an empty list to store the remainders
remainders = []

# Convert the decimal number to binary
while decimal_number > 0:
    remainder = decimal_number % 2  # Get remainder when divided by 2
    remainders.append(remainder)  # Store the remainder
    decimal_number = decimal_number // 2  # Integer division by 2

# Reverse the list to get the binary number in correct order
binary_number = ''.join(str(x) for x in remainders[::-1])

# Print the result
print(f"Decimal number in binary: {binary_number} (2)")