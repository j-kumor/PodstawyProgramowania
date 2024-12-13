import turtle
import figures

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

pen = turtle.Turtle()
pen.speed(5)


def move_turtle(x, y):
    pen.penup()
    pen.setx(x)
    pen.sety(y)
    pen.pendown()


move_turtle(-200, 100)  # First location
figures.draw_square(pen, 100)

move_turtle(100,300)
figures.draw_square(pen, 100)

move_turtle(200, 200)
figures.draw_trangle(pen, 100)

move_turtle(-200, -200)
figures.draw_trangle(pen, 100)

move_turtle(200, -200)
figures.draw_rectangle(pen, 40, 100)

move_turtle(-100, 200)
figures.draw_rectangle(pen, 40, 100)

# keep the window open
pen.hideturtle()
window.mainloop()