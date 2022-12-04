import os
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
fopen = open(CURR_DIR+"/input.02","r")

matches = fopen.readlines()

score = 0

# *** Part 1 ***
for match in matches:
    match = match.replace("\n", "")
    if(ord(match[2]) - ord(match[0]) - 23 == 1 or ord(match[2]) - ord(match[0]) - 23 == -2):
        score += ord(match[2]) - 87 + 6
    elif(ord(match[2]) - ord(match[0]) - 23 == 0):
        score += ord(match[2]) - 87 + 3
    else:
        score += ord(match[2]) - 87

print("Final score for Part 1 = ", score)

# *** Part 2 ***
score = 0

for match in matches:
    match = match.replace("\n", "")
    score += (ord(match[2]) - 88) * 3
    if(match[2] == "X"):
        addIn = ord(match[0]) - 1 - 64
        if(addIn == 0):
            addIn = 3
        score += addIn
    if(match[2] == "Y"):
        addIn = ord(match[0]) - 64
        score += addIn
    if(match[2] == "Z"):
        addIn = ord(match[0]) + 1 - 64
        if(addIn == 4):
            addIn = 1
        score += addIn

print("Final score for Part 2 = ", score)