import numpy as np

fopen = open("/home/ckung/Code/Advent_Of_Code/input.day2","r")
passLine = fopen.readlines()

lowRange  = []
highRange = []
letter    = []
passwd    = []

for pwLineTest in passLine:
    #print(pwLineTest)
    # Split the letter check and the password
    splitter_0 = pwLineTest.split(": ")
    
    # Append password to check into a list and removes the newline character
    passwd.append(splitter_0[1].replace("\n",""))

    # Split the number range and letter to check
    splitter_1 = splitter_0[0].split(" ")

    # Append letter to a list
    letter.append(splitter_1[1])

    # Split the low and high checking range
    splitter_2 = splitter_1[0].split("-")
    lowRange.append(splitter_2[0])
    highRange.append(splitter_2[1])

validCount0 = 0
validCount1 = 0

for i in range(len(lowRange)):    
    # *** Part 1 ***
    # Count the number of letters in a string
    count = passwd[i].count(letter[i])
    #print(count)
    
    # If the count is >0 to the low range and <= to the high Range,
    # the password count is incremented
    if count >= int(lowRange[i]) and count <= int(highRange[i]):
        validCount0 = validCount0 + 1

    # *** Part 2 ***
    # This checks whether only ONE of the indicated spots contains
    # the ltter
    part2check = (passwd[i][int(lowRange[i])-1]  == letter[i]) ^ \
                 (passwd[i][int(highRange[i])-1] == letter[i])
    if part2check:
        validCount1 = validCount1 + 1


print("There are", validCount0, "valid passwords for part 1!")
print("There are", validCount1, "valid passwords for part 2!")