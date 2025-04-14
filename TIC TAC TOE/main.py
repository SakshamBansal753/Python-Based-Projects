from turtle import Screen, Turtle
from Board import Board
from move import Win
import time


screen = Screen()
screen.bgcolor("black")
screen.title("TIC TAC TOE")
screen.tracer(0)
board = Board()
screen.update()
time.sleep(0.1)
game = Win()


current_player = ["X"]

def draw_move(x, y):
    row = get_row(y)
    col = get_col(x)
    if row is not None and col is not None:
        if game.Move(row,col,current_player[0]):
            draw_symbol(row,col,current_player[0])
            if game.check_win(current_player[0]):
                announcer(current_player[0])
                screen.onclick(None)
            else:
                if current_player[0]=="X":
                    current_player[0]="O"
                else:
                    current_player[0]="X"


def get_row(y):
    if 120 < y <= 240:
        return 0
    if 0 < y <= 120:
        return 1
    if -120 <= y <= 0:
        return 2
    return None

def get_col(x):
    if -220 <= x < -100:
        return 0
    if -100 <= x < 20:
        return 1
    if 20 <= x <= 140:
        return 2
    return None
def draw_symbol(x,y,player):

        draw=Turtle()
        draw.hideturtle()
        draw.penup()
        draw.color("White")
        draw.goto(-190 + y * 170 ,140 - x * 120   )
        draw.write(player,align="center", font=("Arial", 40, "bold"))
def announcer(player):
    ann=Turtle()
    ann.hideturtle()
    ann.penup()
    ann.color("Yellow")
    ann.goto(-50,250)
    ann.write(f"{player} Won The Match Congratulations",align="center",font=("Arial", 20, "bold"))

screen.onclick(draw_move)
screen.listen()
screen.mainloop()