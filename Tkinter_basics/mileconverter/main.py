from tkinter import *

window=Tk()
window.title("Miles To KM converter")
window.minsize(width=300,height=200)
window.config(padx=34 ,pady=56,bg="#f0f8ff")
label_font = ("Arial", 10, "bold")
#All Labels
Main_title=Label(text="WELCOME TO CONVERTER",font=label_font)
Main_title.grid(column=1,row=0)
Main_title.config(pady=40,bg="#f0f8ff")
my_label1=Label(text="Is Equal to",font=label_font)
my_label1.grid(column=0,row=2)
my_label2=Label(text="Miles",font=label_font)
my_label2.grid(column=2,row=1)
my_label3=Label(text="0",font=label_font)
my_label3.grid(column=1,row=2)
my_label4=Label(text="Km",font=label_font)
my_label4.grid(column=2,row=2)

def converter():
    converted_entry=float(entry.get())
    converted_entry=round(converted_entry*1.609,3)
    my_label3.config(text=f"{converted_entry}")

#Button
button=Button(text="Calculate",font=label_font)
button.grid(row=3,column=1)


#Entry
entry=Entry(width=20)
entry.grid(column=1,row=1)
button.config(command=converter)



window.mainloop()
