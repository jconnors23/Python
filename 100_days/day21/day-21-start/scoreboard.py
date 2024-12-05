from turtle import Turtle

# best practice, dont hard code values use constants
ALIGNMENT = 'center'
FONT = ('Verdana', 25, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.goto(x=0, y=230)
        self.write(f"Score {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def update(self):
        self.clear()
        self.score += 1

    def write_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)
