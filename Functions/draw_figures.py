import turtle
from figures import draw_square, draw_triangle, draw_rectangle

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)

# Draw figures
# Draw the first square
pen.penup()
pen.goto(-200, 200)
pen.pendown()
draw_square(pen, 100)

# Draw the second square
pen.penup()
pen.goto(100, 200)
pen.pendown()
draw_square(pen, 100)

# Draw the first triangle
pen.penup()
pen.goto(-200, 50)
pen.pendown()
draw_triangle(pen, 100)

# Draw the second triangle
pen.penup()
pen.goto(100, 50)
pen.pendown()
draw_triangle(pen, 100)

# Draw the first rectangle
pen.penup()
pen.goto(-200, -150)
pen.pendown()
draw_rectangle(pen, 150, 100)

# Draw the second rectangle
pen.penup()
pen.goto(100, -150)
pen.pendown()
draw_rectangle(pen, 150, 100)

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()
