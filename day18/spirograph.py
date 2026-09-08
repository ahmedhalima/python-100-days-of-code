from turtle import Turtle, Screen
import random

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r, g, b

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        shape.circle(100)
        shape.color(random_color())
        shape.setheading(shape.heading() + size_of_gap)

shape = Turtle()
screen = Screen()
screen.colormode(255)
shape.pensize(2)
shape.speed('fastest')

draw_spirograph(5)

screen.exitonclick()