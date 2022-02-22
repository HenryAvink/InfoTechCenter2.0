
import random

# Gas Level Function

def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full"]
    currentGasLevel = random.choice(gasLevelList)
    # print(currentGasLevel)
    return currentGasLevel

# Create If-ElIf-Else statements using Comparative Operators to display gas level messages
def gasLevelAlert():
    if gasLevelGauge() == "Empty":
        print("! ! !WARNING! ! !\nYou have run out of gas\nCalling Emergency Contact")




gasLevelAlert()