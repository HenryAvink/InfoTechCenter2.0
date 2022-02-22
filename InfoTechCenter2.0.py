import random


# Gas Level Function

def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel


# Variable calls the value of gasLevelGauge Function
gasLevelIndicator = gasLevelGauge()

# Create If-ElIf-Else statements using the Comparative Operator == (Equal to) to display gas level messages
def gasLevelAlert():
    gasStations = ["Shell", "BP", "Citgo", "Circle K", "Mobil", "Speedway", "Marathon", "Love's", "Meijer", "Costco", "Sunoco"]
    miles = round(random.uniform(1.0,25.0), 2)
    gasLevelIndicator = gasLevelGauge()
    if gasLevelIndicator == "Empty":
        print("! ! !WARNING - YOU ARE ON EMPTY! ! !\nCalling Emergency Contact")
    elif gasLevelIndicator == "Low":
        print("! ! !WARNING - LOW GASOLINE! ! !\nThe closest gas station is " + random.choice(gasStations) + " which is " + str(miles) + " miles away")
    elif gasLevelIndicator == "Quarter Tank":
        print("You are on a QUARTER TANK of gas\nStart planning a visit to the gas station. Closest gas station is " + random.choice(gasStations) + " which is " + str(miles) + " miles away")
    elif gasLevelIndicator == "Half Tank":
        print("You are on a HALF TANK of gas\nYou have 125 miles to empty")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("You have THREE QUARTER TANK of gas\nYou have 205 miles to empty")
    else:
        print("You are at a FULL TANK!\nYou have 310 miles to empty")


# Call Functions Here
gasLevelAlert()
