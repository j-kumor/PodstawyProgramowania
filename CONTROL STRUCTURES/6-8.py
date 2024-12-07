# Checking if both people are adults

# Read the first person's data
person1_name = input('Enter first person name: ')
person1_age = int(input('Enter first person age: '))

# Read the second person's data
person2_name = input('Enter second person name: ')
person2_age = int(input('Enter second person age: '))

# Check if both are adults (age >= 18)
if person1_age >= 18 and person2_age >= 18:
    print(f'Both {person1_name} and {person2_name} are adults.')
else:
    print(f'Either {person1_name} or {person2_name} is not an adult.')