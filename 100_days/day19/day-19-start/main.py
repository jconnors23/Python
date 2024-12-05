from turtle import Turtle, Screen

# higher order function = function that can work with other functions as inputs / parameters
# seperate, independent objects = instances of class
# seperate versions of same object (instances) acting in different ways (diff states)



t = Turtle()
screen = Screen()
screen.listen()


def move_forwards():
    t.forward(10)


def move_backwards():
    t.backward(10)


def move_counter_clockwise():
    t.right(10)


def move_clockwise():
    t.left(10)


def clear():
    t.home()
    t.clear()


screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=move_counter_clockwise)
screen.onkey(key='d', fun=move_clockwise)
screen.onkey(key='c', fun=clear)
screen.exitonclick()
