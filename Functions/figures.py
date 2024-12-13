import turtle

def draw_square(pen, length):
    """Draws a square with the given side length."""
    for _ in range(4):
        pen.forward(length)
        pen.right(90)

def draw_triangle(pen, length):
    """Draws an isosceles triangle with the given base length."""
    for _ in range(3):
        pen.forward(length)
        pen.left(120)

def draw_rectangle(pen, length_a, length_b):
    """Draws a rectangle with the given side lengths."""
    for _ in range(2):
        pen.forward(length_a)
        pen.right(90)
        pen.forward(length_b)
        pen.right(90)

# Main program
if __name__ == "__main__":
    # Set up the screen
    window = turtle.Screen()
    window.bgcolor("lightgreen")

    # Create the turtle
    pen = turtle.Turtle()
    pen.speed(5)

    # Draw figures

    # Draw two squares in different locations
    pen.penup()
    pen.goto(-200, 200)
    pen.pendown()
    draw_square(pen, 100)

    pen.penup()
    pen.goto(100, 200)
    pen.pendown()
    draw_square(pen, 100)

    # Draw two triangles in different locations
    pen.penup()
    pen.goto(-200, 50)
    pen.pendown()
    draw_triangle(pen, 100)

    pen.penup()
    pen.goto(100, 50)
    pen.pendown()
    draw_triangle(pen, 100)

    # Draw two rectangles in different locations
    pen.penup()
    pen.goto(-200, -150)
    pen.pendown()
    draw_rectangle(pen, 120, 60)

    pen.penup()
    pen.goto(100, -150)
    pen.pendown()
    draw_rectangle(pen, 120, 60)

    # Hide the turtle and finish
    pen.hideturtle()
    window.mainloop()