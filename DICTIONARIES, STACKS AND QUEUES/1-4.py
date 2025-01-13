person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming", "excursions"],
    "married": True,
    "phone": {"landline": "123444321", "mobile": "777888999"}
}

# Display the name
print(f"Name: {person['name']}")

print(f"Hobby: {person['hobby']}")

# Display the entire contents of the dictionary
print("\nOriginal Dictionary:")
for key, value in person.items():
    print(f"{key}: {value}")

# Change surname to 'Nowak'
person["surname"] = "Nowak"

# Change the marriage status
person["married"] = not person["married"]

# Add gender: 'male'
person["gender"] = "male"

# Add a new hobby: 'bicycle'
person["hobby"].append("bicycle")

# Add work phone to existing phones
person["phone"]["work"] = "313131444"

# Display the entire updated dictionary
print("\nUpdated Dictionary:")
for key, value in person.items():
    print(f"{key}: {value}")
