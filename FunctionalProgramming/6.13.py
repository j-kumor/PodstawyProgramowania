import matplotlib.pyplot as plt

# List of medal data
medal_data = [
    {"country": "Denmark", "gold": 2, "silver": 4, "bronze": 6},
    {"country": "Finland", "gold": 5, "silver": 0, "bronze": 4},
    {"country": "USA", "gold": 12, "silver": 5, "bronze": 11},
    {"country": "Peru", "gold": 0, "silver": 1, "bronze": 7}
]

# Use map() to create lists of countries and total medals
countries = list(map(lambda x: x["country"], medal_data))
total_medals = list(map(lambda x: x["gold"] + x["silver"] + x["bronze"], medal_data))

# Create a bar chart
plt.bar(countries, total_medals)

# Add a title and labels for the axes
plt.title('Total Medals Won by Each Country')
plt.xlabel('Countries')
plt.ylabel('Total Medals')

# Display the chart
plt.show()
