import os
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
data = open(CURR_DIR+"/input.10","r")

instructions = data.readlines()

cycle_checks = [20, 60, 100, 140, 180, 220]

# ** Part 1 **
signal_list = []

cycle_count = 0
reg_value = 1
for instruction in instructions:
    instruction = instruction.replace("\n","")
    instruction = instruction.split(" ")
    if(instruction[0] == 'noop'):
        cycle_count += 1
        if cycle_count in cycle_checks:
            # print("current cycle = ", cycle_count)
            # print("register value = ", reg_value)
            # print("singal strength = ", cycle_count * reg_value)
            signal_list.append(cycle_count * reg_value)
    elif(instruction[0] == 'addx'):
        for i in range(2):
            cycle_count += 1
            if cycle_count in cycle_checks:
                # print("current cycle = ", cycle_count)
                # print("register value = ", reg_value)
                # print("singal strength = ", cycle_count * reg_value)
                signal_list.append(cycle_count * reg_value)
        reg_value += int(instruction[1])

signal_sum = 0

for signal in signal_list:
    signal_sum += signal

print("signal sum = ", signal_sum)

# ** Part 2 **
cycle_count = 0
reg_value = 1
CRT_signal = ""
screen = []

for instruction in instructions:
    instruction = instruction.replace("\n","").split(" ")
    # print(instruction)
    # print("reg_value = ", reg_value)
    if(instruction[0] == "noop"):
        cycle_count += 1
        # print('Current in cycle ', cycle_count)
        if(cycle_count in [reg_value, reg_value+1, reg_value+2]):
            CRT_signal += '#'
        else:
            CRT_signal += "."

        if cycle_count == 40:
            screen.append(CRT_signal)
            CRT_signal = ""
            cycle_count = 0
    elif(instruction[0] == 'addx'):
        for i in range(2):
            cycle_count += 1
            # print('Current in cycle ', cycle_count)
            if(cycle_count in [reg_value, reg_value+1, reg_value+2]):
                CRT_signal += '#'
            else:
                CRT_signal += "."

            if cycle_count == 40:
                screen.append(CRT_signal)
                CRT_signal = ""
                cycle_count = 0
        reg_value += int(instruction[1])
    # print(CRT_signal)

for line in screen:
    print(line)