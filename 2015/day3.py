# This solution uses a Python dictionary label to check whether a coordinate has been visited

f1 = open("/home/ckung/Code/Advent_Of_Code/2015/input.day3")

directions = f1.readline()
directions = directions.replace("\n","")
#print(directions)

dir_dict = {"00" : "present"}
x_coord = 0
y_coord = 0

num_houses = 1

# *** Part 1 ***

for i in range(len(directions)):
    if(directions[i] == '>'):
        x_coord = x_coord+1
    elif(directions[i] == '<'):
        x_coord = x_coord-1
    elif(directions[i] == '^'):
        y_coord = y_coord+1
    elif(directions[i] == 'v'):
        y_coord = y_coord-1

    str_coord = str(x_coord)+str(y_coord)

    if str_coord not in dir_dict:
        dir_dict[str_coord] = "present"
        num_houses = num_houses + 1

print("Number of houses visited =", num_houses)

# *** Part 2 ***

x_coord_S1 = 0
y_coord_S1 = 0
x_coord_S2 = 0
y_coord_S2 = 0

num_houses = 1
dir_dict = {"00" : "present"}

for i in range(len(directions)):
    if i%2 == 0:
        if(directions[i] == '>'):
            x_coord_S1 = x_coord_S1+1
        elif(directions[i] == '<'):
            x_coord_S1 = x_coord_S1-1
        elif(directions[i] == '^'):
            y_coord_S1 = y_coord_S1+1
        elif(directions[i] == 'v'):
            y_coord_S1 = y_coord_S1-1

        str_coord = str(x_coord_S1)+str(y_coord_S1)
        if str_coord not in dir_dict:
            dir_dict[str_coord] = "present"
            num_houses = num_houses + 1
    else:
        if(directions[i] == '>'):
            x_coord_S2 = x_coord_S2+1
        elif(directions[i] == '<'):
            x_coord_S2 = x_coord_S2-1
        elif(directions[i] == '^'):
            y_coord_S2 = y_coord_S2+1
        elif(directions[i] == 'v'):
            y_coord_S2 = y_coord_S2-1

        str_coord = str(x_coord_S2)+str(y_coord_S2)
        if str_coord not in dir_dict:
            dir_dict[str_coord] = "present"
            num_houses = num_houses + 1

print("Number of houses visited by santa and robo-santa =", num_houses)