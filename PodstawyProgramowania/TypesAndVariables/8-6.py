###
# The program calculates the cost of transporting goods
# based on the given distance in km, fuel price per 1 liter,
# and fuel consumption in liters per 100 km.
#
distance = int(input('Enter distance in km: '))
fuel_price = float(input('Enter fuel price per liter: '))
fuel_consumption = float(input('Enter fuel consumption per 100 km (in liters): '))

total_fuel_consumption = (distance / 100) * fuel_consumption

total_cost = total_fuel_consumption * fuel_price

print(f'Total fuel consumption: {total_fuel_consumption:.2f} liters') #: rozpoczecie formatowania, .2f float z dwoma miejscami
print(f'Total cost of transportation: {total_cost:.2f}')