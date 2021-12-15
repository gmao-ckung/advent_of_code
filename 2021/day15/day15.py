import os
# import numpy as np
from queue import PriorityQueue
from threading import current_thread

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
fopen = open(CURR_DIR+"/input.test","r")
map = fopen.readlines()

x_len = len(map[0].replace("\n",""))
y_len = len(map)

frontier = []
came_from = {}
cost_so_far = {}

frontier.append(['0,0',int(map[0].replace("\n","")[0])])
came_from['0,0'] = None
cost_so_far['0,0'] = int(map[0].replace("\n","")[0])

print(came_from)

while len(frontier) > 0:
    current_loc = frontier.pop()

    if current_loc[0] == str(x_len-1)+','+str(y_len-1):
        break

    x_coord = int(current_loc[0].split(",")[0])
    y_coord = int(current_loc[0].split(",")[1])

    print()