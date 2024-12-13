import turtle
from figures import draw_square  # Import the draw_square function

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Side length
side_length = 100

# Draw a square using the draw_square function
draw_square(side_length)

# Finish
window.mainloop()
