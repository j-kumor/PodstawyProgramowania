# Read time in 24-hour format from the user
time_24 = input("Enter time (24-hour format): ")

# Split the time into hours and minutes
hours, minutes = map(int, time_24.split(":"))

# Determine whether it's AM or PM
if hours >= 12:
    period = "pm"
    if hours > 12:
        hours -= 12  # Convert to 12-hour format for hours greater than 12
else:
    period = "am"
    if hours == 0:
        hours = 12  # Midnight case

# Format and print the time in 12-hour format
print(f"Time in 12-hour format: {hours}:{minutes:02d}{period}")