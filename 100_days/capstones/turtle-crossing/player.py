from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 50
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(name='turtle')
        self.penup()
        self.color('black')
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def game_over(self):
        self.reset()



