
import turtle

def draw_square(length):
    # Create the turtle
    pen = turtle.Turtle()
    pen.speed(5)

    # Draw the square
    for i in range(4):
        pen.forward(length)
        pen.right(90)

    # Hide the turtle
    pen.hideturtle()
