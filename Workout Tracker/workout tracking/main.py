import requests
from datetime import datetime
APPID="YOUR APP ID OF NUTRIENT"
APPKEY="KEY"
SHEETYURL="YOUR SHEETY URL"
Link="LINK OF API"
header={
    'Content-Type': 'application/json',
    "x-app-id":APPID,
    "x-app-key":APPKEY
}
data = {
    "query": input("What exercise you do"),
    "gender": "male",
    "weight_kg": 70,
    "height_cm": 175,
    "age": 18
}

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

responses=requests.post(url=Link,json=data,headers=header)
result=responses.json()
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheety=requests.post(url=SHEETYURL,json=sheet_inputs)

    print(sheety.text)