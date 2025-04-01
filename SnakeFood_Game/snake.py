X_POS=[0,-20,-40]
MOVE_DIST=20
UP=90
DOWN=270
RIGHT=0
LEFT=180
from turtle import Turtle
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()

    def create_snake(self):
        for pos in X_POS:
             self.add_segment((pos,0))
    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DIST)

    def up(self):
        if self.segments[0].heading()!=DOWN:
            self.segments[0].setheading(UP)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)
    def add_segment(self,position):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)
    def extend(self):
        self.add_segment(self.segments[-1].position())

