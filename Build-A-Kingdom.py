import time
import random
import math

#Utility Value
turn = 0
crashTest = 1
playerInput = 0
month = 1
year = 1

#Kingdom Value
kingdomName = "null"
kingdomWealth = 0
kingdomIncome = 0
kingdomDevelopment = 0
kingdomDevelopmentGain = 0
kingdomHappiness = 0
kingdomHappinessGain = 0
kingdomPopulation = 0
kingdomFood = 0
kingdomFoodProduction = 0
pGrowthVal = 0
pGrowthCurVal = 0
pGrowthLimit = 100
Apprentices = False
Magic = False
LandOwnership = False
banks = 0
farms = 0
forges = 0
goods = 0
goodsProduction = 0
taverns = 0

#KingdomEvent
rEvent = ["safe", "safe", "safe", "safe", "safe", "warband", "treasure", "celebration", "infection", "assassination"]
eventVal = 0
plagueSeverity = 0
assassinType = 0
aSurvival = 0

#NPC Values

#clears the terminal Window after recieving any input
def clearInput():
    global continueInput
    continueInput = input()
    print("\x1b[2J")

def clear():
    print("\x1b[2J")

def stat():
    global kingdomWealth
    global kingdomDevelopment
    global kingdomHappiness
    global kingdomPopulation
    global pGrowthVal
    
    print("Gold: " + str(kingdomWealth) + "\nPopulation: " + str(kingdomPopulation) + "\nHappiness: " + str(kingdomHappiness) + "\nFood: " + str(kingdomFood))

def menu():
    global kingdomName
    print("What would you like to name your kingdom?")
    kingdomName = input()
    print(str(kingdomName) + " is such a lovely name, I hope you make it as grand as it sounds.")
    global kingdomWealth
    global kingdomDevelopment
    global kingdomHappiness
    global kingdomPopulation
    global pGrowthVal
    global kingdomFood
    global pGrowthCurVal
    global pGrowthLimit

    kingdomWealth = 50
    kingdomDevelopment = 0
    kingdomHappiness = 50
    kingdomFood = 50
    
    kingdomPopulation = 1
    pGrowthVal = 2
    pGrowthCurVal = 0
    pGrowthLimit = 100

    print("Your new Kingdom Starts with some resources...")
    stat()
    print("(Press enter to continue)")
    clearInput()

def menu2():
    global turn
    global month
    global crashTest
    global year
    while(crashTest == 1):
        clear()
        if(turn > 0):
            print("The ledger has been updated with the kingdoms...")
        print("date: 01/" + str(month) + "/" + str(year))
        print("1. Kingdom Ledger\n2. Constructions\n3. Laws\n4. Next Month\n5. Exit")
        playerInput = input()
        if(playerInput == "1"):
            ledger()
        elif(playerInput == "2"):
            constructions()
        elif(playerInput == "3"):
            laws()
        elif(playerInput == "4"):
            nexTurn()
        elif(playerInput == "5"):
            exit()

def constructions():
    global taverns, goods, goodsProduction, banks, farms, forges, playerInput, turn, month, turn, kingdomDevelopment, kingdomWealth, kingdomHappiness, kingdomFood, kingdomPopulation, pGrowthVal, pGrowthLimit, pGrowthCurVal, kingdomIncome, kingdomDevelopmentGain, kingdomFoodProduction, kingdomHappinessGain, Apprentices, Magic, LandOwnership
    clear()
    print("Construction:\n1. Banks\nCost: 25 Gold\nEffects: Increase Income based on population\n2. farms\nCost: 25 Gold\nEffects: Increases Food production based on population\n3. forges\nCost: 100 Gold\n Effects: Increases goods production based on population\n4. Taverns\nCost: 250 Gold\nEffects: Increase Happiness Based on amount of Taverns.\n5. Back")
    playerInput = input()
    if(playerInput == "1" and kingdomWealth > 24):
        banks = banks + 1
        kingdomWealth = kingdomWealth - 25
    elif(playerInput == "2" and kingdomWealth > 24):
        farms = farms + 1
        kingdomWealth = kingdomWealth - 25
    elif(playerInput == "3" and kingdomWealth > 99):
        forges = forges + 1
        kingdomWealth = kingdomWealth - 100
    elif(playerInput == "4" and kingdomWealth > 249):
        taverns = taverns + 1
        kingdomWealth = kingdomWealth - 250
    elif(not playerInput == "5"):
        print("Not Enough Money!\n(Press enter to continue.)")
        clearInput()

