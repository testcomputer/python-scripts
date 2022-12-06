import turtle

# create a turtle
my_turtle = turtle.Turtle()

# set the speed of the turtle
my_turtle.speed(10)

# set the starting position of the turtle
my_turtle.penup()
my_turtle.setpos(0, 0)
my_turtle.pendown()

# create a loop to draw the spiral
for i in range(200):
    my_turtle.forward(i * 2)
    my_turtle.right(90)

# keep the window open until the user closes it
turtle.mainloop()
