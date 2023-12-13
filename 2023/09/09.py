import os

# Read input file from current directory
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
file = open(CURR_DIR+"/input.in","r")

history = file.read().splitlines()

def diff_history_1(history):
    new_history = []
    for i in range(len(history)):
        if(i != len(history)-1):
            new_history.append(history[i+1]-history[i])

    # print(new_history)
    if(all(i == 0 for i in new_history)):
        return new_history
    else:
        next_history = diff_history_1(new_history)

    new_history.append(next_history[-1] + new_history[-1])

    # print(new_history)
    return new_history

def diff_history_2(history):
    new_history = []
    for i in range(len(history)):
        if(i != len(history)-1):
            new_history.append(history[i+1]-history[i])

    if(all(i == 0 for i in new_history)):
        return new_history
    else:
        next_history = diff_history_2(new_history)

    new_history.insert(0,-next_history[0] + new_history[0])
    # print(new_history)
    return new_history

curr_sum = 0
for curr_history in history:
    curr_history = curr_history.split()
    for i in range(len(curr_history)):
        curr_history[i] = int(curr_history[i])

    # print(curr_history)

    next_history = diff_history_1(curr_history)

    curr_history.append(next_history[-1] + curr_history[-1])
    # print(curr_history)

    curr_sum += curr_history[-1]

print(f'Part 1 : Sum = {curr_sum}')

curr_sum = 0
for curr_history in history:
    curr_history = curr_history.split()
    for i in range(len(curr_history)):
        curr_history[i] = int(curr_history[i])

    # print(curr_history)

    next_history = diff_history_2(curr_history)

    curr_history.insert(0,-next_history[0] + curr_history[0])
    # print(curr_history)

    curr_sum += curr_history[0]

print(f'Part 2 : Sum = {curr_sum}')