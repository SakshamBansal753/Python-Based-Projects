from turtle import Turtle ,Screen
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score=0
        self.right_score=0
        self.Update_scoreboard()

    def Update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=("Courier ", 60, "normal"))
        self.goto(100, 200)
        self.write(self.right_score, align="center", font=("Courier ", 60, "normal"))

    def lpoint(self):
        self.left_score+=1
        self.Update_scoreboard()

    def rpoint(self):
            self.right_score += 1
            self.Update_scoreboard()
