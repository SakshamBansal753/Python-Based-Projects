BACKGROUND_COLOR = "#B1DDC6"
FONT="Arial"
import random
from tkinter import*
import pandas
current_card={}
to_learn={}
try:
    data=pandas.read_csv("data/Words_to_learn.csv")
except FileNotFoundError:
    originaldata=pandas.read_csv("data/french_words.csv")
    to_learn=originaldata.to_dict(orient="records")
else:

    to_learn=data.to_dict(orient="records")

def next_card():
    global current_card,flip
    window.after_cancel(flip)
    current_card=random.choice(to_learn)
    canva.itemconfig(title,text=current_card["French"],font=(FONT,60,"bold"),fill="black")
    canva.itemconfig(super,text="French",fill="black")
    canva.itemconfig(card_Back_image, image=old_image)
    flip=window.after(3000, func=flip_card)


def flip_card():
       canva.itemconfig(super,text="English",fill="white")
       canva.itemconfig(title,text=current_card["English"],fill="white")
       canva.itemconfig(card_Back_image,image=card_back)

def is_knew():
    to_learn.remove(current_card)
    data=pandas.DataFrame(to_learn)
    data.to_csv("data/Words_to_learn.csv",index=False)
    next_card()


















#window
window=Tk()
window.title("Flash Card")

window.config(bg=BACKGROUND_COLOR,pady=50,padx=50)
flip=window.after(3000,func=flip_card)

#Canvas
canva=Canvas(width=800,height=526,highlightthickness=0)
old_image = PhotoImage(file="images/card_front.png")
card_back=PhotoImage(file="images/card_back.png")
card_Back_image=canva.create_image(400,262,image=old_image)
super=canva.create_text(400,150,text="Title",font=(FONT,40,"italic"))
title=canva.create_text(400,283,text="word",font=(FONT,60,"bold"))
canva.config(bg=BACKGROUND_COLOR)
canva.grid(column=0,columnspan=2,row=0)
#Buttons
my_image2=PhotoImage(file="images/right.png")
Right=Button(image=my_image2,highlightthickness=0,command=is_knew)
Right.grid(column=1,row=1)
my_image3=PhotoImage(file="images/wrong.png")
wrong=Button(image=my_image3,highlightthickness=0,command=next_card)
wrong.grid(column=0,row=1)
next_card()
window.mainloop()