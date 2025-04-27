# Tkinter Basics

Hello young guns, I am Saksham! 👋  
Welcome to the journey of mastering **Tkinter** — the standard GUI (Graphical User Interface) library for Python.

This project is all about learning Tkinter from scratch, starting with simple windows to building full-fledged desktop applications!

---

## What's Covered

- Setting up Tkinter
- Creating your first window
- Adding Labels, Buttons, and Inputs
- Layout management (Pack, Grid, Place)
- Handling Events
- Building simple apps (like a Calculator, To-Do list, etc.)

---

## Quick Start: Hello World!

```python
from tkinter import *

window=Tk()
window.title("My First GUI Program")
window.minsize(width=600,height=600)


#Label
my_label=Label(text="I am A Label",font=("Arial",24,"bold"))

my_label.place(x=0,y=0)

def button_click():
    my_label.config(text=f"{input.get()}")
#Buttons
button=Button(text="Hello I am button")
button.pack()

#Entry

input=Entry(width=10)
input.insert(END,"Email")
input.pack()
text=Text(height=5,width=30)
text.focus()
print(text.get("1.0",END))
text.pack()

#SPINBOX
def spin_box():
    print(spinbox.get())

spinbox=Spinbox(from_=0,to=15,width=6,command=spin_box)
spinbox.pack()
#Scale
def scale_used(value):
    print(value)

scale=Scale(from_=0,to=100,command=scale_used)
scale.pack()

#Checkbox
def check():
    print(checked_state.get())

checked_state=IntVar()
check_btn=Checkbutton(text="IS ON?",variable=checked_state,command=check)
check_btn.pack()

#RadioButton
def radio():
    print(radio_state.get())
radio_state=IntVar()
Radio1=Radiobutton(text="123",value=1,variable=radio_state,command=radio)
Radio2=Radiobutton(text="124",value=2,variable=radio_state,command=radio)
Radio3=Radiobutton(text="125",value=3,variable=radio_state,command=radio)
Radio1.pack()
Radio2.pack()
Radio3.pack()

#ListBox
def  list_s(event):
    print(listbox.get(listbox.curselection()))
listbox=Listbox(height=4)
fruits=["Apple","Pear","Orange","Banana"]
for item in fruits:
    listbox.insert(fruits.index(item),item)

listbox.bind("<<ListboxSelect>>",list_s)
listbox.pack()

button.config(command=button_click)

window.mainloop()
```

**ANd**
```python
from tkinter import *

window=Tk()
window.title("My First GUI Program")
window.minsize(width=600,height=600)
window.config(padx=90,pady=90)


#Label
my_label=Label(text="I am A Label",font=("Arial",24,"bold"))
my_label.config(pady=50,padx=50)
my_label.grid(column=0,row=0)

def button_click():
    my_label.config(text=f"{input.get()}")
#Buttons
button=Button(text="Hello I am button")
button.grid(column=2,row=0)
button=Button(text="Hello I am button")
button.grid(column=1,row=1)

#Entry
#You Cant use pack with grid
input=Entry(width=10)
input.insert(END,"Email")
input.grid(column=3,row=3)

window.mainloop()
```

## Project Goals

- Make coding GUIs easy and fun 🎯
- Empower you to build your own cool apps 💻
- Learn by doing and experimenting! 🚀

---

## Author

**Saksham** ✌️

Happy Coding! 🌟

