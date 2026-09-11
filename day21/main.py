from turtle import Screen

from scoreboard import ScoreBoard
from snake import Snake
from food import Food
import time
game_is_on = True

screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen._root.resizable(False, False)
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(fun=snake.up, key='Up')
screen.onkey(fun=snake.down, key='Down')
screen.onkey(fun=snake.left, key='Left')
screen.onkey(fun=snake.right, key='Right')

screen.update()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend(snake.segments[-1].position())
        scoreboard.increase_score()

    # detect collisions with the wall
    if (snake.head.xcor() > 290 or snake.head.xcor() < -290 or
            snake.head.ycor() > 290 or snake.head.ycor() < -290):
        game_is_on = False
        scoreboard.game_over()

    # detect collision with its own tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
