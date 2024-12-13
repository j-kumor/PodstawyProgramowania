###
# Calculates the area of a triangle based on the lengths
#
import math


def triangle_area(a, b, c):
    if a > 0 and b > 0 and c > 0:
        s = 0.5*(a + b + c)
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area
    else:
        return "Length of sides is incorrect"


print(triangle_area(3, 4, 5))
print(triangle_area(5, 12, 13))
print(triangle_area(7, 24, 25))
