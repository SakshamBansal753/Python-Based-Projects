from tkinter import *

import requests

APPID="3337be12d4710d6fa0e668b07b7d5157"
def get_weather():
    city = entry.get()
    params={
        'q':city,
        "appid":APPID,
        "units":"metric"
    }
    response=requests.get(url="https://api.openweathermap.org/data/2.5/weather",params=params)
    response.raise_for_status()
    data=response.json()
    temperature=data["main"]["temp"]
    description = data["weather"][0]["description"]
    weather_text = f"{city.title()} - {temperature}°C, {description.capitalize()}"
    canva.itemconfig(weather_display, text=weather_text)
    global weather_img
    if data["weather"][0]["id"] < 700:
        canva.itemconfig(icon, image=rain_icon)









Temp=0
#GUI
window=Tk()
window.title("Weather APP")
window.minsize(width=600,height=600)
window.config(bg="lightblue")
window.config(padx=60,pady=20)
#Title
title=Label(text="Weather APP",font=("Arial",30,"bold"),bg="lightblue")
title.grid(row=0,columnspan=2,column=0)
canva = Canvas(width=500, height=300, highlightthickness=0,bg="lightblue")
img1 = PhotoImage(file="rainy-background.png")
canva.create_image(250,120,image=img1)
weather_display=canva.create_text(250,200,text=f"Enter a city name",fill="black",font=("Arial",25,"bold"),width=200)
canva.grid(row=1,column=0,columnspan=2)
weather_img = PhotoImage(file="weather icon.png")
icon=canva.create_image(120,90,image=weather_img)
country=Label(text="City Name:",font=("Arial",30,"bold"),bg="lightblue")
country.grid(row=2,column=0)
entry=Entry(width=30)
entry.grid(column=1,row=2)
rain_icon = PhotoImage(file="images (1).png")
#checkweather
check=Button(text="Click to see weather",bg="blue",highlightthickness=0,highlightcolor="red",highlightbackground="blue",command=get_weather,width=60,font=("Arial",14,"bold"))
check.grid(row=3,column=0,columnspan=2)


window.mainloop()