def separateViaDelin(commaDelinLine, delin=",", part=-1):
    # Separate string via delineator
    lineListData = commaDelinLine.split(delin)
    lineListData[-1] = lineListData[-1].split("\n")[0]    # Get rid of the newline        

    return lineListData[0], lineListData[1]

def grabDigits(inputList):
    patternDigits = []
    outputDigits = []
    for line in inputList:
        patternData, outputData = separateViaDelin(line,"|")
        patternDigits.append(patternData)
        outputDigits.append(outputData)
    return patternDigits, outputDigits

def findPattern(input, numSeg):
    return [x for x in input.split(" ") if len(x) == numSeg]

def createList(input):
    return [x for x in input.split(" ") if len(x) != 0]

def create_init_pattern_dict(patternD, outputD):
    one_pattern = findPattern(patternD, 2)
    # if len(one_pattern) == 0:
    #     one_pattern = findPattern(outputD, 2)
    seven_pattern = findPattern(patternD, 3)
    # if len(seven_pattern) == 0:
    #     seven_pattern = findPattern(outputD, 3)
    four_pattern = findPattern(patternD, 4)
    # if len(four_pattern) == 0:
    #     four_pattern = findPattern(outputD, 4)
    eight_pattern = findPattern(patternD,7)
    # if len(eight_pattern) == 0:
    #     eight_pattern = findPattern(outputD,7)

    pattern_dict = {1 : one_pattern[0], 7 : seven_pattern[0], 4 : four_pattern[0], 8: eight_pattern[0]}

    return pattern_dict