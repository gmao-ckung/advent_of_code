import os

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
fopen = open(CURR_DIR+"/input.day15","r")
map = fopen.readlines()

def get_risk(x_coord, y_coord, x_len, y_len, map):
    scaled_x_coord = x_coord%x_len
    scaled_y_coord = y_coord%y_len
    tile_coord_x = int(x_coord/x_len)
    tile_coord_y = int(y_coord/y_len)

    starting_risk = int(map[scaled_y_coord].replace("\n","")[scaled_x_coord])
    scaled_risk = starting_risk + tile_coord_x + tile_coord_y
    if scaled_risk > 9:
        scaled_risk -= 9
    return scaled_risk

def return_string_coord(x_coord, y_coord):
    return str(x_coord)+","+str(y_coord)

def sort_frontier_value(location):
    return location[1]

x_len = len(map[0].replace("\n",""))
y_len = len(map)

frontier = []
cost_so_far = {}

frontier.append(['0,0',0])
cost_so_far['0,0'] = 0

# Dijkstra Algorithm
while len(frontier) > 0:
    # Note : The sort lets you grab the next lowest risk
    frontier.sort(reverse=True, key=sort_frontier_value)
    current_loc = frontier.pop()

    if current_loc[0] == str(x_len-1)+','+str(y_len-1):
        break

    x_coord = int(current_loc[0].split(",")[0])
    y_coord = int(current_loc[0].split(",")[1])

    neighbors = [[x_coord-1,y_coord],
                 [x_coord+1,y_coord],
                 [x_coord,y_coord-1],
                 [x_coord,y_coord+1]]

    for neighbor in neighbors:
        if neighbor[0] >= 0 and neighbor[0] < x_len and neighbor[1] >= 0 and neighbor[1] < y_len:
            risk_value = get_risk(neighbor[0], neighbor[1], x_len, y_len, map)
            new_cost = cost_so_far[current_loc[0]] + risk_value

            coord_string = return_string_coord(neighbor[0],neighbor[1])
            if coord_string not in cost_so_far.keys() or new_cost < cost_so_far[coord_string]:
                cost_so_far[coord_string] = new_cost
                frontier.append([coord_string, new_cost])
        
print("Part 1 : Lower risk path total =", cost_so_far[str(x_len-1)+","+str(y_len-1)])

frontier = []
cost_so_far = {}

frontier.append(['0,0',0])
cost_so_far['0,0'] = 0

scaled_x_len = x_len*5
scaled_y_len = y_len*5

# Dijkstra Algorithm
while len(frontier) > 0:
    frontier.sort(reverse=True, key=sort_frontier_value)
    current_loc = frontier.pop()

    # print('current location = ', current_loc)

    if current_loc[0] == str(scaled_x_len-1)+','+str(scaled_y_len-1):
        break

    x_coord = int(current_loc[0].split(",")[0])
    y_coord = int(current_loc[0].split(",")[1])

    neighbors = [[x_coord-1,y_coord],
                 [x_coord+1,y_coord],
                 [x_coord,y_coord-1],
                 [x_coord,y_coord+1]]

    for neighbor in neighbors:
        if neighbor[0] >= 0 and neighbor[0] < scaled_x_len and neighbor[1] >= 0 and neighbor[1] < scaled_y_len:
            risk_value = get_risk(neighbor[0], neighbor[1], x_len, y_len, map)
            new_cost = cost_so_far[current_loc[0]] + risk_value

            coord_string = return_string_coord(neighbor[0],neighbor[1])
            if coord_string not in cost_so_far.keys() or new_cost < cost_so_far[coord_string]:
                cost_so_far[coord_string] = new_cost
                frontier.append([coord_string, new_cost])
        
print("Part 2 : Lower risk path total =", cost_so_far[str(scaled_x_len-1)+","+str(scaled_y_len-1)])