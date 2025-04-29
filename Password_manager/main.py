from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols=[random.choice(numbers) for _ in range(nr_symbols)]
    password_numbers=[random.choice(symbols) for _ in range(nr_numbers)]
    
    password_list=password_letters+password_numbers+password_symbols
    random.shuffle(password_list)
    
    password="".join(password_list)
    pass_entry.insert(0,password)

    pyperclip.copy(password)
    
    






# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_data():
    web_data = web_entry.get()
    pass_data=pass_entry.get()
    email_data=email_entry.get()
    if len(web_data)==0 or len(pass_data)==0 or len(email_data)==0:
        messagebox.showerror(title="Error",message="Please Fill All Fields ")
    else:
        is_ok=messagebox.askokcancel(title=web_data,message=f"These are the details entered:\n Email: {email_data}\n Password:{pass_data} \n Is it oK to save?")
        if is_ok:
            with open("Data.txt", "a") as file:
                file.write(f" {web_data}  |   {pass_data}   | {email_data}\n")
            web_entry.delete(first=0, last=END)
            pass_entry.delete(first=0, last=END)
            email_entry.delete(first=0, last=END)


# ---------------------------- UI SETUP ------------------------------- #


#DOM Window Setup

window=Tk()
window.minsize(width=600,height=600)
window.title("Password Manager")
window.config(padx=50)
window.config(bg="white")
window.config(pady=70)



#Canvas Setup


photo=PhotoImage(file="logo.png")
canvas=Canvas(width=200,height=200,highlightthickness=0)
canvas.create_image(100,100,image=photo)
canvas.config(bg="white")
canvas.grid(column=1,row=0)



#Labels


web_label=Label(text="Website:",padx=20,pady=10,bg="white")
web_label.grid(column=0,row=1)

email_label=Label(text="Email/Username:",padx=20,pady=10,bg="white")
email_label.grid(column=0,row=2)

pass_label=Label(text="Password:",padx=20,pady=10,bg="white")
pass_label.grid(column=0,row=3)


#button

generate=Button(text="Generate Password",bg="white",width=21,highlightthickness=0,command=generate)
generate.grid(column=2,row=3,sticky="e")

add_btn=Button(text="Add",width=29,bg="white",padx=30,command=add_data)
add_btn.grid(row=4,column=1,columnspan=2)

#Entries

web_entry=Entry(width=35,bg="white")
web_entry.grid(row=1,column=1,columnspan=2)
web_entry.focus()


email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(END,"Example@gmail.com")


pass_entry=Entry(width=25,bg="white")
pass_entry.grid(row=3,column=1,sticky="e")
window.mainloop()