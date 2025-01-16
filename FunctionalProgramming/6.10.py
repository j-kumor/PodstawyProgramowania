import matplotlib.pyplot as plt

# Dictionary of cities and their temperatures
temperatures = {"Krakow": 7, "Warszawa": -2, "Sopot": 4, "Koszalin": -1, "Opole": 3}

# Use map() to create lists of cities and their temperatures
cities = list(map(lambda x: x, temperatures.keys()))
temps = list(map(lambda x: temperatures[x], temperatures.keys()))

# Create a bar chart
plt.bar(cities, temps)

# Add a title and labels for the axes
plt.title('Temperatures Recorded in Cities')
plt.xlabel('Cities')
plt.ylabel('Temperature (°C)')

# Display the chart
plt.show()
