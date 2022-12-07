import os
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
fopen = open(CURR_DIR+"/input.06","r")

signals = fopen.readlines()

# *** Part 1***

for signal in signals:
    marker = []
    index = 0
    for letter in signal:
        if(len(marker) < 4):
            marker.append(letter)
            # print(marker)
            index += 1
        else:
            # print(set(marker))
            if(len(set(marker)) == len(marker)):
                print("Part 1 : First Marker found after character ", index)
                break
            else:
                marker.pop(0)
                marker.append(letter)
                # print(marker)
                index += 1

# *** Part 2***

for signal in signals:
    marker = []
    index = 0
    for letter in signal:
        if(len(marker) < 14):
            marker.append(letter)
            # print(marker)
            index += 1
        else:
            # print(set(marker))
            if(len(set(marker)) == len(marker)):
                print("Part 2 : First Marker found after character ", index)
                break
            else:
                marker.pop(0)
                marker.append(letter)
                # print(marker)
                index += 1