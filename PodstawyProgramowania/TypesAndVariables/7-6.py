#The speed of vehicles on a highway in Poland must be between 40 and 140 km/h. Write a program that checks whether the vehicle speed entered from the keyboard is correct. Sample result:

speed = int(input("Enter vehicle speed (km/h): "))

is_valid = 40 <= speed <= 140 #sprawdza czy jest w dobrym przedziale

print(f"Speed is valid: {is_valid}")