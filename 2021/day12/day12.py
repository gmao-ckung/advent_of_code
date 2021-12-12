import os

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
fopen = open(CURR_DIR+"/input.day12","r")
allPaths = fopen.readlines()

def search_path(startPt, path_Dict, currPath, possible_paths, checkKey=""):
    for nextPt in path_Dict[startPt]:
        if nextPt == "end":
            if currPath+["end"] not in possible_paths:
                possible_paths.append(currPath + ["end"])
        elif nextPt.isupper():
            search_path(nextPt, path_Dict, currPath+[nextPt], possible_paths, checkKey)
        elif nextPt.islower():
            if nextPt not in currPath or (nextPt in currPath and currPath.count(nextPt) < 2 and nextPt == checkKey):
                search_path(nextPt, path_Dict, currPath+[nextPt], possible_paths, checkKey)

path_Dict = {}

for path in allPaths:
    path = path.replace("\n","")
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

possible_paths = []

search_path("start", path_Dict, [], possible_paths)

print("Part 1: There are", len(possible_paths), "possible paths")

possible_paths = []

for currKey in path_Dict.keys():
    if currKey.islower() and currKey != "start" and currKey != "end":
        checkKey = currKey
        search_path("start", path_Dict, [], possible_paths, checkKey)
print("Part 2: There are", len(possible_paths), "possible paths")
