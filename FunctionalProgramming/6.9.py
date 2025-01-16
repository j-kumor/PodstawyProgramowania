# Dictionary of cities and their temperatures
temperatures = {"Krakow": 7, "Warszawa": -2, "Sopot": 4, "Koszalin": -1, "Opole": 3}

# Use filter() and lambda function to get cities with positive temperatures
cities_with_positive_temps = list(filter(lambda city: temperatures[city] > 0, temperatures))

# Display the result
print("Cities with positive temperatures:", " ".join(cities_with_positive_temps))
