import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt="Which turtle will win the race? Enter a color:")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []


for index in range(0, 6):
    shape = Turtle(shape='turtle')
    shape.penup()
    shape.color(colors[index])
    shape.goto(x=-230, y=y_positions[index])
    all_turtles.append(shape)

if user_bet:
    race_mode = True

while race_mode:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_mode = False
            winning_turtle = turtle.pencolor()
            if user_bet == winning_turtle:
                print(f'You won, the winning color is {winning_turtle}')
            else:
                print(f'You lost, the winning color is {winning_turtle}')
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
