from turtle import Turtle

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

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)

    def is_collision_with_wall(self):
        if self.head.xcor() > 280 or self.head.xcor() < -280 or self.head.ycor() > 280 or self.head.ycor() < -280:
            return True
        return False

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self, pos):
        segment = Turtle("square")
        segment.color("White")
        segment.penup()
        segment.goto(pos)
        self.segments.append(segment)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        self.move()

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        self.move()

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        self.move()

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        self.move()
