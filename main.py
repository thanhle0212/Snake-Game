from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
sc = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 25:
        food.refresh()
        snake.extend()
        sc.increase_score()

    # Detect collision with wall
    if snake.is_collision_with_wall():
        game_is_on = False
        sc.game_over()

    for s in snake.segments[1:]:
        if snake.head.distance(s) < 10:
            game_is_on = False
            sc.game_over()

screen.exitonclick()
