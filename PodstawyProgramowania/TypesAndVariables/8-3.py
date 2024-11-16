###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

# Read temperature in Celsius from the keyboard
celsius = float(input("Enter temperature in Celsius: "))

# Calculate temperature in Kelvin
kelvin = celsius + 273.15

# Calculate temperature in Fahrenheit
fahrenheit = celsius * 9/5 + 32

# Print the results
print(f"Temperature in Celsius: {celsius}°C")

print(f"Temperature in Kelvin: {kelvin} K")

print(f"Temperature in Fahrenheit: {fahrenheit}°F")