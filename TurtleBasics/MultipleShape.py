import turtle
from turtle import Turtle, Screen

timmy_the_turtle=Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("blue","green")
timmy_the_turtle.position()
def draw_shape(num_sides):
    for i in range(num_sides):
        angle=360/num_sides
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)

for i in range(3,11):
    draw_shape(i)


screen=Screen()
screen.exitonclick()
