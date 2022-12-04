import os
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
fopen = open(CURR_DIR+"/input.01","r")

calorieLines = fopen.readlines()

# *** Part 1 ***
currCalories = 0
maxCalories = 0

for calorieLine in calorieLines:
    calorieLine = calorieLine.replace("\n", "")
    if calorieLine != "":
        currCalories += int(calorieLine)
    else:
        if maxCalories < currCalories:
            maxCalories = currCalories
        currCalories = 0

print(maxCalories)

# *** Part 2 ***
currCalories = 0
maxCalorieList = [0,0,0]

for calorieLine in calorieLines:
    calorieLine = calorieLine.replace("\n", "")
    if calorieLine != "":
        currCalories += int(calorieLine)
    else:
        if maxCalorieList[0] < currCalories:
            maxCalorieList.insert(0,currCalories)
        elif maxCalorieList[1] < currCalories:
            maxCalorieList.insert(1,currCalories)
        elif maxCalorieList[2] < currCalories:
            maxCalorieList.insert(2,currCalories)
        if(len(maxCalorieList) > 3):
            maxCalorieList.pop(3)
        currCalories = 0

if maxCalorieList[0] < currCalories:
    maxCalorieList.insert(0,currCalories)
elif maxCalorieList[1] < currCalories:
    maxCalorieList.insert(1,currCalories)
elif maxCalorieList[2] < currCalories:
    maxCalorieList.insert(2,currCalories)
if(len(maxCalorieList) > 3):
    maxCalorieList.pop(3)

print(maxCalorieList[0] + maxCalorieList[1] + maxCalorieList[2])