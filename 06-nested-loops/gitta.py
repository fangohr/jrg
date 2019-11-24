import turtle 

gitta = turtle.Turtle()

# Pixel Abstand von Punkt zu Punkt
dot_distance = 25

# wieviele Spalten und Reihen
width = 5
height = 7

gitta.penup()

for y in range(height):
    for i in range(width):
        gitta.dot()
        gitta.forward(dot_distance)
    gitta.backward(dot_distance * width)
    gitta.right(90)
    gitta.forward(dot_distance)
    gitta.left(90)

turtle.done()
turtle.bye()
