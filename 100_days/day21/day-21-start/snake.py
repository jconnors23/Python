from turtle import Turtle

# CONSTANTS should be in all caps for classes
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        # reverse order of square segments to move snake
        # starting at last index, stopping at first, stepping back by 1 each time in array
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # desired position coordinates
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            # last -> 2nd to last
            self.segments[seg_num].goto(new_x, new_y)
        # move head of snake
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        # check for direction that snake is facing, cant go up if going down already (onto itself)
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def create_snake(self):
        for coordinates in STARTING_POSITIONS:
            self.add_segment(coordinates)

    def add_segment(self, coordinates):
        t = Turtle('square')
        t.color('white')
        t.penup()
        t.goto(coordinates)
        self.segments.append(t)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def over(self):
        for segment in self.segments:
            segment.clear()
