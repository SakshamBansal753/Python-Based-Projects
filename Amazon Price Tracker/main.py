from bs4 import BeautifulSoup
import requests
import smtplib
GMAIL="Gmail"
APP="AppPassword"
HEADER={"User-Agent":"serMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
        }
response=requests.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1",headers=HEADER)
soup=BeautifulSoup(response.text,"html.parser")

Price=soup.find(name="span",class_="a-offscreen").getText()
Price=float(Price.split("$")[1])
print(Price)
Target=100.00
title=soup.find(id="productTitle").getText().strip()
print(title)
if Price<Target:
    message=f"{title} is now on sale with Price ={Price}"
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(GMAIL,APP)
        connection.sendmail(from_addr=GMAIL,to_addrs=GMAIL,msg=f"Subject:Amazon Price alert:\n\n{message}\nhttps://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1".encode("utf-8"))
        connection.close()