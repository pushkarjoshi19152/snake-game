from turtle import Screen
from snake import Snake
import food
import time
import scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
ood = food.Food()
points = scoreboard.score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    if ood.distance(snake.head) < 15:
        ood.refresh()
        points.increment_score()
        # increase snake length
        snake.add_segment()
    # detect collisions with wall
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        points.game_over()
        game_is_on = False
    # detect collisions with snake body
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            points.game_over()
            game_is_on= False

    snake.move()

screen.exitonclick()
