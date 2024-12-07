# Define speed limits
speed_limit_min = 40  # Minimum allowed speed (km/h)
speed_limit_max = 140  # Maximum allowed speed (km/h)

# Read the car speed from the user
car_speed = int(input("Enter car speed: "))

# Check if the car speed is within the valid range
if car_speed < speed_limit_min or car_speed > speed_limit_max:
    print("Warning: invalid car speed!!")
else:
    print("Car speed is within the valid range.")