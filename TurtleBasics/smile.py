import turtle
from turtle import Turtle, Screen

timmy_the_turtle=Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("blue","green")
timmy_the_turtle.position()
timmy_the_turtle.circle(150)
timmy_the_turtle.teleport(-100)
timmy_the_turtle.teleport(y=170)
timmy_the_turtle.teleport(-80)
timmy_the_turtle.circle(30)
timmy_the_turtle.circle(10)
timmy_the_turtle.teleport(80)
timmy_the_turtle.circle(30)
timmy_the_turtle.circle(10)
turtle.penup()
turtle.goto(-40, 110)
turtle.pendown()
turtle.width(5)
turtle.setheading(-60)
turtle.circle(40, 120)


screen=Screen()
screen.exitonclick()
