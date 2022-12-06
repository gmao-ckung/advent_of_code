import os
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
fopen = open(CURR_DIR+"/input.05","r")

plan = fopen.readlines()
check = [" ", "[", "]"]

stacks = {}

mode = "read"
for line in plan:
    line = line.replace("\n","")
   
    if mode == "read":
        if line[0] == " " and line[1] == "1":
            mode = "move"
        else:
            for i in range(0,len(line)):
                if(line[i] not in check):
                    # print(int(i/4)+1, line[i])
                    if(int(i/4)+1 not in stacks.keys()):
                        stacks[int(i/4)+1] = [line[i]]
                    else:
                        stacks[int(i/4)+1].append(line[i])

    else:
        if line == "":
            for key in stacks.keys():
                stacks[key].reverse()
        else:
            directions = line.split(" ")
            for moves in range(int(directions[1])):
                moveCrate = stacks[int(directions[3])].pop()
                # print(moveCrate)
                stacks[int(directions[5])].append(moveCrate)
                # print(stacks[int(directions[5])])

msg = ""
for col in range(1,max(stacks.keys())+1):
    msg = msg + stacks[col].pop()

print("Part 1 :", msg)

stacks = {}

mode = "read"
for line in plan:
    line = line.replace("\n","")
   
    if mode == "read":
        if line[0] == " " and line[1] == "1":
            mode = "move"
        else:
            for i in range(0,len(line)):
                if(line[i] not in check):
                    # print(int(i/4)+1, line[i])
                    if(int(i/4)+1 not in stacks.keys()):
                        stacks[int(i/4)+1] = [line[i]]
                    else:
                        stacks[int(i/4)+1].append(line[i])

    else:
        if line == "":
            for key in stacks.keys():
                stacks[key].reverse()

        else:
            directions = line.split(" ")
            # print(directions)
            buffer = []
            for moves in range(int(directions[1])):
                buffer.append(stacks[int(directions[3])].pop())
            # print(buffer)
            for moves in range(len(buffer)):
                stacks[int(directions[5])].append(buffer.pop())
            # print(stacks)

msg = ""
for col in range(1,max(stacks.keys())+1):
    msg = msg + stacks[col].pop()

print("Part 2 :", msg)