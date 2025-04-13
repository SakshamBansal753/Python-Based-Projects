import pandas

data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirells=len(data[data["Primary Fur Color"]=="Gray"])

black_squirells=len(data[data["Primary Fur Color"]=="Black"])
red_squirells=len(data[data["Primary Fur Color"]=="Cinnamon"])


data_dict={
    "Fur Color":["Gray","Black","Cinnamon"],
    "Number":[grey_squirells,black_squirells,red_squirells]
}
print(data_dict)
df=pandas.DataFrame(data_dict)
df.to_csv("New_data.csv")

