from turtle import Turtle, Screen
import random

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r, g, b

shape = Turtle()
screen = Screen()
shape.pensize(15)
screen.colormode(255)

directions = [0, 90, 180, 270]
shape.speed(30)

for i in range(200):
    shape.color(random_color())
    shape.forward(30)
    shape.setheading(random.choice(directions))


screen.exitonclick()
