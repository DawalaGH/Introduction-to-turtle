import turtle
turtle.Screen().bgcolor("lightblue")
turtle.Screen().setup(400,300)
polygon=turtle.Turtle()
num_sides=5
len_sides=100
angle=360/num_sides
for i in range(num_sides):
    polygon.forward(len_sides)
    polygon.right(angle)
turtle.done()