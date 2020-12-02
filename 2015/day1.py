f1 = open("/home/ckung/Code/Advent_Of_Code/2015/input.day1")

dataLine = f1.readline()
dataLine = dataLine.replace('\n','')

# *** Part 1 ***

currFloor = 0
for i in range(len(dataLine)):
    if dataLine[i] == '(':
        currFloor = currFloor + 1
    elif dataLine[i] == ')':
        currFloor = currFloor - 1

print("Part 1 : Current Floor =", currFloor)

# *** Part 2 ***
currFloor = 0
for i in range(len(dataLine)):
    if dataLine[i] == '(':
        currFloor = currFloor + 1
    
    elif dataLine[i] == ')':
        currFloor = currFloor - 1
    
    if currFloor < 0:
        print("Part 2 : Entering the basement")
        print("Part 2 : Current character position =", i+1)
        break