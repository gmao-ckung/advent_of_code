import os
import math
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
print(CURR_DIR)
f1 = open(CURR_DIR+"/input.test")
data = f1.readlines()

YT = False # Flag for "your ticket" info
NT = False # Flag for "nearby tickets" info

for line in data:
    line=line.replace("\n","")

    if YT:
        your_ticket_numbers = [int(i) for i in line.split(",")]
        YT = False

    if line == "your ticket:":
        YT = True
    elif line == "nearby tickets:":
        NT = True