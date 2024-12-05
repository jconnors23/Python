from turtle import Turtle, Screen
import random as r

# keyword arguments = name args of fun


screen = Screen()
screen.setup(500, 400)
colors = ['red', 'blue', 'yellow', 'green', 'purple', 'pink']
turtles = []


def create_turtle(count):
    x_start = -230
    y_start = -100
    for c in colors:
        t = Turtle(shape='turtle')
        t.color(c)
        t.penup()
        t.goto(x=x_start, y=y_start)
        y_start += 50
        turtles.append(t)


create_turtle(6)
user_bet = screen.textinput(title='make bet', prompt='which turtle will win, enter a color:')
is_race = True

while is_race:
    for t in turtles:
        if t.xcor() > 230:
            winner = t.pencolor()
            if user_bet == winner:
                print(f"winning turtle was {winner}, your bet hit")
            else:
                print(f"winning turtle was {winner}, your bet didnt hit")
            is_race = False
            continue
        t.forward(r.randint(0, 10))


screen.exitonclick()
