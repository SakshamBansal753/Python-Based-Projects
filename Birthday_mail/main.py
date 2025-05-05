##################### Normal Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib
my_email="test_email"
password="app_paas"
data=pandas.read_csv("birthdays.csv")

now=dt.datetime.now()
today = (now.month, now.day)

new_dict = {(data_row.month,data_row.day): data_row for (index, data_row) in data.iterrows()}

if today in new_dict:
    birthday_person=new_dict[today]
    file_path=f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter:
        contents=letter.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(from_addr=my_email,to_addrs=birthday_person["email"],msg=f"Subject:Happy Birthday\n\n{contents}")




