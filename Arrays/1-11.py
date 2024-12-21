# The weather station report
temperatures = [
 3, 7, 1, -2, 6, -4, 5, 1, 2, 3,
 4, -1, 0, 2, -1, -2, 5, -2, 7, 2,
 -1, 4, 1, -4, 2, 3, 6, 7, 5, 7
]

# Number of measurements
measurements = len(temperatures)

# Calculates average temperature
temp_total = 0
for temp in temperatures:
   temp_total += temp
avg_temp = temp_total / measurements

# Calculates min and max temperatures
min_temp = min(temperatures)
max_temp = max(temperatures)

# Calculates number of days with negative temperature
negative_temp = 0
i = 0
while i < measurements:
   if temperatures[i] < 0:
      negative_temp += 1
   i += 1

# Prints out month report
print('TEMPERATURE REPORT')
print('==================')
print('Month: March')
print('Number of measurements:', measurements)
print('Average temperature in the month: {:.2f}'.format(avg_temp))
print('Minimum temperature:', min_temp)
print('Maximum temperature:', max_temp)
print('Number of days with negative temperature:', negative_temp)
