from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
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
def Search():
    web_data = web_entry.get()
    try:
        with open("Data.json")as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
            messagebox.showerror(title="Error", message="No data File you made")
    else:
            if web_data in data:
                email=data[web_data]["email"]
                password=data[web_data]["password"]
                messagebox.showinfo(title=web_data,message=f"email:{email}\n Password:{password}")
            else:
                messagebox.showerror(title="Error",message="No details Exist")
def add_data():
    web_data = web_entry.get()
    pass_data=pass_entry.get()
    email_data=email_entry.get()
    new_data={
        web_data:{
            "email":email_data,
            "password":pass_data
        }
    }
    if len(web_data)==0 or len(pass_data)==0 or len(email_data)==0:
        messagebox.showerror(title="Error",message="Please Fill All Fields ")
    else:
        try:
            with open("Data.json","r") as datafile:
                data=json.load(datafile)

        except FileNotFoundError:
            with open("Data.json","w") as datafile:
                    json.dump(new_data,datafile,indent=4)
        else:
            data.update(new_data)
            with open("Data.json", "w") as datafile:
                json.dump(new_data,datafile,indent=4)
        finally:
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
search=Button(text="Search",bg="white",width=17,command=Search)
search.grid(row=1,column=2)
generate=Button(text="Generate Password",bg="white",width=21,highlightthickness=0,command=generate)
generate.grid(column=2,row=3,sticky="e")

add_btn=Button(text="Add",width=29,bg="white",padx=30,command=add_data)
add_btn.grid(row=4,column=1,columnspan=2)

#Entries

web_entry=Entry(width=25,bg="white")
web_entry.grid(row=1,column=1,sticky="e")
web_entry.focus()


email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(END,"Example@gmail.com")


pass_entry=Entry(width=25,bg="white")
pass_entry.grid(row=3,column=1,sticky="e")
window.mainloop()