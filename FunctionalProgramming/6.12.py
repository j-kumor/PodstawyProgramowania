# List of medal data
medal_data = [
    {"country": "Denmark", "gold": 2, "silver": 4, "bronze": 6},
    {"country": "Finland", "gold": 5, "silver": 0, "bronze": 4},
    {"country": "USA", "gold": 12, "silver": 5, "bronze": 11},
    {"country": "Peru", "gold": 0, "silver": 1, "bronze": 7}
]

# Use filter() and lambda function to get countries with at least 10 medals
countries_with_10_or_more = list(filter(lambda data: data["gold"] + data["silver"] + data["bronze"] >= 10, medal_data))

# Display the result
print("COUNTRIES WITH AT LEAST 10 MEDALS")
for country in countries_with_10_or_more:
    print(f"{country['country']}: {country['gold']},{country['silver']},{country['bronze']}")
