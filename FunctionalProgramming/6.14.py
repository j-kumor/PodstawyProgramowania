# List of bottle fillings
filled_bottles = [508, 500, 512, 499, 492, 511, 503, 476, 501, 509]

# Bottle capacity and tolerance
bottle_capacity = 500
tolerance = 2  # in percentage

# Calculate the allowable tolerance range
lower_limit = bottle_capacity - (bottle_capacity * tolerance / 100)
upper_limit = bottle_capacity + (bottle_capacity * tolerance / 100)

# Use filter() to get the incorrectly filled bottles
incorrectly_filled = list(filter(lambda x: x < lower_limit or x > upper_limit, filled_bottles))

# Calculate the percentage of incorrectly filled bottles
incorrect_percentage = (len(incorrectly_filled) / len(filled_bottles)) * 100

# Display the result
print(f"Bottle capacity:    {bottle_capacity}ml")
print(f"Filling tolerance:  {tolerance}%")
print(f"Filled bottles:     {', '.join(map(str, filled_bottles))}")
print(f"Incorrectly filled: {incorrect_percentage:.0f}%")
