# Define the anonymous function
is_even = lambda number: number % 2 == 0

# Test the function with user input
number = int(input("Enter a number to check if it's even: "))

# Check if the number is even and display the result
if is_even(number):
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
