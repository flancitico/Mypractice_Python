import turtle

turtle.showturtle()
turtle.fillcolor('red')
turtle.begin_fill()
for i in range(8):
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(45)
    turtle.forward(50)
turtle.end_fill()
turtle.done()  # Esta línea hace que la ventana de Turtle permanezca abierta
