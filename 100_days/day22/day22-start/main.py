from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

scr = Scoreboard()
s = Screen()
s.tracer(0)
s.setup(width=800, height=600)
s.bgcolor('black')
s.title('Pong')
b = Ball()
lp = Paddle(-350, 0)
rp = Paddle(350, 0)
s.listen()
s.onkey(rp.up, 'Up')
s.onkey(rp.down, 'Down')
s.onkey(lp.up, 'w')
s.onkey(lp.down, 's')

game_state = True
while game_state:
    # make ball move on each refresh
    time.sleep(b.move_speed)
    s.update()
    b.move()
    # wall & paddle collision
    if b.ycor() >= 280 or b.ycor() <= -280:
        b.ybounce()
    if b.distance(rp) < 50 and b.xcor() > 320 or b.distance(lp) < 50 and b.xcor() < -320:
        b.xbounce()
    # out of bounds
    if b.xcor() > 380:
        scr.l_score += 1
        scr.new_score()
        b.reset()
    if b.xcor() < -380:
        scr.r_score += 1
        scr.new_score()
        b.reset()

s.exitonclick()
