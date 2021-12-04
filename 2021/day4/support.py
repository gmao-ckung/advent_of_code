import numpy as np

def readLineIntoList(commaDelinLine, delin=","):
    # Separate numbers via delineator into a list
    if delin == ",":
        lineListData = commaDelinLine.split(delin)
        lineListData[-1] = lineListData[-1].split("\n")[0]    # Get rid of the newline        
    else:
        lineListData = commaDelinLine.split()
    
    return lineListData

def createBingoBoards(inputData,bingoBoardSize):
    # From the number of lines in the input file, we can figure out number of
    # bingo boards
    numOfBoards = int((len(inputData)-1) / (bingoBoardSize+1))

    # Creating two 3D array of bingo boards where the 3rd axis delineates each distinct board
    # The first bingo board contains the numbers
    bingoBoards_num = np.zeros((bingoBoardSize,bingoBoardSize,numOfBoards),dtype=int)
    # The second bingo board is the "stamp" board on whether a number was found
    bingoBoards_stamps = np.zeros((bingoBoardSize,bingoBoardSize,numOfBoards),dtype=bool)

    for line in range(2,len(inputData)):
        adjustLineIndex = line - 2
        currentRowToWrite = adjustLineIndex%(bingoBoardSize+1)
        currentBoardIndex = int(adjustLineIndex/(bingoBoardSize+1))

        if currentRowToWrite != bingoBoardSize:
            lineData = readLineIntoList(inputData[line], " ")
            for col in range(bingoBoardSize):
                bingoBoards_num[currentRowToWrite,col,currentBoardIndex] = int(lineData[col])

    return bingoBoards_num, bingoBoards_stamps

def applyNumToBingoBoard(bingoBoard_num, bingoBoard_stamp, number):
    bingoBoard_stamp = np.logical_or((bingoBoard_num == number), bingoBoard_stamp)
    return bingoBoard_stamp

def findNumberonBingoBoard(bingoBoard_num, bingoBoard_stamps, number):
    for boardIndex in range(bingoBoard_num.shape[2]):
        bingoBoard_stamps[:,:,boardIndex] = applyNumToBingoBoard(bingoBoard_num[:,:,boardIndex],
                                                                 bingoBoard_stamps[:,:,boardIndex], 
                                                                 int(number))
    return bingoBoard_stamps

def checkColsForBingos(bingoBoard_stamp, bingoBoardSize):
    for boardIndex in range(bingoBoard_stamp.shape[2]):
        checkColBingo = np.where(sum(bingoBoard_stamp[:,:,boardIndex]) == bingoBoardSize)
        if checkColBingo[0].shape[0] > 0:
            return True, boardIndex, checkColBingo[0][0]

    return False, None, None

def checkColsForBingos_v2(bingoBoard_stamp, bingoBoardSize):
    boardBingoList = []
    for boardIndex in range(bingoBoard_stamp.shape[2]):
        checkColBingo = np.where(sum(bingoBoard_stamp[:,:,boardIndex]) == bingoBoardSize)
        if checkColBingo[0].shape[0] > 0:
            boardBingoList.append(boardIndex)

    return boardBingoList

def checkRowsForBingos(bingoBoard_stamp, bingoBoardSize):
    bingoBoard_stamp_T = np.transpose(bingoBoard_stamp,axes=[1,0,2])
    isBingo, boardNum, RowNum = checkColsForBingos(bingoBoard_stamp_T, bingoBoardSize)

    return isBingo, boardNum, RowNum

def checkRowsForBingos_v2(bingoBoard_stamp, bingoBoardSize):
    bingoBoard_stamp_T = np.transpose(bingoBoard_stamp,axes=[1,0,2])
    boardBingoList = checkColsForBingos_v2(bingoBoard_stamp_T, bingoBoardSize)

    return boardBingoList

def checkDiagForBingos(bingoBoard_stamp, bingoBoardSize):
    for boardIndex in range(bingoBoard_stamp.shape[2]):
        if np.trace(bingoBoard_stamp[:,:,boardIndex]) == bingoBoardSize:
            return True, boardIndex, 0
        if np.trace(np.fliplr(bingoBoard_stamp[:,:,boardIndex])) == bingoBoardSize:
            return True, boardIndex, 1

    return False, None, None

def sumUnmarkedNum(bingoBoard_num, bingoBoard_stamp):
    return sum(bingoBoard_num[~np.array(bingoBoard_stamp)])

def printScore(number, bingoBoard_num, bingoBoard_stamp, boardIndex):
    print("The score is", number * sumUnmarkedNum(bingoBoard_num[:,:,boardIndex], bingoBoard_stamp[:,:,boardIndex]))