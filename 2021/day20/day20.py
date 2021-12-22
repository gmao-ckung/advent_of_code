import os

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
fopen = open(CURR_DIR+"/input.test","r")
image_data = fopen.readlines()

image_algorithm = image_data[0].replace("\n","")
print(image_algorithm)

num_image_enhancements = 2

