import turtle
import random
from turtle import Turtle, Screen

timmy_the_turtle=Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("blue","green")
turtle.colormode(255)
def random_color():
    r=random.randint(0,255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)

    random_col=(r,b,g)
    return random_col

timmy_the_turtle.position()

directions=[0,90,180,270]
timmy_the_turtle.pensize(15)
timmy_the_turtle.speed(0)

is_true=True
while is_true:
    timmy_the_turtle.forward(30)
    timmy_the_turtle.setheading(random.choice(directions))
    timmy_the_turtle.color(random_color())


screen=Screen()
screen.exitonclick()
