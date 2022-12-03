import turtle

# create a turtle
t = turtle.Turtle()

# move the turtle to the starting position
t.penup()
t.goto(-100, 0)
t.pendown()

# draw the heart shape
t.begin_fill()
t.fillcolor("red")
t.left(140)
t.forward(200)
t.circle(-50, 180)
t.setheading(0)
t.forward(200)
t.circle(-50, 180)
t.end_fill()
