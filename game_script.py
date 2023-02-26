import random

actualGameLength = 0

yourGold = 0

chestDictionary = {
    "green" : 60,
    "orange" : 25,
    "purple" : 10,
    "gold" : 5
}

chestList = list(chestDictionary.keys())
chestProbability = list(chestDictionary.values())

eventDictionary = {
    "nothing" : 20,
    "chest" : 70,
    "monster" : 10
}

eventList = list(eventDictionary.keys())
eventProbabilty = list(eventDictionary.values())

goldFromChest = {
    "green" : 1000,
    "orange" : 4000,
    "purple" : 9000,
    "gold" : 16000
}

def findApproximateValue(value):
    lovestValue = value - 0.1 * value
    highestValue = value + 0.1 * value
    return random.randint(lovestValue, highestValue)

print("""The game involves making 10 moves through 10 chambers in the tomb. 
Every move is to another chamber. In each chamber you have a chance to find a chest 
of different types with the amount of gold or nothing. However, 
there is a risk. While passing through the chambers, you will encounter a monster 
that will kill you and you will lose all your gold. You have to decide whether 
you take a risk or keep going next step.
""")

while actualGameLength < 10:
    yourMove = input("""Write "move" if you want to go do next chamber or "stop" if you want to leave the tomb with current gold: """)
    if (yourMove == "move"):
        actualGameLength = actualGameLength + 1
        drawnEvent = random.choices(eventList, eventProbabilty)[0]
        if (drawnEvent == "nothing"):
            print("You haven't found anything, maybe try again")
        elif (drawnEvent == "chest"):
            chestColor = random.choices(chestList, chestProbability)[0]
            chestReward = findApproximateValue(goldFromChest[chestColor])
            print("You find a", chestColor, "chest with", chestReward, "gold")
            yourGold = yourGold + chestReward
        elif (drawnEvent == "monster"):
            actualGameLength = 11
            print("Game over, monster kills you, you lose all gold")
    elif (yourMove == "stop"):
        actualGameLength = 10
    else:
        print("Wrong select, try again!")
            
            
if (actualGameLength == 10):
    print("Congratulations, you find", yourGold, "gold and leave the tomb.")
