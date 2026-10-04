import os
from dotenv import load_dotenv
import requests

load_dotenv()

api_key = os.environ.get("OPEN_WEATHEAR_API_KEY", "")
api_url = "https://pro.openweathermap.org/data/2.5/forecast"
temp_lat = 41.299496
temp_lng = 69.240074


parameters = {
    "lat" : temp_lat,
    "lon" : temp_lng,
    "cnt" : 4,
    "appid" : api_key
}
request = requests.get(api_url, params=parameters)
request.raise_for_status()

will_rain = False

weather_data = request.json()["list"]
for hour_data in weather_data:
    if hour_data["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")
