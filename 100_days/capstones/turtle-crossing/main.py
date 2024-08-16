import time
import random as r
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# todo car speeds enchancements

lvl = 1
s = Screen()
s.setup(width=600, height=600)
s.tracer(0)
scr = Scoreboard(1)
cars = []
selected_cars = []
p = Player()
s.listen()
s.onkey(p.up, 'Up')

for i in range(10):
    c = CarManager()
    cars.append(c)

game = True

while game:

    time.sleep(0.1)
    s.update()
    selected_cars.append(r.choice(cars))

    if p.ycor() >= 300:
        lvl += 1
        p.goto(0, -280)
        scr.clear()
        scr = Scoreboard(lvl)
        for car in selected_cars:
            car.clear()
            car.hideturtle()
        selected_cars = []
        cars = []
        for i in range(10):
            c = CarManager()
            for level in range(scr.count):
                c.increase_speed()
            cars.append(c)

    for car in selected_cars:
        if car.distance(p) <= 20:
            for vehicle in selected_cars:
                vehicle.reset()
            p.game_over()
            scr.game_over()
            game = False
        car.going(car.move_distance)


s.exitonclick()
