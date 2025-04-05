from turtle import Turtle ,Screen
from paddle import Paddle
from ball import Ball
from Scoreboard import Scoreboard
import time
screen=Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=800,height=600)
screen.tracer(0)
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(r_paddle.move_upward,"Up")
screen.onkey(r_paddle.move_down,"Down")
screen.onkey(l_paddle.move_upward,"w")
screen.onkey(l_paddle.move_down,"s")
game_is_on=True
while game_is_on:
    time.sleep(ball.s)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()
    if ball.xcor()>380:
        ball.reset()
        scoreboard.lpoint()

    if ball.xcor() <-380:
            ball.reset()
            scoreboard.rpoint()
screen.exitonclick()