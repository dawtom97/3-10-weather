from services.openweather_api import get_weather
from services.files import create_file
from services.dashboard import render
from services.mysql_db import create_weather_table, save_weather
import time

# render()

create_weather_table()

while True:
    weather = get_weather()
    create_file([weather])
    save_weather(weather)
    print("Pobrałem dane pogodowe")
    time.sleep(120)



