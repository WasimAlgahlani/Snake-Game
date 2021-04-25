from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=500, height=500)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 13:
        score_board.track()
        food.refresh()
        snake.extend_body()
    if snake.head.xcor() > 230 or snake.head.xcor() < -230 or snake.head.ycor() > 230 or snake.head.ycor() < -230:
        score_board.reset_score()
        snake.reset_snake()
    for body in snake.snake_body[1:]:
        if snake.head.distance(body) < 8:
            score_board.reset_score()
            snake.reset_snake()

screen.exitonclick()
