import requests
from twilio.rest import Client

API_KEY = "Your_API_KEY "
ACCOUNT_SID = "YOUR_TWILIO_SID"
AUTH_TOKEN = "YOUR_AUTH_YOKEN"
FROM_PHONE = "+TWILIO"
TO_PHONE = "Your self"


def get_weather_data(lat, lon):

    params = {
        'lat': lat,
        'lon': lon,
        'cnt': 4,  
        'appid': API_KEY
    }

    try:
        response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None


def will_it_rain(weather_data):
    if not weather_data:
        return False

    for hour_data in weather_data["list"]:
        condition_code = hour_data["weather"][0]["id"]
        if int(condition_code) < 700:  # Rains have codes < 700
            return True
    return False


def send_sms(message):
    """Sends an SMS message via Twilio"""
    try:
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages.create(
            body=message,
            from_=FROM_PHONE,
            to=TO_PHONE
        )
        print(f"Message sent: {message.status}")
    except Exception as e:
        print(f"Error sending SMS: {e}")


def main():

    lat, lon = 26.2236, 78.1792


    weather_data = get_weather_data(lat, lon)

    if will_it_rain(weather_data):
        send_sms("It's raining! Don't forget your umbrella! ☔")
    else:
        print("No rain expected.")


if __name__ == "__main__":
    main()

