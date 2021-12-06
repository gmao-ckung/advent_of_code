import numpy as np

def separateViaDelin(commaDelinLine, delin=","):
    # Separate string via delineator
    lineListData = commaDelinLine.split(delin)
    lineListData[-1] = lineListData[-1].split("\n")[0]    # Get rid of the newline        

    return lineListData

def createFishArray(list):
    N = len(list)
    fishArray = np.zeros(N,dtype=int)
    for i in range(N):
        fishArray[i] = int(list[i])

    return fishArray

def iterateFishLife(fishArray, days):
    for day in range(days):
        fishArray -= 1

        mask = fishArray < 0

        if(sum(mask) > 0):
            fishArray[mask] = 6
            newFish = np.ones(sum(mask), dtype=int) * 8
            fishArray = np.append(fishArray, newFish, axis=0)

    return fishArray

def interateFishLife_recursive(fishTimer,days):
    fishTimer -= 1
    days -= 1

    if fishTimer > days:
        return 1
    elif days == 0:
        if fishTimer >= 0:
            return 1
        else:
            return 2
    else:
        if fishTimer >= 0:
            return interateFishLife_recursive(fishTimer, days)
        else:
            return interateFishLife_recursive(6, days) + interateFishLife_recursive(8, days)

