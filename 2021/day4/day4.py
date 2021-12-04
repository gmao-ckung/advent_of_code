import numpy as np
import os
from support import *

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
fopen = open(CURR_DIR+"/input.day4","r")
inputData = fopen.readlines()

# Making assumption that all bingo boards are 5x5
bingoBoardSize = 5

# The first line in the input file has the drawn numbers
numbersDrawn = readLineIntoList(inputData[0])

# Create 3D array of bingo boards where the 3rd axis delineates each distinct board
# There are two distinct boards: A "number" board and a "stamping" board
bingoBoard_num, bingoBoard_stamps = createBingoBoards(inputData,bingoBoardSize)

# *** Part 1 ***

for number in numbersDrawn:
    bingoBoard_stamps = findNumberonBingoBoard(bingoBoard_num, bingoBoard_stamps, int(number))

    isBingo, boardNum, colIndex = checkColsForBingos(bingoBoard_stamps, bingoBoardSize)
    if isBingo:
        printScore(int(number), bingoBoard_num, bingoBoard_stamps, boardNum)
        break
    isBingo, boardNum, rowIndex = checkRowsForBingos(bingoBoard_stamps, bingoBoardSize)
    if isBingo:
        printScore(int(number), bingoBoard_num, bingoBoard_stamps, boardNum)
        break