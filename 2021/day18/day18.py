import os

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
fopen = open(CURR_DIR+"/input.test","r")
snailfishes = fopen.readlines()

# Sum up initial snailfishes into a string
snailfish_string = ""
for snailfish in snailfishes:
    snailfish = snailfish.replace("\n","")
    if snailfish_string == "":
        snailfish_string += snailfish
    else:
        snailfish_string = "[" + snailfish_string + "," + snailfish + "]"

print(snailfish_string)

def find_snailfish_pair(snailfish_string, curr_index, level):
    snailfish_pair = ""
    while(snailfish_string[curr_index] != "]"):
        if snailfish_string[curr_index] == "[":
            level += 1
            snailfish_pair += "["
            snailfish_pair += find_snailfish_pair(snailfish_string, curr_index, level)
        else:
            snailfish_pair += snailfish_string[curr_index]
        curr_index += 1

    return snailfish_pair+"]"

curr_index = 0
reduced_snailfish = ""
level = 0
while curr_index < len(snailfish_string):
    if snailfish_string[curr_index] == "[":
        level += 1
        reduced_snailfish += "["

    elif snailfish_string[curr_index] == "]":
        level -= 1
        reduced_snailfish += "]"
    else:
        inner_pair = ""

        while(snailfish_string[curr_index] != "]"):

