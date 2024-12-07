# Program that checks if a name is a female name (ending with 'a')

name = input("Enter name: ")

# Check if the name ends with 'a' (case insensitive)
if name.endswith('a'):
    print(f"{name} -- Polish female name")
else:
    print(f"{name} -- Not a Polish female name")