import numpy as np
import os
from support import *

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
fopen = open(CURR_DIR+"/input.day4","r")
inputData = fopen.readlines()

# Making assumption that all bingo boards are 5x5
bingoBoardSize = 5

numbersDrawn = readLineIntoList(inputData[0])

bingoBoard_num, bingoBoard_stamps = createBingoBoards(inputData,bingoBoardSize)

# *** Part 1 ***
for number in numbersDrawn:
    findNumberonBingoBoard(bingoBoard_num, bingoBoard_stamps, int(number))
    isBingo, boardNum, colIndex = checkColsForBingos(bingoBoard_stamps, bingoBoardSize)
    if isBingo:
        printScore(int(number), bingoBoard_num, bingoBoard_stamps, boardNum)
        break
    isBingo, boardNum, rowIndex = checkRowsForBingos(bingoBoard_stamps, bingoBoardSize)
    if isBingo:
        printScore(int(number), bingoBoard_num, bingoBoard_stamps, boardNum)
        break

# *** Part 2 ***
bingoBoard_num, bingoBoard_stamps = createBingoBoards(inputData,bingoBoardSize)

for number in numbersDrawn:
    findNumberonBingoBoard(bingoBoard_num, bingoBoard_stamps, int(number))
    bingoBoardList = checkColsForBingos_v2(bingoBoard_stamps, bingoBoardSize)
    if len(bingoBoardList) > 0:
        if bingoBoard_num.shape[2] > 1:
            bingoBoard_num = np.delete(bingoBoard_num,bingoBoardList,2)
            bingoBoard_stamps = np.delete(bingoBoard_stamps,bingoBoardList,2)
        else:
            printScore(int(number), bingoBoard_num, bingoBoard_stamps, 0)
            break
    bingoBoardList = checkRowsForBingos_v2(bingoBoard_stamps, bingoBoardSize)
    if len(bingoBoardList) > 0:
        if bingoBoard_num.shape[2] > 1:
            bingoBoard_num = np.delete(bingoBoard_num,bingoBoardList,2)
            bingoBoard_stamps = np.delete(bingoBoard_stamps,bingoBoardList,2)
        else:
            printScore(int(number), bingoBoard_num, bingoBoard_stamps, 0)
            break