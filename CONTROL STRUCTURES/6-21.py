# Read the amount in PLN from the user
amount = int(input("Enter the amount in PLN: "))

# Initialize the count of each type of coin
coins_5 = amount // 5  # Number of 5 PLN coins
remaining_amount = amount % 5  # Remaining amount after using 5 PLN coins

coins_2 = remaining_amount // 2  # Number of 2 PLN coins
remaining_amount = remaining_amount % 2  # Remaining amount after using 2 PLN coins

coins_1 = remaining_amount  # Number of 1 PLN coins (the remainder)

# Display the result
print(f"The amount of PLN {amount} in coins:")
print(f"5 PLN coins: {coins_5}")
print(f"2 PLN coins: {coins_2}")
print(f"1 PLN coins: {coins_1}")
