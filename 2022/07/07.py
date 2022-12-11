import os
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
fopen = open(CURR_DIR+"/input.test","r")

fileSystem = {}
command_or_output = fopen.readline()
upperDir = "None"
currDir = "None"
while(command_or_output):
    # print(command_or_output)
    parsedCO = command_or_output.replace("\n","").split(" ")
    # print(parsedCO)
    if(parsedCO[0] == "$"):
        # print("command found : ", parsedCO)
        if(parsedCO[1] == "cd"):
            upperDir = currDir
            if(parsedCO[2] == ".."):
                currDir = fileSystem[currDir][".."]
            elif(parsedCO[2] not in fileSystem.keys()):
                currDir = parsedCO[2]
                fileSystem[currDir] = {}
                fileSystem[currDir][".."] = upperDir
                # print(fileSystem[parsedCO[2]])
            else:
                currDir = fileSystem[parsedCO[2]]

            command_or_output = fopen.readline().replace("\n","")
        elif(parsedCO[1] == "ls"):
            command_or_output = fopen.readline()
            commandFound = False
            while(command_or_output and not commandFound):
                parsedCO = command_or_output.replace("\n","").split(" ")
                if(parsedCO[0] != "$"):
                    #Need to be able to account for multiple directories
                    print(parsedCO)
                    if(parsedCO[0] == 'dir'):
                        if 'dir' not in fileSystem[currDir].keys():
                            fileSystem[currDir][parsedCO[0]] = [parsedCO[1]]
                        else:
                            fileSystem[currDir][parsedCO[0]].append(parsedCO[1])
                    else:
                        fileSystem[currDir][parsedCO[0]] = parsedCO[1]
                    command_or_output = fopen.readline()
                else:
                    print(parsedCO)
                    commandFound = True
                
            # print(fileSystem[currDir])
    
dirSizes = {}

for keys in fileSystem.keys():
    print("Dir ", keys, " contains the following: ", fileSystem[keys])
    for data in fileSystem[keys]:
        print(data) 