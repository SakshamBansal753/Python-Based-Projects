from turtle import Turtle,Screen

tim=Turtle()
screen=Screen()
def move_for():
    tim.forward(10)
def move_back():
    tim.back(10)
def move_left():
    tim.left(10)
def move_right():
    tim.right(10)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
screen.listen()
screen.onkey(key="w",fun=move_for)
screen.onkey(move_back,"s")
screen.onkey(move_left,"a")
screen.onkey(move_right,"d")
screen.onkey(clear,"c")
screen.exitonclick()
