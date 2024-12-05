import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
#TODO clear screen end game and play again functionality
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
game_state = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

while game_state:
    screen.update()
    time.sleep(.1)
    snake.move()

    # detect collision w food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update()
        scoreboard.write_score()
    # detect collision w wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_state = False
        snake.over()
        food.over()
        scoreboard.game_over()
    # detect collision w tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_state = False
            snake.over()
            food.over()
            scoreboard.game_over()

screen.exitonclick()
