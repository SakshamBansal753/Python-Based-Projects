from tkinter import  *
from tkinter import Text
import time
import random
#Setup
ALL_TEXT=[
    "All Here Are Useless",
    "I Love To Grind  Myself And Play games",
    "It is okay to do Murder",
    "Crime is actually maintaining the world",
    "Om Namo Bhagwate Vasudevay namha",
    "I am the most useless Guy ever Existed"
]
start_time = None

def start_timer(e):
    global start_time
    if start_time is None:
        start_time=time.time()



def check_speed():
    global start_time,random_text
    if start_time is None:
        print(f"Start This Game")
        result_label.config(text=f"Start Typing")
        return
    end_time=time.time()
    typed_text = user_input.get("1.0", END).strip()
    elapsed_time = end_time - start_time
    elapsed_minutes = elapsed_time / 60
    word_count=len(typed_text)
    wpm=round(word_count/elapsed_minutes,2) if elapsed_minutes>0 else 0
    result_label.config(text=f"Your speed is {wpm} WPM|{elapsed_minutes} Minutes|")
    user_input.delete("1.0",END)

def reatart_time():
    global start_time, random_text
    start_time=None
    s_label.config(text=random_text)
    random_text=random.choice(ALL_TEXT)
    result_label.config(text="")
    user_input.delete("1.0",END)

random_text=random.choice(ALL_TEXT)
window=Tk()
window.config(bg="black")
window.title("Speed Test")
window.geometry("920x320")


#Label
Main_label=Label(text="Welcome To Speed Test",fg="red")
Main_label.grid(column=1,row=0)

#Speed_text
s_label=Label(text=random_text,bg="gray",fg="Green",font=("Ariel",30,"bold"))
s_label.grid(column=1,row=1)
#Input
user_input=Text(fg="blue",font=("Ariel",20,"bold"),width=50,height=3)
user_input.grid(column=1,row=2)
user_input.bind("<KeyPress>",start_timer)
result_label = Label(window, text="", font=("Arial", 14),fg="white",bg="black")
result_label.grid(column=1,row=3)

#Check Button
check_button=Button(text="Check",command=check_speed,width=45)
check_button.grid(column=1,row=4)

restart_btn=Button(text="Restart",width=45,command=reatart_time)
restart_btn.grid(column=1,row=5)
window.mainloop()
