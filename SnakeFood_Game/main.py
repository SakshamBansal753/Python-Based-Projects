from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
game_is_on=True
snake=Snake()
food=Food()
scoreboard=ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food)<15:
         food.refresh()
         snake.extend()
         scoreboard.increase_score()


    if snake.segments[0].xcor()>290 or snake.segments[0].xcor()<-290 or snake.segments[0].ycor()>290 or snake.segments[0].ycor()<-290:
        game_is_on=False
        scoreboard.stop()
    for segment in snake.segments[1:]:
        if  snake.segments[0].distance(segment)<10:
            game_is_on=False
            scoreboard.stop()

screen.exitonclick()



