import json

with open('dogs.json', 'r', encoding='utf-8') as file:
    dogs = json.load(file)

# Iterate through the list of dogs and print information for dogs younger than 5 years
for dog in dogs:
    if dog["age"] < 5:
        print("Name:", dog["name"])
        print("Breed:", dog["breed"])
        print("Age:", dog["age"])
        print("Weight (kg):", dog["weight_kg"])
        print("Owner:", dog["owner"])
        print("Vaccinated:", dog["vaccinated"])
        print()  # Print a blank line between each dog
