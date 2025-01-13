# Array of dictionaries with country names and populations
countries = [
    {"name": "Poland", "population": 38000000},
    {"name": "Germany", "population": 83000000},
    {"name": "France", "population": 67000000},
    {"name": "Italy", "population": 59000000},
    {"name": "Spain", "population": 47000000},
]

# Print the header
print(f"{'COUNTRY':<10} {'POPULATION':<10}")

# Print the contents of the array
for country in countries:
    print(f"{country['name']:<10} {country['population']:<10}") #<10 szerokosc pola przy wyswietlaniu
