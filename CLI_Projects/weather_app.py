import requests
import time
from dotenv import load_dotenv
import os
import platform
from datetime import datetime, timedelta, timezone

## Functions
def get_temp_emoji(temp):
    if temp > 30:
        temp = "🔥"
    elif temp < 10:
        temp = "🥶"
    else:
        temp = "🌤️"
    return temp

def get_weather_emoji(condition):
    condition = condition.lower()
    if condition == "clear":
        return "☀️"
    elif condition == "clouds":
        return "☁️"
    elif condition == "rain":
        return "🌧️"
    elif condition == "drizzle":
        return "🌦️"
    elif condition == "thunderstorm":
        return "⛈️"
    elif condition == "snow":
        return "❄️"
    elif condition in ["mist", "fog", "haze", "smoke"]:
        return "🌫️"
    elif condition == "tornado":
        return "🌪️"
    else:
        return "🌍"

def get_weather_info(city):
    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(base_url)

    if response.status_code == 200:
        weather_data = response.json()

        ## Get location (City, Country)
        weather_city = f"{weather_data["name"]}, {weather_data["sys"]["country"]}"

        ## Get the date
        timestamp = weather_data["dt"]
        timezone_offset = weather_data["timezone"]
        utc_time = datetime.fromtimestamp(timestamp, tz=timezone.utc)
        local_time = utc_time + timedelta(seconds=timezone_offset)
        if(platform.system() == "Windows"):
            formatted_date = local_time.strftime("%A, %B %d, %Y")
        else:
            formatted_date = local_time.strftime("%A, %B %-d, %Y")

        ## Get the time
        formatted_time = local_time.strftime("%H:%M")
        

        ## -------- Get weather info --------
        temperature = weather_data["main"]["temp"]
        feels_like = weather_data["main"]["feels_like"]
        humidity = weather_data["main"]["humidity"]
        pressure = weather_data["main"]["pressure"]
        
        # Wind speed and direction
        wind_speed = round(weather_data["wind"]["speed"] * 3.6, 1)
        wind_degree = weather_data["wind"]["deg"]
        directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
        index = round(wind_degree / 45) % 8
        wind_direction = directions[index]
        
        # Get weather emoji
        condition = weather_data["weather"][0]["main"]
        condition_emoji = get_weather_emoji(condition)
        condition_description = weather_data["weather"][0]["description"]

        # Get temperature emojis
        feels_like_emoji = get_temp_emoji(feels_like)
        temperature_emoji = get_temp_emoji(temperature)

        # ----------------------------------------

        ## Return weather info well formatted
        return f"""📍 Location {weather_city}
📅 Date: {formatted_date}
🕒 Time: {formatted_time}

🌡️  Temperature: {temperature}°C {temperature_emoji}
🌡️  Feels like: {feels_like}°C {feels_like_emoji}
💧 Humidity: {humidity}%
🌬️  Wind: {wind_speed} km/h {wind_direction}
{condition_emoji}  Condition: {condition_description.capitalize()}
🔼 Pressure: {pressure} hPa"""
        
    else:
        return f"Failed to retreive data. Error coce: {response.status_code}"

## Getting the API key
load_dotenv()
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')


print("====================")
print("🌤️   Weather App CLI")
print("====================")

while True:
    ## Prompt the user for a city
    user_input = input("Enter the name of the city: ")
    
    ## If the user types something
    if user_input:
        ## Windows OS
        if platform.system() == "Windows":
            os.system("cls")
        ## Linux/macOS
        else:
            print("\033c", end="")
        
        print("====================")
        print("🌤️  Weather App CLI")
        print("====================")
        print(get_weather_info(user_input))

        ## break out of the loop
        break
