# Define the anonymous function
initials = lambda name, surname: f"{name[0].upper()}.{surname[0].upper()}."

# Test the function
name = input("Enter your first name: ")
surname = input("Enter your surname: ")

# Get and display the initials
result = initials(name, surname)
print(f"Your initials are: {result}")
