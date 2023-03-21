import turtle


turtle.pensize(5)

turtle.penup()
turtle.pendown()

for i in range(0,500,20):
    turtle.forward(i)
    turtle.left(90)

turtle.done()