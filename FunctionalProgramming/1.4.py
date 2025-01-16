# Define the anonymous function
ms_to_kmh = lambda ms: ms * 3.6

# Take speed in m/s from the user
speed_ms = float(input("Enter the speed in meters per second (m/s): "))

# Convert to km/h
speed_kmh = ms_to_kmh(speed_ms)

# Display the result
print(f"{speed_ms} m/s = {speed_kmh} km/h")
