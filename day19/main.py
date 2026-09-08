from turtle import Turtle, Screen

shape = Turtle()
screen = Screen()

def move_forward():
    shape.forward(10)

def move_backward():
    shape.backward(10)

def turn_left():
    shape.setheading(shape.heading() + 10)

def turn_right():
    shape.setheading(shape.heading() - 10)

def clear():
    shape.clear()
    shape.penup()
    shape.home()

screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='c', fun=clear)



screen.exitonclick()
