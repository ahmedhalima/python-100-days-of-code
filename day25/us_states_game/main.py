import turtle
from turtle import Turtle, Screen
import pandas

STATES_COUNT = 50
right_answers = 0
guessed_states = []

screen = Screen()
screen.setup(width=725, height=491)
screen._root.resizable(False, False)
screen.title('US states Game')

image_name = 'blank_states_img.gif'
screen.addshape(image_name)
turtle.shape(image_name)

while right_answers < STATES_COUNT:
    user_answer = screen.textinput(title=f"{right_answers}/50 States Guessed", prompt="What's another state name?")
    csv_file = pandas.read_csv('50_states.csv')
    if user_answer:
        if user_answer.lower() == 'exit':
            break
        result_exists = csv_file[csv_file['state'].str.lower() == user_answer.lower()]
        if len(result_exists) > 0:
            # check if already guesses
            exists = False
            for state in guessed_states:
                if state[0] == result_exists['state'].item():
                    exists = True
                    break
            if exists:
                continue

            found_state = [
                result_exists['state'].item(), result_exists['x'].item(), result_exists['y'].item()
            ]
            guessed_states.append(found_state)
            right_answers += 1
            turtle_n = Turtle()
            turtle_n.hideturtle()
            turtle_n.penup()
            turtle_n.goto(result_exists['x'].item(), int(result_exists['y'].item()))
            turtle_n.write(result_exists['state'].item())
screen.mainloop()

