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

