import turtle
import random
import colorgram
from turtle import Turtle, Screen

timmy_the_turtle=Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("blue","green")
turtle.colormode(255)
timmy_the_turtle.position()
timmy_the_turtle.speed(0)
timmy_the_turtle.penup()
timmy_the_turtle.setpos(-200, -200)
colors=colorgram.extract('image.jpeg',30)
rgb_colors=[]
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    new_color=(r,g,b)
    rgb_colors.append(new_color)
x=-200
y=-200

for yat in range(10):
    for xat in  range(10):

        timmy_the_turtle.pendown()
        timmy_the_turtle.dot(20,random.choice(rgb_colors))
        timmy_the_turtle.penup()
        timmy_the_turtle.setpos(x,y)
        x+=50
    y+=50
    x=-200



screen=Screen()
screen.exitonclick()
