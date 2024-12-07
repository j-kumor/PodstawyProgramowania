# Program to calculate the parking fee based on the number of hours parked

# Ask the user for the number of hours the car was parked
hours_parked = int(input("Enter the number of hours the car was parked: "))

# Calculate and print the parking fee based on the number of hours
if 1 <= hours_parked <= 2:
    fee = 5
elif 3 <= hours_parked <= 6:
    fee = 15
elif hours_parked > 6:
    fee = 20
else:
    fee = 0  # If the number of hours is less than 1 (invalid case)

# Print the fee
print(f"The parking fee for {hours_parked} hours is: {fee} PLN")