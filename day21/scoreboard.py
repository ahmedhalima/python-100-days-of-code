from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')

class ScoreBoard(Turtle):
    score = 0

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.goto(0, 260)
        self.write_score()
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def write_score(self):
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)