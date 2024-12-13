def draw_square(pen, length):
    """Draws a square with the given side length using the specified turtle."""
    for _ in range(4):
        pen.forward(length)
        pen.right(90)

def draw_triangle(pen, length):
    """Draws an isosceles triangle with the given side length."""
    for _ in range(3):
        pen.forward(length)
        pen.left(120)

def draw_rectangle(pen, length_a, length_b):
    """Draws a rectangle with sides length_a and length_b."""
    for _ in range(2):
        pen.forward(length_a)
        pen.right(90)
        pen.forward(length_b)
        pen.right(90)
