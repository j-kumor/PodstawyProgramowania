# Recorded speed values
speeds = [48, 47, 54, 50, 42, 68, 39, 46]

# Filter speeds that are higher than the allowed speed (50 km/h)
high_speeds = list(filter(lambda speed: speed > 50, speeds))

# Display the result
print(f"Recorded values: {', '.join(map(str, speeds))}")
print(f"Speed too high: {', '.join(map(str, high_speeds))}")
