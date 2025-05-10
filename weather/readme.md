# Weather Alert System

Hello Young Guns! 👋

I am Saksham, and this is my Weather Alert System project that fetches the weather forecast for a given location and sends an SMS notification via Twilio if it's going to rain. This is a simple yet effective way to stay informed and never get caught in the rain again! ☔

## Features

- Fetches 4-hour weather forecast from OpenWeather API.
- Checks for rain conditions in the forecast.
- Sends an SMS alert if rain is expected, using Twilio.

## Requirements

Before running the project, make sure you have the following:

- Python 3.x installed on your machine.
- A valid OpenWeather API Key (you can sign up for free [here](https://openweathermap.org/)).
- A Twilio Account SID and Auth Token (sign up [here](https://www.twilio.com/)).
- A Twilio phone number for sending SMS.
- A phone number to receive the SMS alert.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/weather-alert-system.git
   cd weather-alert-system
   ```
Install required dependencies:

Run the following command to install the necessary Python libraries:

```bash
Copy
Edit
pip install requests twilio
Set up your API keys:
```
Open the script and replace the following placeholders with your actual credentials:

# Replace these with your actual credentials

API_KEY = "Your_Actual_OpenWeather_API_Key"  # OpenWeather API Key
ACCOUNT_SID = "Your_Twilio_SID"  # Your Twilio Account SID
AUTH_TOKEN = "Your_Twilio_Auth_Token"  # Your Twilio Auth Token
FROM_PHONE = "+Your_Twilio_Phone_Number"  # Your Twilio phone number (e.g., "+1234567890")
TO_PHONE = "Your_Phone_Number"  # Your personal phone number (e.g., "+19876543210")
