class C:
    def __init__(self, points):
        self.points = points  # List of points (each point is a list of [x, y] coordinates)

    def m(self, n):
        # Count how many points are in the first quadrant (both x and y > 0)
        count = 0
        for point in self.points:
            if point[0] > 0 and point[1] > 0:
                count += 1
        
        # Return True if at least 'n' points are in the first quadrant
        return count >= n

# Sample usage
obj = C([[2, 3], [1, 8], [-6, 4], [3, -7]])

# Test cases
print(obj.m(2))  # Expected: True
print(obj.m(3))  # Expected: False
