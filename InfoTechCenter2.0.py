import random
import requests
import json


# Weather Branch

def weather():
    weatherForecast = ["Icy", "Snowy", "Raining", "Windy", "Foggy", "Sunny"]
    weatherConditions = random. choice(weatherForecast)
    return weatherConditions

# Calling weather Function to determine weather
weatherAlert = weather()

def vehicleResponseSystem():
    if weatherAlert == "Icy":
        print("\nVRS changed your alarm 30 minutes earlier based on the NWS forecast of",weatherAlert,":(")
        print("VRS will only allow your car to go 30MPH")




vehicleResponseSystem()

