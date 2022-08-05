# Let's draw some cool drawins with the package turtle

# import turtle
import turtle

# Let's get a nice set-up in turtle
turtle.bgcolor("white") # Pen color
turtle.pensize(2)
turtle.bgcolor("black")# Backgroud color
turtle.speed(50)

# Draw a square
#turtle.forward(50)
#turtle.left(90)
#turtle.forward(50)
#turtle.left(90)
#turtle.forward(50)
#turtle.left(90)
#turtle.forward(50)
#turtle.left(90)
#turtle.done()

for colours in ("red", "orange", "yellow", "green", "blue", "purple"):
     turtle.color(colours)
     turtle.circle(150)
     turtle.left(10)

for i in range(12):
    for colours in ("red", "orange", "yellow", "green", "blue", "purple"):
        turtle.color(colours)
        turtle.circle(150)
        turtle.left(10)

    for i in range(6):
        for colours in ("red", "orange", "yellow", "green", "blue", "purple"):
            turtle.color(colours)
            turtle.circle(150)
            turtle.left(10)
turtle.done()