from turtle import Turtle
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self, x):
        super().__init__()
        self.count = x
        self.title = f"Level: {self.count}"
        self.color('black')
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.write(self.title, align='left', font=FONT)

    def level_up(self):
        self.clear()
        self.title = f"Level: {self.count}"
        self.write(self.title, align='left', font=FONT)

    def game_over(self):
        self.clear()
        self.title = 'Game Over'
        self.goto(0, 0)
        self.write(self.title, align='center', font=FONT)
