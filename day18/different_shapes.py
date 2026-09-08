from turtle import Turtle, Screen
import random

shape = Turtle()
shape.pensize(3)
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angel = 360 / num_sides
    for _ in range(num_sides):
        shape.forward(100)
        shape.right(angel)

for i in range(3, 11):
    shape.color(random.choice(colours))
    draw_shape(i)

screen = Screen()
screen.exitonclick()