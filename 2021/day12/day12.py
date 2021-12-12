import os
import numpy as np

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
fopen = open(CURR_DIR+"/input.day12","r")
allPaths = fopen.readlines()

path_Dict = {}


for path in allPaths:
    path = path.replace("\n","")
    print(path)
    connection_pair = path.split("-")
    if connection_pair[0] not in path_Dict.keys() and connection_pair[0] != "end":
        if connection_pair[1] != "start":
            path_Dict[connection_pair[0]] = [connection_pair[1]]
    else:
        if connection_pair[1] != "start" and connection_pair[0] != "end":
            path_Dict[connection_pair[0]].append(connection_pair[1])
    
    if connection_pair[1] not in path_Dict.keys() and connection_pair[1] != "end":
        if connection_pair[0] != "start":
            path_Dict[connection_pair[1]] = [connection_pair[0]]
    else:
        if connection_pair[0] != "start" and connection_pair[1] != "end":
            path_Dict[connection_pair[1]].append(connection_pair[0])

    
print(path_Dict)

possible_paths = []

def search_path_pt1(startPt, path_Dict, currPath, possible_paths):
    # print("**************")
    # print("startPt =", startPt)
    # print("currPath =", currPath)
    for nextPt in path_Dict[startPt]:
        # print("nextPt =", nextPt)
        if nextPt == "end":
            possible_paths.append(currPath + ["end"])
            # print(currPath + ["end"])
        elif nextPt.isupper():
            search_path_pt1(nextPt, path_Dict, currPath+[nextPt], possible_paths)
        elif nextPt.islower():
            if nextPt not in currPath:
                search_path_pt1(nextPt, path_Dict, currPath+[nextPt], possible_paths)
    # print("going back up")

def search_path_pt2(startPt, path_Dict, currPath, possible_paths, checkKey):
    # print("**************")
    # print("startPt =", startPt)
    # print("currPath =", currPath)
    for nextPt in path_Dict[startPt]:
        # print("nextPt =", nextPt)
        if nextPt == "end":
            if currPath+["end"] not in possible_paths:
                possible_paths.append(currPath + ["end"])
                # print(currPath + ["end"])
        elif nextPt.isupper():
            search_path_pt2(nextPt, path_Dict, currPath+[nextPt], possible_paths, checkKey)
        elif nextPt.islower():
            if nextPt not in currPath or (nextPt in currPath and currPath.count(nextPt) < 2 and nextPt == checkKey):
                search_path_pt2(nextPt, path_Dict, currPath+[nextPt], possible_paths, checkKey)
    # print("going back up")

search_path_pt1("start", path_Dict, [], possible_paths)

print("Part 1: There are", len(possible_paths), "possible paths")

possible_paths = []

for currKey in path_Dict.keys():
    if currKey.islower() and currKey != "start" and currKey != "end":
        checkKey = currKey
        search_path_pt2("start", path_Dict, [], possible_paths, checkKey)
print("Part 2: There are", len(possible_paths), "possible paths")
