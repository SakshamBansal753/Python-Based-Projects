from turtle import Turtle
X_COR=-220
Y_COR=0
class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.turtlesize(stretch_len=1 ,stretch_wid=1)
        self.hideturtle()
        self.pensize(12)
        self.penup()
        self.goto(X_COR,Y_COR)
        self.shape("square")
        self.color("White")
        self.horizontal(X_COR,Y_COR)
        self.vertical()
        self.speed(0)

    def horizontal(self, X_COR,Y_COR):
        for y in range(2):
            self.penup()
            self.goto(X_COR,Y_COR)
            self.pendown()
            for i in range(9):
                self.forward(50)
            Y_COR=140
            X_COR=-230


    def vertical(self):
        X=-150
        Y=-190
        self.left(90)
        for x in range(2):
            self.penup()
            self.goto(X,Y)
            self.pendown()
            for i in range(9):
                self.forward(50)
            X=90
            Y=-190






