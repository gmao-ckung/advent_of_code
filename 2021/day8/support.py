def separateViaDelin(commaDelinLine, delin=","):
    # Separate string via delineator
    lineListData = commaDelinLine.split(delin)
    lineListData[-1] = lineListData[-1].split("\n")[0]    # Get rid of the newline        

    return lineListData[-1]

def grabOutputDigits(inputList):
    outputDigits = []
    for line in inputList:
        outputData = separateViaDelin(line,"|")
        outputDigits.append(outputData)
    return outputDigits