def laws():
    global playerInput, turn, month, turn, kingdomDevelopment, kingdomWealth, kingdomHappiness, kingdomFood, kingdomPopulation, pGrowthVal, pGrowthLimit, pGrowthCurVal, kingdomIncome, kingdomDevelopmentGain, kingdomFoodProduction, kingdomHappinessGain, Apprentices, Magic, LandOwnership
    clear()
    print("Current Kingdom Laws:\n1. Unpaid Apprentices: " + str(Apprentices) + "\n2. Magic: " + str(Magic) + "\n3. Land Ownership: " + str(LandOwnership) + "\n4. Back")
    playerInput = input()
    if(playerInput == "1" and Apprentices == False):
        Apprentices = True
    elif(playerInput == "1" and Apprentices == True):
        Apprentices = False
    elif(playerInput == "2" and Magic == True):
        Magic = False
    elif(playerInput == "2" and Magic == False):
        Magic = True
    elif(playerInput == "3" and LandOwnership == True):
        LandOwnership = False
    elif(playerInput == "3" and LandOwnership == False):
        LandOwnership = True

def ledger():
    global taverns, goods, goodsProduction, banks, farms, forges, playerInput, turn, month, turn, kingdomDevelopment, kingdomWealth, kingdomHappiness, kingdomFood, kingdomPopulation, pGrowthVal, pGrowthLimit, pGrowthCurVal, kingdomIncome, kingdomDevelopmentGain, kingdomFoodProduction, kingdomHappinessGain, Apprentices, Magic, LandOwnership
    clear()
    print(str(kingdomName) + ": ")
    print("ECONOMY:\nGold: " + str(kingdomWealth) + "\nIncome: " + str(kingdomIncome) + "\nGoods: " + str(goods) + "\nGoods Production: " + str(goodsProduction) + "\nFood: " + str(kingdomFood) + "\nFoodProduction: " + str(kingdomFoodProduction))
    print("POPULACE:\nPopulation: " + str(kingdomPopulation) + "\nHappiness: " + str(kingdomHappiness) + "\nHapiness Gain: " + str(kingdomHappinessGain))
    print("BUILDINGS:\nBanks: " + str(banks) + "\nFarms: " + str(farms) + "\nForges: " + str(forges) + "\nTaverns: " + str(taverns))
    print("\n1. Sell Goods\n2. Back")
    playerInput = input()
    if(playerInput == "1"):
        kingdomWealth = kingdomWealth + goods
        print("You have sold all your goods and acquired " + str(goods) + " gold.")
        goods = 0
        print("(Press enter to continue)")
        clearInput()


def nexTurn():
    global year, taverns, goods, goodsProduction, banks, farms, forges, playerInput, turn, month, turn, kingdomDevelopment, kingdomWealth, kingdomHappiness, kingdomFood, kingdomPopulation, pGrowthVal, pGrowthLimit, pGrowthCurVal, kingdomIncome, kingdomDevelopmentGain, kingdomFoodProduction, kingdomHappinessGain, Apprentices, Magic, LandOwnership
    global rEvent, eventVal
    turn = turn + 1

    if(kingdomFood < 0):
        pGrowthVal = 0
    elif(kingdomFood > -1 and kingdomFood < 100):
        pGrowthVal = 1
    elif(kingdomFood > 99 and kingdomFood < 1000):
        pGrowthVal = math.ceil(kingdomFood/100)
    elif(kingdomFood > 999):
        pGrowthVal = 10
    
    if(month == 12):
        month = 0
        year = year + 1
    month = month + 1
    if(pGrowthCurVal < pGrowthLimit):
        pGrowthCurVal = pGrowthCurVal + pGrowthVal
    else:
        pGrowthCurVal = 0
        kingdomPopulation = kingdomPopulation + 1
    kingdomHappinessGain = taverns - 1
    kingdomHappiness = kingdomHappiness + kingdomHappinessGain
    if(kingdomWealth > 100 and kingdomFood > 100):
        kingdomDevelopmentGain = 1
    else:
        kingdomDevelopmentGain = 0
    kingdomDevelopment = kingdomDevelopment + kingdomDevelopmentGain
    kingdomFoodProduction = (farms * 2) * kingdomPopulation
    kingdomFood = kingdomFood + kingdomFoodProduction - (kingdomPopulation * 2)
    kingdomIncome = kingdomPopulation * banks - (math.ceil(kingdomDevelopment * .5))
    kingdomWealth = kingdomWealth + kingdomIncome
    goodsProduction = forges * kingdomPopulation
    goods = goods + goodsProduction
    if(kingdomHappiness < -50):
        print("Your people have rebelled and executed you.")
        clearInput()
        exit()
    elif(kingdomFood < (-1 * (kingdomPopulation * 100))):
        kingdomPopulation = kingdomPopulation - 1
        kingdomHappiness = kingdomHappiness - 1
        food = food + 100
        if(not kingdomPopulation > 0):
            print("You and your people starved to death.")
            clearInput()
            exit()
    eventVal = random.randrange(0, 10)
    if(rEvent[eventVal] == "warband"):
        warband()
    elif(rEvent[eventVal] == "treasure"):
        treasure()
    elif(rEvent[eventVal] == "celebration"):
        celebration()
    elif(rEvent[eventVal] == "infection"):
        infection()
    elif(rEvent[eventVal] == "assassination"):
        assassination()
    else:
        print("Nothing particularly special happens.")
    if(kingdomPopulation < 1):
        print("You have no more people and are left poor and alone.")
        exit()
    
