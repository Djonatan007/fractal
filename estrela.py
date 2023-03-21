import turtle

cor = ['red', 'blue', 'green', 'purple', 'black']

turtle.pensize(15)

turtle.penup()
turtle.pendown()

for i in range(5):
    turtle.pencolor(cor[i])
    turtle.forward(200)
    turtle.right(144)

turtle.done()