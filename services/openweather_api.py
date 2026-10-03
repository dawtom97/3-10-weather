import requests
from config import App
from datetime import datetime
from common.functions import from_ts

def get_weather():
    KEY = App.OW_API_KEY
    CITY = App.OW_CITY
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={KEY}"

    try:
        response = requests.get(URL)
        data = response.json()
        weather = {
            "temp": data.get("main").get("temp") - 273.15,
            "feels_like": data.get("main").get("feels_like"),
            "humidity": data.get("main").get("humidity"),
            "pressure": data.get("main").get("pressure"),
            "wind": data.get("wind").get("speed"),
            "clouds": data.get("clouds").get("all"),
            "city": data.get("name"),
            "sunrise": from_ts(data.get("sys").get("sunrise")),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        return weather
    except Exception as err:
        print(err)
