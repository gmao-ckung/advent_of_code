import os
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
fopen = open(CURR_DIR+"/input.07","r")

fileSystem = {}
command_or_output = fopen.readline()
upperDir = "None"
currDir = "None"
while(command_or_output):
    parsedCO = command_or_output.replace("\n","").split(" ")
    print(parsedCO)
    if(parsedCO[0] == "$"):
        # print("command found : ", parsedCO)
        if(parsedCO[1] == "cd"):
            if(parsedCO[2] == ".."):
                currDir = fileSystem[currDir][".."]
                upperDir = fileSystem[currDir][".."]
            else:
                upperDir = currDir
                if parsedCO[2] == "/":
                    checkDir = parsedCO[2]
                else:
                    checkDir = currDir + "_" + parsedCO[2]
                if(checkDir not in fileSystem.keys()):
                    currDir = checkDir
                    fileSystem[currDir] = {}
                    fileSystem[currDir][".."] = upperDir
                    # print(fileSystem[parsedCO[2]])
                else:
                    currDir = fileSystem[checkDir]

            command_or_output = fopen.readline().replace("\n","")
        elif(parsedCO[1] == "ls"):
            command_or_output = fopen.readline()
            commandFound = False
            while(command_or_output and not commandFound):
                parsedCO = command_or_output.replace("\n","").split(" ")
                print(parsedCO)
                if(parsedCO[0] != "$"):
                    #Need to be able to account for multiple directories
                    # print(parsedCO)
                    if(parsedCO[0] == 'dir'):
                        if 'dir' not in fileSystem[currDir].keys():
                            fileSystem[currDir][parsedCO[0]] = [parsedCO[1]]
                        else:
                            fileSystem[currDir][parsedCO[0]].append(parsedCO[1])
                    else:
                        fileSystem[currDir][parsedCO[0]] = parsedCO[1]
                    command_or_output = fopen.readline()
                else:
                    # print(parsedCO)
                    commandFound = True
                
            # print(fileSystem[currDir])
    
dirSizes = {}

def getDirSize(dir, fileSystem, upperDir):
    dirSize = 0
    # for dir in directories:
    if upperDir == "":
        currDir = dir
    else:
        currDir = upperDir + "_" + dir
    # print("dir", currDir,' contains the following: ', fileSystem[currDir])
    for data in fileSystem[currDir]:
        # print(data)
        if data == 'dir':
            # print("Going into directory ", fileSystem[currDir][data])
            for nextDir in fileSystem[currDir][data]:
                dirSize += getDirSize(nextDir, fileSystem, currDir)
        elif data != '..':
            # print("File size ", data, " found")
            dirSize += int(data)
    return dirSize

# Part 1

totalSum = 0

for dir in fileSystem.keys():
    dirSize = 0
    dirSize += getDirSize(dir, fileSystem, "")
    print("Size of directory ", dir, " = ", dirSize)
    if dirSize <= 100000:
        totalSum += dirSize

print("Total Sum = ", totalSum)

# Par t2

freeSpace = 70000000 - getDirSize('/', fileSystem,"")
minSpace = 70000000

for dir in fileSystem.keys():
    dirSize = getDirSize(dir,fileSystem,"")
    print("Size of directory ", dir, " = ", dirSize)
    print("freeSpace + dirSize = ", freeSpace + dirSize)
    if((minSpace > freeSpace + dirSize) & (30000000<(freeSpace + dirSize))):
        minSpace = freeSpace + dirSize

print("Total Directory Size = ", minSpace - freeSpace)