import os
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
fopen = open(CURR_DIR+"/input.03","r")

sacks = fopen.readlines()

# *** Part 1 ***

prioritySum = 0
for sack in sacks:
    sack = sack.replace("\n", "")
    comp1 = list(sack[0:int(len(sack)/2)])
    comp2 = list(sack[int(len(sack)/2):len(sack)])
    intersect = list(set(comp1) & set(comp2))
    if(ord(intersect[0]) >= 97):
        prioritySum += ord(intersect[0]) - 96
    else:
        prioritySum += ord(intersect[0]) - 38

print("Sum of priorities = ", prioritySum)

prioritySum = 0
currIndex = 0
group = []
for sack in sacks:
    currIndex += 1
    sack = sack.replace("\n", "")
    group.append(sack)

    if currIndex == 3:
        currIndex = 0
        intersect = list(set(group[0]) & set(group[1]) & set(group[2]))
        # print(intersect)
        if(ord(intersect[0]) >= 97):
            prioritySum += ord(intersect[0]) - 96
        else:
            prioritySum += ord(intersect[0]) - 38
        group = []

print("Sum of priorities = ", prioritySum)