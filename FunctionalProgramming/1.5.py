# Define the average speed function
def avg_speed(distance, hours, minutes):
    # Convert travel time to hours
    total_hours = hours + (minutes / 60)
    # Calculate average speed
    return distance / total_hours

# Take inputs from the user
distance = float(input("Enter distance in km: "))
hours = int(input("Enter number of travel hours: "))
minutes = int(input("Enter number of travel minutes: "))

# Calculate the average speed
average_speed = avg_speed(distance, hours, minutes)

# Display the result
print(f"Average speed: {average_speed:.1f} km/h")
