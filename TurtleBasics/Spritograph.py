import turtle
import random
from turtle import Turtle, Screen

timmy_the_turtle=Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("blue","green")
turtle.colormode(255)
timmy_the_turtle.position()
timmy_the_turtle.speed(0)
def random_color():
    r=random.randint(0,255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)

    random_col=(r,b,g)
    return random_col
for i in range(100):

    timmy_the_turtle.circle(90)
    current_heading=timmy_the_turtle.heading()
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.setheading(current_heading+5)




screen=Screen()
screen.exitonclick()
