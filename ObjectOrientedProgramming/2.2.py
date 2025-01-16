class Square:
    def __init__(self, a):
        self.a = a  # Side length of the square

    def area(self):
        return self.a * self.a  # Calculates the area of the square

    def perimeter(self):
        return 4 * self.a  # Calculates the perimeter of the square

# Create two square objects
square1 = Square(4)
square2 = Square(6)

print('Square with side 4:')
print(f'Area is {square1.area()}, Perimeter is {square1.perimeter()}')

print('Square with side 6:')
print(f'Area is {square2.area()}, Perimeter is {square2.perimeter()}')
