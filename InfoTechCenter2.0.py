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
    elif weatherAlert == "Snowy":
        print("\nVRS changed your alarm 15 minutes earlier based on the NWS forecast of", weatherAlert, ":(")
        print("VRS will only allow your car to go 60MPH")
    elif weatherAlert == "Raining":
        print("\nVRS changed your alarm 5 minutes earlier based on the NWS forecast of", weatherAlert, ":(")
        print("VRS will only allow your car to go 70MPH")
    elif weatherAlert == "Windy":
        print("\nVRS changed your alarm 5 minutes earlier based on the NWS forecast of", weatherAlert, ":(")
        print("VRS will only allow your car to go 70MPH")
    elif weatherAlert == "Foggy":
        print("\nVRS changed your alarm 5 minutes earlier based on the NWS forecast of", weatherAlert, ":(")
        print("VRS will only allow your car to go 60MPH")
    else:
        print("\nWeather is",weatherAlert, "let's go!")
        print("VRS will allow your car to go 120MPH")




vehicleResponseSystem()

