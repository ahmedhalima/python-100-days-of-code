from turtle import Turtle, Screen
import random

shape = Turtle()
shape.speed('fastest')
shape.hideturtle()
screen = Screen()
screen.colormode(255)

colors = [(236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
          (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165),
          (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129),
          (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

def random_color():
    return random.choice(colors)

shape.setheading(225)
shape.penup()
shape.forward(250)
shape.setheading(0)
number_of_dots = 101

for dot_count in range(1, number_of_dots):
    shape.dot(20, random_color())
    shape.forward(50)
    if dot_count % 10 == 0:
        shape.setheading(90)
        shape.forward(50)
        shape.setheading(180)
        shape.forward(500)
        shape.setheading(0)


screen.exitonclick()