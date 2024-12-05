import turtle

import colorgram
# colors = colorgram.extract('image.jpg', 10)
# for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    rgb_colors.append((r, g, b))

import turtle as t
import random as rand
from turtle import Screen
turtle.colormode(255)
j = t.Turtle()

#colors = [(254, 253, 252), (232, 254, 243), (253, 234, 245), (43, 2, 176), (79, 253, 174), (226, 149, 109), (230, 225, 253), (160, 3, 82), (4, 211, 101), (3, 138, 64)]
colors = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
#start from where we want
j.penup()
j.hideturtle()
j.setheading(225)
j.forward(300)
j.setheading(0)
# break statement solves blank spaces problem 
def ten():
    for i in range(10):
        j.dot(20, rand.choice(colors))
        if i == 9:
            break
        j.forward(50)


def dots():
    j.speed('fastest')
    grid = True
    count = 0
    rowcount = 0
    while grid:
        ten()
        j.setheading(90)
        j.forward(50)
        # fine code
        rowcount += 1
        count += 10
        if rowcount % 2 == 0:
            j.setheading(0)
        else:
            j.setheading(180)
        if count == 100:
            grid = False

dots()
screen = Screen()
screen.exitonclick()




















# ran into issue with color gram imports and pip compatibility
# To fix, went to python interpreter settings, ensured
# that the interpreter is the one from c drive installs - > python install location
# consider changing default interpreter for projects
# to fix also ensured that venv files were not excluded from settings and interpreter tab