def warband():
    global playerInput, kingdomPopulation, kingdomWealth, kingdomHappiness, kingdomFood
    clear()
    print("A hostile warband is invading your lands.\nYou may fight them off if you have the soldiers, or pay them off if you have the food or gold.\n1. Fight (-1 population)\n2. Pay (-100 gold)\n3. Ignore (There will be consequences)")
    playerInput = input()
    if(playerInput == "1" and kingdomPopulation > 1):
        print("The battle was terrible with many losses but you prevail.\nYou have gained some loot from the warband. (+20 gold)")
        kingdomPopulation = kingdomPopulation - 1
        kingdomWealth = kingdomWealth + 20
        clearInput()
    elif(playerInput == "2" and kingdomWealth > 99):
        print("The people are unhappy with this decision but it has caused the warband to leave for now.")
        kingdomHappiness = kingdomHappiness - 1
        kingdomWealth = kingdomWealth - 100
        clearInput()
    else:
        print("A portion of your population has been killed by the bandits and a portion of your food and gold have been stolen.")
        kingdomHappiness = kingdomHappiness - 5
        kingdomPopulation = kingdomPopulation - math.floor(kingdomPopulation * .3)
        kingdomWealth = kingdomWealth - math.ceil(kingdomWealth * .3)
        kingdomFood = kingdomFood - math.ceil(kingdomFood * .3)
        clearInput()
    
def treasure():
    global playerInput, kingdomPopulation, kingdomWealth, kingdomHappiness, kingdomFood
    clear()
    print("Your people have found a treasure chest. +50 gold")
    kingdomWealth = kingdomWealth + 50
    clearInput()

def celebration():
    global playerInput, kingdomPopulation, kingdomWealth, kingdomHappiness, kingdomFood
    clear()
    print("A great day of celebration has come.\n(Press enter to see the results of this celebration.)")
    playerInput = input()
    if(kingdomFood < 0):
        print("You didn't have food and the people rioted. -5 Happiness")
        kingdomHappiness = kingdomHappiness - 5
    elif(kingdomFood > 0):
        print("Your people enjoyed themselves on this great occasion. +2 Happiness")
        kingdomHappiness = kingdomHappiness + 2
    elif(kingdomFood > 250):
        print("Your people had a feast and celebrated throughout the night.\n+10 Happiness, -50 food")
        kingdomHappiness = kingdomHappiness + 10
        kingdomFood = kingdomFood - 50
    clearInput()

