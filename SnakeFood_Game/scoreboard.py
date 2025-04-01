from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0, y=250)
        self.hideturtle()
        self.write(f"Score :{self.score} ",align="center",font=("Courier",24,"normal"))


    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score :{self.score} ", align="center", font=("Courier", 24, "normal"))


    def stop(self):
        self.goto(0,0)
        self.write(f"Game Over \n Your Final Score {self.score} ",align="center",font=("Courier",24,"normal"))