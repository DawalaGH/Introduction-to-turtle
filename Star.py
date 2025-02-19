import turtle

# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("Aqua")

# Create a new turtle object
star = turtle.Turtle()

# Draw a star
for i in range(5):
    star.forward(100)
    star.right(144)

# Keep the window open
turtle.done()
