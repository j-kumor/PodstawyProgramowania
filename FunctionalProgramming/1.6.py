# Define the anonymous function for average speed calculation
avg_speed = lambda distance, hours, minutes: distance / (hours + minutes / 60)

# Take inputs from the user
distance = float(input("Enter distance in km: "))
hours = int(input("Enter number of travel hours: "))
minutes = int(input("Enter number of travel minutes: "))

# Calculate the average speed using the lambda function
average_speed = avg_speed(distance, hours, minutes)

# Display the result
print(f"Average speed: {average_speed:.1f} km/h")
