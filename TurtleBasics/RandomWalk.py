import turtle
import random
from turtle import Turtle, Screen

timmy_the_turtle=Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("blue","green")
timmy_the_turtle.position()

directions=[0,90,180,270]

is_true=True
while is_true:
    timmy_the_turtle.forward(30)
    timmy_the_turtle.setheading(random.choice(directions))


screen=Screen()
screen.exitonclick()
