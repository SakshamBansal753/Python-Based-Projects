from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    my_label.config(text="TIMER")
    canvas.itemconfig(timer_text,text="00:00")
    tick.config(text="")
    global  reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():

    global reps

    reps+=1
    work_sec=WORK_MIN*60
    short_sec=SHORT_BREAK_MIN*60
    long_sec=LONG_BREAK_MIN*60
    if reps%8==0:
        count_down(long_sec)
        my_label.config(text="Break",fg=RED)
    elif reps%2==0:
        count_down(short_sec)
        my_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        my_label.config(text="Work", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        start()
        mark=""
        for x in range(math.floor(reps/2)):
            mark+="✔"

        tick.config(text=f"{mark}")


# ---------------------------- UI SETUP ------------------------------- #
#WINDOW
window=Tk()
window.title("Pamodoro")
window.config(padx=120,pady=60)
window.config(bg=YELLOW)


#LABEL

#title Label
my_label=Label(text="TIMER",fg=GREEN,font=(FONT_NAME,45,"bold"),bg=YELLOW,padx=50)
my_label.grid(column=1,row=0)

#Tick Label
tick=Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,25))
tick.grid(column=1,row=3)


#BUTTON

#start_Button

start_btn=Button(text="Start",fg=RED,font=(FONT_NAME,14,"bold"),command=start)
start_btn.grid(column=0,row=2)

#reset Button


Reset_btn=Button(text="Reset",fg=RED,font=(FONT_NAME,14,"bold"),command=reset)
Reset_btn.grid(column=2,row=2)

#CANVAS

canvas=Canvas(width=250 ,height=250,highlightthickness=0)
Photo=PhotoImage(file="tomato.png")
canvas.create_image(128,126,image=Photo)
canvas.config(bg=YELLOW)
timer_text=canvas.create_text(128,150,text="00:00",fill="white",font=(FONT_NAME,24,"bold"))

canvas.grid(column=1,row=1)


window.mainloop()