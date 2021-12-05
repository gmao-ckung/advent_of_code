import numpy as np

def separateViaDelin(commaDelinLine, delin=","):
    # Separate string via delineator
    lineListData = commaDelinLine.split(delin)
    lineListData[-1] = lineListData[-1].split("\n")[0]    # Get rid of the newline        

    return lineListData

def createDirectionList(inputData):
    directionList = []

    # *** Create Direction List ***
    for line in inputData:
        line = separateViaDelin(line, " -> ")
        directionList.append(line)

    return directionList

def findMax_X_Y(directionList):
    # *** Find Min/Max in x and y to create grid ***
    # *** Assume (0,0) is a corner point ***
    maxX = 0
    maxY = 0

    for directions in directionList:
        startPt = separateViaDelin(directions[0],",")
        endPt = separateViaDelin(directions[1],",")

        if int(startPt[0]) > maxX:
            maxX = int(startPt[0])
        
        if int(endPt[0]) > maxX:
            maxX = int(endPt[0])

        if int(startPt[1]) > maxY:
            maxY = int(startPt[1])
        
        if int(endPt[1]) > maxY:
            maxY = int(endPt[1])

    return maxX, maxY

def createMap(maxX, maxY):
    return np.zeros((maxX+1, maxY+1), dtype=int)

def find_horiz_or_vert_dir(directionList, map):
    for directions in directionList:
        startPt = separateViaDelin(directions[0],",")
        endPt = separateViaDelin(directions[1],",")

        x0 = int(startPt[0])
        x1 = int(endPt[0])

        y0 = int(startPt[1])
        y1 = int(endPt[1])

        # Found vertical direction
        if x0 == x1:
            # Going in positive direction
            if y1 - y0 > 0:
                for y in range(y0, y1+1):
                    map[x0, y] += 1

            # Going in negative direction
            if y1 - y0 < 0:
                for y in range(y0, y1-1, -1):
                    map[x0, y] += 1

        if y0 == y1:
            # Going in positive direction
            if x1 - x0 > 0:
                for x in range(x0, x1+1):
                    map[x, y0] += 1

            # Going in negative direction
            if x1 - x0 < 0:
                for x in range(x0, x1-1, -1):
                    map[x, y0] += 1

def find_diag_dir(directionList, map):
    for directions in directionList:
        startPt = separateViaDelin(directions[0],",")
        endPt = separateViaDelin(directions[1],",")

        x0 = int(startPt[0])
        x1 = int(endPt[0])

        y0 = int(startPt[1])
        y1 = int(endPt[1])

        diffX = x1 - x0
        diffY = y1 - y0

        # +x, +y
        if diffX > 0 and diffY > 0:
            x = x0
            y = y0
            while(x <= x1 and y <= y1):
                map[x,y] += 1
                x += 1
                y += 1

        # -x, +y
        if diffX < 0 and diffY > 0:
            x = x0
            y = y0
            while(x >= x1 and y <= y1):
                map[x,y] += 1
                x -= 1
                y += 1

        # +x, -y
        if diffX > 0 and diffY < 0:
            x = x0
            y = y0
            while(x <= x1 and y >= y1):
                map[x,y] += 1
                x += 1
                y -= 1
        
        # -x, -y
        if diffX < 0 and diffY < 0:
            x = x0
            y = y0
            while(x >= x1 and y >= y1):
                map[x,y] +=1
                x -= 1
                y -= 1
