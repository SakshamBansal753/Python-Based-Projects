import turtle
import random
from turtle import Turtle, Screen

timmy_the_turtle=Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("blue","green")
timmy_the_turtle.position()
colours=["CornflowerBlue","Black","red","green","yellow","pink",'SeaGreen']
directions=[0,90,180,270]


is_true=True
while is_true:
    timmy_the_turtle.forward(30)
    timmy_the_turtle.setheading(random.choice(directions))
    timmy_the_turtle.color(random.choice(colours))

screen=Screen()
screen.exitonclick()
