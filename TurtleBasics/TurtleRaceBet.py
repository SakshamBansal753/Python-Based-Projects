from turtle import Turtle,Screen
import random

is_race=False
tim=Turtle()
screen =Screen()
screen.setup(600,600)
tim.color("black")
tim.pensize(23)
tim.penup()
tim.goto(230,230)
tim.pendown()
tim.goto(230,-230)
tim.speed(0)

user_input=screen.textinput(title="Make Your Bet",prompt="Which will win enter colour")
colors=["Violet","orange","Blue","Green","Yellow","red"]
y_pos=[-70,-40,-10,20,50,80]
all_turtles=[]
for turtle_index in range(0,6):
    timmy = Turtle()
    timmy.shape("turtle")
    timmy.penup()
    timmy.color(colors[turtle_index])

    timmy.goto(x=-200,y=y_pos[turtle_index])

    all_turtles.append(timmy)
if user_input:
    is_race=True
while is_race:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race = False
            win=turtle.pencolor()
            if win==user_input:
                print(f"You Won the winner is{win}")
            else:
                print(f"You Lost To the winner is{win}")

        turtle.forward(random.randint(0,6))





screen.exitonclick()
