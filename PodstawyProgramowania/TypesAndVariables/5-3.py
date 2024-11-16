#zadanie 5.3

###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))

surface_area = 2 * (a * b + b * c + a * c)

print(f'Objetosc prostopadloscianu wynosi {a*b*c}.')
print(f'Pole powierzchni prostopadloscianu wynosi {surface_area}.')