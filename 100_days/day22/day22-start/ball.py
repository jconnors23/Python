from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=1.4, stretch_len=1.4)
        self.color('white')
        self.goto(0, 0)
        self.xmove = 10
        self.ymove = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def ybounce(self):
        if self.ycor() > 0:
            self.ymove *= -1
        elif self.ycor() < 0:
            self.ymove *= -1

    def xbounce(self):
        if self.move_speed > 0:
            self.move_speed -= 0.01
        if self.xcor() > 0:
            self.xmove *= -1
        elif self.xcor() < 0:
            self.xmove *= -1

    def reset(self):
        new_x = 0
        new_y = 0
        self.move_speed = 0.1
        self.xmove *= -1
        self.goto(new_x, new_y)

