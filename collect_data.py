import requests
import csv
from datetime import datetime

API_KEY = "784b3f4a2e51848bf18cdef7604e4688"
CITY = "Karachi"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

def collect_weather_data():
    response = requests.get(URL)
    data = response.json()

    weather = {
        "datetime": datetime.now().isoformat(),
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "condition": data["weather"][0]["main"]
    }

    with open("data/raw_data.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=weather.keys())
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(weather)

if __name__ == "__main__":
    collect_weather_data()
