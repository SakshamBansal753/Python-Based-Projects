FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-270,260)
        self.write(f"Level:{self.level}",align="left",font=FONT)

    def increase(self):
        self.level+=1
        self.clear()
        self.write(f"Level:{self.level}",align="left",font=FONT)
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER Your SCORE IS {self.level}",align="center",font=FONT)
