import numpy as np
f1 = open("/Users/ckung/Documents/Code/advent_of_code/2020/input.day8")

instruction_list = f1.readlines()

def accumulator_run(instruction_list):

    PC = 0
    acc_value = 0
    max_PC = len(instruction_list)

    execution_count = np.zeros(max_PC,dtype=int)

    while PC < max_PC and execution_count[PC] < 1:
        instruction = instruction_list[PC]
        instruction = instruction.replace("\n","")
        instruction_s = instruction.split(" ")
        #print(instruction_s)

        if instruction_s[0] == "nop":
            #print("Executing nop...")
            execution_count[PC] = execution_count[PC] + 1
            PC = PC + 1

        elif instruction_s[0] == "acc":
            execution_count[PC] = execution_count[PC] + 1
            #print("Executing acc...")
            acc_value = acc_value + int(instruction_s[1])
            #print("New value of acc =", acc_value)
            PC = PC + 1

        elif instruction_s[0] == "jmp":
            execution_count[PC] = execution_count[PC] + 1
            #print("Executing jump instruction...")
            PC = PC + int(instruction_s[1])
            #print("New PC =", PC)

    return acc_value, PC

# *** Part 1 ***
acc_value, PC = accumulator_run(instruction_list)
print("Final Value of accumulator =", acc_value)


max_PC = len(instruction_list)
# *** Part 2 ***
for PC in range(max_PC):
    instruction = instruction_list[PC]
    instruction = instruction.replace("\n","")
    instruction_s = instruction.split(" ")

    execution_count = np.zeros(max_PC,dtype=int)

    if instruction_s[0] == "nop":
        old_instruction = instruction
        new_instruction = "jmp " + instruction_s[1]
        #print(new_instruction)
        instruction_list[PC] = new_instruction
        acc_value, last_PC = accumulator_run(instruction_list)
        if last_PC != max_PC:
            instruction_list[PC] = old_instruction
        else:
            print("Final Value of accumulator =", acc_value)
            break
        
    elif instruction_s[0] == "jmp":
        old_instruction = instruction
        new_instruction = "nop " + instruction_s[1]
        print(new_instruction)
        instruction_list[PC] = new_instruction
        acc_value, last_PC = accumulator_run(instruction_list)
        if last_PC != max_PC:
            instruction_list[PC] = old_instruction
        else:
            print("Final Value of accumulator =", acc_value)
            break