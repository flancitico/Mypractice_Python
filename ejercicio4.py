import turtle

# Configuración de la pantalla
window = turtle.Screen()
window.bgcolor("white")
window.title("Te amo, Sari")

# Configuración de la tortuga
pen = turtle.Turtle()
pen.shape("turtle")
pen.color("red")
pen.speed(0.05)

# Función para dibujar un corazón


def draw_heart():
    pen.begin_fill()
    pen.left(140)
    pen.forward(224)
    for _ in range(200):
        pen.right(1)
        pen.forward(2)
    pen.left(120)
    for _ in range(200):
        pen.right(1)
        pen.forward(2)
    pen.forward(224)
    pen.end_fill()

# Función para escribir un mensaje


def write_message():
    pen.penup()
    pen.goto(0, -50)
    pen.color("black")
    pen.write("Te amo, Sari", align="center", font=("Arial", 24, "normal"))
    pen.hideturtle()


# Dibujar el corazón y escribir el mensaje
draw_heart()
write_message()

# Mantener la ventana abierta
turtle.done()
