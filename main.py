'''
Author: Dipak Yadav
'''

# check if argument length is 2
import sys


if len(sys.argv) != 2:
    print("Usage: python main.py <cityname>")
    sys.exit(1)

# get city name from argument
city = sys.argv[1]
weather_api_key = "bd5e378503939ddaee76f12ad7a97608"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}"
# send request to openweathermap
import requests
response = requests.get(url)
# check if request is successful
if response.status_code != 200:
    print("Error: Request Failed")
    sys.exit(1)

# convert response to json
data = response.json()
# extract temperature and description
temperature = data["main"]["temp"]
description = data["weather"][0]["description"]
# print emojis based on weather description
emoji = ""
if "rain" in description:
    emoj = "🌧"
elif "cloud" in description:
    emoj = "☁️"
elif "sunny" in description:
    emoj = "☀️"
else:
    emoj = "🌈"



# print emojis based on weather temperature
temperature_fahrenheit = (temperature - 273.15) * 9/5 + 32
temp_emoji = ""
if temperature_fahrenheit < 10:
    temp_emoji = "⛄"
elif temperature_fahrenheit > 30:
    temp_emoji = "🔥"
else:
    temp_emoji = "😊"


print(f"The weather in {city} is  :                {description}  {emoj}")
print(f"Temperature               :                {temperature_fahrenheit}°F  {temp_emoji}")

# print emojis based on humidity
humidity = data["main"]["humidity"]
humidity_emoji = ""
if humidity < 30:
    humidity_emoji = "Dry 😊"
elif humidity > 60:
    humidity_emoji = "Humid 😓"
else:
    humidity_emoji = "Wet 😐"

print(f"The humidity is           :                {humidity}% | {humidity_emoji}")

# print emojis based on wind speed
wind_speed = data["wind"]["speed"]
wind_emoji = ""
if wind_speed < 10:
    wind_emoji = "Breezy 🍃"
elif wind_speed > 30:
    wind_emoji = "Windy 🌪"
else:
    wind_emoji = "Calm 🌬"

print(f"The wind speed is         :                {wind_speed} | {wind_emoji}")

# print emojis based on pressure
pressure = data["main"]["pressure"]
pressure_emoji = ""
if pressure < 1000:
    pressure_emoji = "Low 📉"
elif pressure > 1030:
    pressure_emoji = "High 📈"
else:
    pressure_emoji = "Normal 😐"

print(f"The pressure is           :                {pressure} | {pressure_emoji}")

# print emojis based on visibility
visibility = data["visibility"]
visibility_emoji = ""
if visibility < 1000:
    visibility_emoji = "Low 👀"
elif visibility > 10000:
    visibility_emoji = "High 👀"
else:
    visibility_emoji = "Normal 👀"

print(f"The visibility is         :                {visibility} | {visibility_emoji}")

# print emojis based on cloudiness
cloudiness = data["clouds"]["all"]
cloudiness_emoji = ""
if cloudiness < 30:
    cloudiness_emoji = "Clear ☀️"
elif cloudiness > 60:
    cloudiness_emoji = "Cloudy ☁️"
else:
    cloudiness_emoji = "Partly cloudy ⛅"

print(f"The cloudiness is         :                {cloudiness}% | {cloudiness_emoji}")

# print emojis based on sunrise
sunrise = data["sys"]["sunrise"]
# convert sunrise to city's local time
import datetime
sunrise = datetime.datetime.fromtimestamp(sunrise)
sunrise_emoji = ""
if sunrise.hour < 6:
    sunrise_emoji = "Rose early 🌅"
elif sunrise.hour > 18:
    sunrise_emoji = "Rose late 🌇"
else:
    sunrise_emoji = "Normal time 🌄"


print(f"The sunrise is            :                {sunrise.hour}:{sunrise.minute}:{sunrise.second} | {sunrise_emoji}")

# print emojis based on sunset
sunset = data["sys"]["sunset"]
# convert sunset to city's local time
import datetime
sunset = datetime.datetime.fromtimestamp(sunset)
sunset_emoji = ""
if sunset.hour < 6:
    sunset_emoji = "Set early 🌅"
elif sunset.hour > 18:
    sunset_emoji = "Set late 🌇"
else:
    sunset_emoji = "Normal time 🌄"


print(f"The sunset is             :                {sunset.hour}:{sunset.minute}:{sunset.second} | {sunset_emoji}")
