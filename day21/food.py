from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.penup()
        self.pensize(3)
        # self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(x=random_x, y=random_y)
        self.speed('fastest')