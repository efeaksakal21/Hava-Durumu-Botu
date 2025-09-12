import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

CITY = "Istanbul"  # istediğin şehir


def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["main"]
        temp = data["main"]["temp"]
        print(f"🌍 Şehir: {city}")
        print(f"🌡️  Sıcaklık: {temp}°C")
        print(f"⛅ Hava: {weather}")
    else:
        print("Hata:", response.json())


if __name__ == "__main__":
    get_weather(CITY)
