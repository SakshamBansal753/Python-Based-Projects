import smtplib

import  datetime as dt
import random
my_email="test_email"
password="App_password"



now=dt.datetime.now()
weekday=now.weekday()
if weekday==0:
    with open("quotes.txt")as quotefile:
        all_qu=quotefile.readlines()
        random_quote=random.choice(all_qu)
        print(random_quote)
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="random_email",
                            msg=f"Subject:Your Today Motivational quote\n\n{random_quote}")
        connection.close()



