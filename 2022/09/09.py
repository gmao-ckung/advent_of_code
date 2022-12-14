import os
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
data = open(CURR_DIR+"/input.09","r")

directions = data.readlines()

head_coord = [0, 0]
tail_coord = [0, 0]

def check_dist(head,tail):
    horiz_dist = (head[0] - tail[0])
    vert_dist = head[1] - tail[1]

    return [horiz_dist, vert_dist]

def adjust_tail(head_coord, tail_coord, curr_dists):
    if (abs(curr_dists[0]) + abs(curr_dists[1])) == 3 or (abs(curr_dists[0]) + abs(curr_dists[1])) == 4:
            tail_coord[0] += int(curr_dists[0] / abs(curr_dists[0]))
            tail_coord[1] += int(curr_dists[1] / abs(curr_dists[1]))
    elif(abs(curr_dists[0]) + abs(curr_dists[1])) == 2:
        tail_coord[0] += int((head_coord[0] - tail_coord[0]) / 2)
        tail_coord[1] += int((head_coord[1] - tail_coord[1]) / 2)

def check_if_visited(visited_coord, tail_coord):
    if(str(tail_coord[0])+","+str(tail_coord[1]) not in visited_coord.keys()):
        visited_coord[str(tail_coord[0])+","+str(tail_coord[1])] = 1
    else:
        visited_coord[str(tail_coord[0])+","+str(tail_coord[1])] += 1

# ** Part 1 **

visited_coord = {}
for direction in directions:
    direction = direction.replace("\n","").split(" ")
    # print(direction)
    if direction[0] == 'R':
        for iteration in range(int(direction[1])):
            head_coord[0] += 1
            curr_dists = check_dist(head_coord, tail_coord)
            # print(curr_dists)
            adjust_tail(head_coord,tail_coord, curr_dists)
            # print('head_coord = ', head_coord, ': tail_coord = ', tail_coord)
            check_if_visited(visited_coord, tail_coord)

    elif direction[0] == 'L':
        for interation in range(int(direction[1])):
            head_coord[0] -= 1
            curr_dists = check_dist(head_coord, tail_coord)
            # print(curr_dists)
            adjust_tail(head_coord,tail_coord, curr_dists)
            # print('head_coord = ', head_coord, ': tail_coord = ', tail_coord)
            check_if_visited(visited_coord, tail_coord)
    elif direction[0] == 'U':
        for interaction in range(int(direction[1])):
            head_coord[1] += 1
            curr_dists = check_dist(head_coord, tail_coord)
            # print(curr_dists)
            adjust_tail(head_coord,tail_coord, curr_dists)
            # print('head_coord = ', head_coord, ': tail_coord = ', tail_coord)
            check_if_visited(visited_coord, tail_coord)
    elif direction[0] == 'D':
        for interaction in range(int(direction[1])):
            head_coord[1] -= 1
            curr_dists = check_dist(head_coord, tail_coord)
            # print(curr_dists)
            adjust_tail(head_coord,tail_coord, curr_dists)
            # print('After adjustment : head_coord = ', head_coord, ': tail_coord = ', tail_coord)
            check_if_visited(visited_coord, tail_coord)

print("Number of spots visited by tail = ", len(visited_coord.keys()))

# ** Part 2 **

head_coord = [0, 0]
tail_coord = [[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0]]

visited_coord = {'0,0': 1}
for direction in directions:
    direction = direction.replace("\n","").split(" ")
    # print(direction)
    if direction[0] == 'R':
        for iteration in range(int(direction[1])):
            # print("adjusting head")
            head_coord[0] += 1
            curr_dists = check_dist(head_coord, tail_coord[0])
            # print(curr_dists)
            adjust_tail(head_coord,tail_coord[0], curr_dists)
            # print('head_coord = ', head_coord, ': tail_coord[0] = ', tail_coord[0])
            for tail_index in range(1,9):
                curr_dists = check_dist(tail_coord[tail_index-1], tail_coord[tail_index])
                # print(curr_dists)
                # print('pre: tail_coord[', tail_index-1, '] = ', tail_coord[tail_index-1], ': tail_coord[', tail_index, '] = ', tail_coord[tail_index])
                adjust_tail(tail_coord[tail_index-1],tail_coord[tail_index], curr_dists)
                # print('post: tail_coord[', tail_index-1, '] = ', tail_coord[tail_index-1], ': tail_coord[', tail_index, '] = ', tail_coord[tail_index])
            check_if_visited(visited_coord, tail_coord[8])

    elif direction[0] == 'L':
        for interation in range(int(direction[1])):
            # print("adjusting head")
            head_coord[0] -= 1
            curr_dists = check_dist(head_coord, tail_coord[0])
            # print(curr_dists)
            adjust_tail(head_coord,tail_coord[0], curr_dists)
            # print('head_coord = ', head_coord, ': tail_coord = ', tail_coord)
            for tail_index in range(1,9):
                curr_dists = check_dist(tail_coord[tail_index-1], tail_coord[tail_index])
                adjust_tail(tail_coord[tail_index-1],tail_coord[tail_index], curr_dists)
            check_if_visited(visited_coord, tail_coord[8])
    elif direction[0] == 'U':
        for interaction in range(int(direction[1])):
            # print("adjusting head")
            head_coord[1] += 1
            curr_dists = check_dist(head_coord, tail_coord[0])
            # print(curr_dists)
            adjust_tail(head_coord,tail_coord[0], curr_dists)
            # print('head_coord = ', head_coord, ': tail_coord[0] = ', tail_coord[0])
            for tail_index in range(1,9):
                curr_dists = check_dist(tail_coord[tail_index-1], tail_coord[tail_index])
                # print(curr_dists)
                adjust_tail(tail_coord[tail_index-1],tail_coord[tail_index], curr_dists)
                # print('post: tail_coord[', tail_index-1, '] = ', tail_coord[tail_index-1], ': tail_coord[', tail_index, '] = ', tail_coord[tail_index])
            check_if_visited(visited_coord, tail_coord[8])
    elif direction[0] == 'D':
        for interaction in range(int(direction[1])):
            # print("adjusting head")
            head_coord[1] -= 1
            curr_dists = check_dist(head_coord, tail_coord[0])
            # print(curr_dists)
            adjust_tail(head_coord,tail_coord[0], curr_dists)
            # print('After adjustment : head_coord = ', head_coord, ': tail_coord = ', tail_coord)
            for tail_index in range(1,9):
                curr_dists = check_dist(tail_coord[tail_index-1], tail_coord[tail_index])
                adjust_tail(tail_coord[tail_index-1],tail_coord[tail_index], curr_dists)
            check_if_visited(visited_coord, tail_coord[8])

print("Number of spots visited by tail = ", len(visited_coord.keys()))