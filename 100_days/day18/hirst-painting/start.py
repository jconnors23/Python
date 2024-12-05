import math
import random as r
import turtle as t
from turtle import Screen
#tkinter - gui under the hood 
t.colormode(255)
jim = t.Turtle()
directions = [0, 90, 180, 270]
jim.shape('turtle')

# select random color
def random_color():
    red = r.randint(0, 255)
    green = r.randint(0, 255)
    blue = r.randint(0, 255)
    combo = (red, green, blue) #stone carved
    return combo

# draw square
# for i in range (4):
#     jim.forward(100)
#     jim.right(90)
#
# dashed line
# for i in range (10):
#     jim.forward(10)
#     jim.penup()
#     jim.forward(10)
#     jim.pendown()

# draw several shapes

def shapes(sides):
    for i in range(sides):
        jim.forward(100)
        jim.right(360 / sides)

def random_walk():
    for i in range (150):
        jim.pencolor(random_color())
        jim.pensize(15)
        jim.speed('fastest')
        jim.forward(30)
        jim.setheading(r.choice(directions))

def draw_circles(gap):
    jim.speed('fastest')
    for i in range(int(360 / gap)):
        jim.color(random_color())
        jim.circle(100)
        jim.setheading((jim.heading() + gap))


screen = Screen()
# shapes(3)
# shapes(4)
# shapes(5)
#random_walk()
draw_circles(5)
screen.exitonclick()