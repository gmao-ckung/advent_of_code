import numpy as np
import os
# from support import *

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
fopen = open(CURR_DIR+"/input.day10","r")
initialDataList = fopen.readlines()

def checkSyntax(data, currentStack, currentIdx):
    noErrorFound = True
    while(currentIdx < len(data) and noErrorFound == True):

        if data[currentIdx] == "(" or \
            data[currentIdx] == "[" or \
            data[currentIdx] == "{" or \
            data[currentIdx] == "<":
            noErrorFound = True
            currentStack.append(data[currentIdx])
            currentIdx += 1            

        elif data[currentIdx] == ")":
            if currentStack[-1] == "(":
                del currentStack[-1]
                currentIdx += 1
            else:
                print("Error detected: Found", data[currentIdx], "for", currentStack[-1])
                currentStack.append(data[currentIdx])
                return False, currentStack
        
        elif data[currentIdx] == "]":
            if currentStack[-1] == "[":
                del currentStack[-1]
                currentIdx += 1
            else:
                print("Error detected: Found", data[currentIdx], "for", currentStack[-1])
                currentStack.append(data[currentIdx])
                return False, currentStack

        elif data[currentIdx] == "}":
            if currentStack[-1] == "{":
                del currentStack[-1]
                currentIdx += 1
            else:
                print("Error detected: Found", data[currentIdx], "for", currentStack[-1])
                currentStack.append(data[currentIdx])
                return False, currentStack

        elif data[currentIdx] == ">":
            if currentStack[-1] == "<":
                del currentStack[-1]
                currentIdx += 1
            else:
                print("Error detected: Found", data[currentIdx], "for", currentStack[-1])
                currentStack.append(data[currentIdx])
                return False, currentStack

    return True, currentStack

syntax_points = 0

for data in initialDataList:
    data = data[:-1]
    currentStack = []
    currentIdx = 0
    noErrorFound, currentStack = checkSyntax(data,currentStack,currentIdx)

    if ~noErrorFound:
        if currentStack[-1] == ")":
            syntax_points += 3
        elif currentStack[-1] == "]":
            syntax_points += 57
        elif currentStack[-1] == "}":
            syntax_points += 1197
        elif currentStack[-1] == ">":
            syntax_points += 25137


print("Part 1: Syntax Points =", syntax_points)