def infection():
    global playerInput, kingdomPopulation, kingdomWealth, kingdomHappiness, kingdomFood, plagueSeverity
    clear()
    plagueSeverity = random.randrange(0, 5)
    if(plagueSeverity < 1):
        plagueSeverity = 1
    elif(plagueSeverity > 3):
        plagueSeverity = 3
    print("A great plague has cursed your lands.\nSeverity = " + str(plagueSeverity) + "\n1. Isolate your capital\n2. Burn your dead\n3. Ignore the plague")
    playerInput = input()
    if(plagueSeverity == 1):
        if(playerInput == "1"):
            print("Thanks to the Isolation of your Capital you fight off the plague with only the loss of some food. -25 food")
            kingdomFood = kingdomFood - 25
        elif(playerInput == "2"):
            print("Burning your dead has led to the disease dying out though people are less happy now. -1 Happiness")
            kingdomHappiness = kingdomHappiness - 1
        elif(playerInput == "3"):
            print("Some people have died due to your arrogance. This has left the people unhappy with your rule. -2 Happiness, -" + str(math.floor(kingdomPopulation * .1)) + " Population")
            kingdomHappiness = kingdomHappiness - 1
            kingdomPopulation = kingdomPopulation - math.floor(kingdomPopulation * .1)
    elif(plagueSeverity == 2):
        if(playerInput == "1"):
            print("Thanks to the Isolation of your Capital you fight off the worst of the plague losing only some trade and food.\n-50 food, -5 gold")
            kingdomFood = kingdomFood - 50
            kingdomWealth = kingdomWealth - 5
        elif(playerInput == "2"):
            print("Burning your dead has led to the disease dying out faster than it would have naturally though people are less happy now and some gold has gone missing.\n -3 Happiness, -10 gold")
            kingdomHappiness = kingdomHappiness - 3
            kingdomWealth = kingdomWealth - 10
        elif(playerInput == "3"):
            print("Some people have died due to your arrogance. This has left the people severely unhappy with your rule.\n -10 Happiness, -" + str(math.floor(kingdomPopulation * .25)) + " Population, -30 gold")
            kingdomHappiness = kingdomHappiness - 10
            kingdomPopulation = kingdomPopulation - math.floor(kingdomPopulation * .25)
            kingdomWealth = kingdomWealth - 30
    elif(plagueSeverity == 3):
        if(playerInput == "1"):
            print("Thanks to the Isolation of your Capital you fight off the worst of the plague but your kingdom has suffered.\n-50 food, -25 gold, -" + str(math.floor(kingdomPopulation * .1)) + " Population")
            kingdomFood = kingdomFood - 50
            kingdomWealth = kingdomWealth - 25
        elif(playerInput == "2"):
            print("Burning your dead has led to the disease dying out faster than it would have naturally though people are unhappy now and some gold has gone missing.\n -5 Happiness, -30 gold, -" + str(math.floor(kingdomPopulation * .25)))
            kingdomHappiness = kingdomHappiness - 5
            kingdomWealth = kingdomWealth - 30
            kingdomPopulation = kingdomPopulation - math.floor(kingdomPopulation * .25)
        elif(playerInput == "3"):
            print("Many people have died due to your arrogance. This has left the people severely unhappy with your rule.\n -25 Happiness, -" + str(math.floor(kingdomPopulation * .5)) + " Population, -50 gold")
            kingdomHappiness = kingdomHappiness - 25
            kingdomPopulation = kingdomPopulation - math.floor(kingdomPopulation * .5)
            kingdomWealth = kingdomWealth - 50
    clearInput()


def assassination():
    global playerInput, kingdomPopulation, kingdomWealth, kingdomHappiness, kingdomFood, assassinType, aSurvival
    assassinType = random.randrange(0, 3)
    clear()
    if(assassinType == 1):
        print("A dark figure looms over you, a sharp object in hand.\n1. Fight the figure (50%)\n2. run (75%)")
        if(kingdomHappiness > 10):
            print("3. Call for your guards (100%)")
        playerInput = input()
        if(playerInput == "1"):
            aSurvival = random.randrange(0, 101)
            if(aSurvival > 50):
                print("You succesfully fight off your attacker.")
            else:
                print("Your attacker kills you. You lose.")
                clearInput()
                exit()
        elif(playerInput == "2"):
            aSurvival = random.randrange(0, 101)
            if(aSurvival > 25):
                print("You succesfully escape your attacker.")
            else:
                print("Your attacker catches up and kills you. You lose.")
                clearInput()
                exit()
        elif(playerInput == "3" and kingdomHappiness > 10):
            print("Guards rush into your room and kill the attacker.")
        else:
            print("Your guards seem unable to hear you scream as the assassin kills you")
    else:
        print("A figure is standing over you...")
        time.sleep(.5)
        print("It is just your spouse.")
    clearInput()

def main():
    global playerInput
    print("KINGDOM MAKER\n1. Start\n2. Exit")
    playerInput = input()
    if(playerInput ==  "1"):
        menu()
        menu2()
    else:
        print("Failure")

print("Welcome to")
time.sleep(.5)
print(" ")
time.sleep(.5)
print(" ")
time.sleep(.5)
print("KINGDOM BUILDER\n(Press Enter to Continue)")
clearInput()

main()