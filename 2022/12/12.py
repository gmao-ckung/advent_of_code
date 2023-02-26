import os
import sys
from queue import PriorityQueue
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
data = open(CURR_DIR+"/input.12","r")

heights = data.readlines()
height_dict = {}

# Read input into height dictionary (height_dict)
curr_row = 1
for height in heights:
    height = height.replace("\n","")
    curr_col = 1
    for entry in height:
        coord = str(curr_row) + "," + str(curr_col)
        height_dict[coord] = entry
        curr_col += 1
    curr_row += 1

# Define boundaries for map
max_row = curr_row-1
max_col = curr_col-1

# *** Part 1 ***

# Find location of 'S'
for height in height_dict:
    if height_dict[height] == 'S':
        start_loc = height
        break

# print("Start Location =", start_loc)

# Use Dijkstra’s Algorithm to search and find minimum number of steps
# See https://www.redblobgames.com/pathfinding/a-star/introduction.html for description
# to implement Dijkstra's Algorithm

def find_min_steps(height_dict, start_loc, max_row, max_col):

    frontier = PriorityQueue()
    frontier.put(start_loc,0)

    came_from = {}
    cost_so_far = {}
    came_from[start_loc] = None
    cost_so_far[start_loc] = 0

    while(not frontier.empty()):
        curr_loc = frontier.get()
        # print("Current Coord = ", curr_loc)
        # Use 'ord' to translate string to height
        if height_dict[curr_loc] == 'S':
            curr_height = ord('a')
        elif height_dict[curr_loc] == 'E':
            continue
        else:
            curr_height = ord(height_dict[curr_loc])
        # print("****")
        # print('current location letter = ', height_dict[curr_loc])
        # print('current location height = ', curr_height)
        x_coord, y_coord = curr_loc.split(',')
        up_coord = x_coord + ',' + str(int(y_coord)-1)
        dn_coord = x_coord + ',' + str(int(y_coord)+1)
        lf_coord = str(int(x_coord)-1) + ',' + y_coord
        rt_coord = str(int(x_coord)+1) + ',' + y_coord

        neigh_coord = [up_coord, dn_coord, lf_coord, rt_coord]

        for next in neigh_coord:
            x,y = next.split(',')
            if x != '0' and y != '0' and x != str(max_row+1) and y != str(max_col+1):
                # print("Examining neighbor coord : ", next)
                # print("Letter of neighbor coord :", height_dict[next])
                if(height_dict[next] != 'E'):
                    if height_dict[next] == 'S':
                        exam_height = ord('a')
                    else:
                        exam_height = ord(height_dict[next])

                    new_cost = cost_so_far[curr_loc] + 1
                    if(exam_height - curr_height <= 1):
                        if next not in cost_so_far or new_cost < cost_so_far[next]:
                            # print(next)
                            came_from[next] = curr_loc
                            cost_so_far[next] = new_cost
                            frontier.put(next,new_cost)
                else:
                    new_cost = cost_so_far[curr_loc] + 1
                    if(ord('z') - curr_height) <= 1:
                        if next not in cost_so_far or new_cost < cost_so_far[next]:
                            # print(next)
                            cost_so_far[next] = new_cost
                            came_from[next] = curr_loc
                            frontier.put(next,new_cost)

    for height in height_dict:
        if height_dict[height] == 'E':
            location = height
            break

    # Check in case a path doesn't exist
    if location not in cost_so_far:
        return sys.maxsize*2 + 1
    else:
        return cost_so_far[location]

print("Part 1 : Steps = ", find_min_steps(height_dict, start_loc, max_row, max_col))

# *** Part 2 ***
# Note : This may be faster if I implemented A* algorithm

start_loc = []
for height in height_dict:
    if height_dict[height] == 'S' or height_dict[height] == 'a':
        start_loc.append(height)

min_steps = sys.maxsize * 2 + 1

for start in start_loc:
    steps = find_min_steps(height_dict, start, max_row, max_col)

    if steps < min_steps:
        min_steps = steps

print("Part 2 : Steps = ", min_steps)