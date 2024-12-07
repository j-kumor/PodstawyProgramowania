# Program to check the user's age group

# Ask the user for their age
age = int(input("Enter your age: "))

# Check which age group they belong to
if age < 13:
    age_group = "Child"
elif 13 <= age <= 19:
    age_group = "Teen"
elif 20 <= age <= 64:
    age_group = "Adult"
else:
    age_group = "Senior"

# Print the result
print(f"You belong to the {age_group} age group.")