# Get the number from the user
number = int(input("Enter number: "))

# Loop through numbers 1 to 10 and print the multiplication table
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")