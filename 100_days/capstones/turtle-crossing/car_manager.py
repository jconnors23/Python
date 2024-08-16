from turtle import Turtle
import random as r

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = .75
MOVE_SPEEDS = [1, 1.25, 1.5, 1.75, 2]

# can use probability to create cars at defined rate
class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.move_distance = None
        self.creation()

    def going(self, distance):
        if self.xcor() < -350:
            self.creation()
        self.forward(distance)

    def creation(self):
        starting_y = r.randint(-250, 250)
        self.penup()
        self.color(r.choice(COLORS))
        self.goto(350, starting_y)
        self.setheading(180)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.shape(name='square')
        self.move_distance = r.choice(MOVE_SPEEDS)

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT
