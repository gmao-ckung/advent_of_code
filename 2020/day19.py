import os
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
print(CURR_DIR)
f1 = open(CURR_DIR+"/input.day18")
expressions = f1.readlines()
