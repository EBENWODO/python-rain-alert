import os
import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
 
MY_LAT = 6.852290
MY_LONG = 7.395650

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
# weather_data_id = weather_data["list"][0]["weather"][0]["id"]
# print(weather_data_id)

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body="It's going to rain today. Remember to bring an ☂️",
    from_="+12567806323",
    to="+2349134119112",
    )
    
    print(message.status)