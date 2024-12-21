# Open the file and read the data
with open('countries.txt', 'r') as file:
    countries = []
    for line in file:
        # Strip whitespace and split by comma
        parts = line.strip().split(',')
        if len(parts) == 3:
            country, capital, population = parts
            countries.append((country, capital, int(population)))

# Print the numbered list of countries
for index, (country, capital, population) in enumerate(countries, start=1):
    print(f"{index}. {country}, {capital}, {population}")