import turtle
from turtle import  Turtle,Screen
import pandas

data=pandas.read_csv("50_states.csv")
all_states=data.state.to_list()
guessed_state=[]
screen=Screen()
screen.title("US GUESSING GAME")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
while len(guessed_state)<50:
    ans_state=screen.textinput(title=f"{len(guessed_state)}/50 Guess The State is Correct",prompt="What is Another StateName or enter exit for out").title()
    if ans_state=="Exit":
        missing_state=[]
        for state in all_states:
            if state not in guessed_state:
                missing_state.append(state)

        break
    if ans_state in all_states:
        US = Turtle()
        US.hideturtle()
        US.penup()
        state_data=data[data.state==ans_state]
        US.goto(state_data.x.item(),state_data.y.item())
        US.write(ans_state)
        guessed_state.append(ans_state)



new_data=pandas.DataFrame(missing_state)
new_data.to_csv("States that You miss.csv")

