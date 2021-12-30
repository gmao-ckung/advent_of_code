import os

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
fopen = open(CURR_DIR+"/input.day20","r")
image_data = fopen.readlines()

image_algorithm = image_data[0].replace("\n","")
# print(image_algorithm)

num_image_enhancements = 2

image_dict = {}
for i in range(2, len(image_data)):
    y_index = i-2
    image_line = image_data[i].replace("\n","")
    for i in range(len(image_line)):
        if image_line[i] == "#":
            if str(i)+","+str(y_index) not in image_dict.keys():
                image_dict[str(i)+","+str(y_index)] = 1

print(image_dict)

x_min = 0
x_max = len(image_line)

y_min = 0
y_max = len(image_data) - 2


for steps in range(num_image_enhancements):

    new_image_dict = {}

    for key in image_dict.keys():
        coord = key.split(",")
        coord_x = int(coord[0])
        coord_y = int(coord[1])

        # Note that my coordinate system is normal x but inverse y
        # ---------> +x
        # |                     NW  N  NE
        # |                      W  C   E
        # |                     SW  S  SE
        # v +y
        key_NW = str(coord_x-1)+","+str(coord_y-1)
        key_N  = str(coord_x)+","+str(coord_y-1)
        key_NE = str(coord_x+1)+","+str(coord_y-1)
        key_W  = str(coord_x-1)+","+str(coord_y)
        key_C  = key
        key_E  = str(coord_x+1)+","+str(coord_y)
        key_SW = str(coord_x-1)+","+str(coord_y+1)
        key_S  = str(coord_x)+","+str(coord_y+1)
        key_SE = str(coord_x+1)+","+str(coord_y+1)

        # The NW pixel will get a value of 1
        if key_NW not in new_image_dict.keys():
            new_image_dict[key_NW] = 1
        else:
            new_image_dict[key_NW] += 1

        # The N pixel will get a value of 2
        if key_N not in new_image_dict.keys():
            new_image_dict[key_N] = 2
        else:
            new_image_dict[key_N] += 2

        # The NE pixel will get a value of 4
        if key_NE not in new_image_dict.keys():
            new_image_dict[key_NE] = 4
        else:
            new_image_dict[key_NE] += 4

        # The W pixel will get a value of 8
        if key_W not in new_image_dict.keys():
            new_image_dict[key_W] = 8
        else:
            new_image_dict[key_W] += 8

        # The center pixel will get a value of 16
        if key_C not in new_image_dict.keys():
            new_image_dict[key_C] = 16
        else:
            new_image_dict[key_C] += 16

        # The E pixel will get a value of 32
        if key_E not in new_image_dict.keys():
            new_image_dict[key_E] = 32
        else:
            new_image_dict[key_E] += 32

        # The SW pixel will get a value of 64
        if key_SW not in new_image_dict.keys():
            new_image_dict[key_SW] = 64
        else:
            new_image_dict[key_SW] += 64

        # The S pixel will get a value of 128
        if key_S not in new_image_dict.keys():
            new_image_dict[key_S] = 128
        else:
            new_image_dict[key_S] += 128

        # The SE pixel will get a value of 256
        if key_SE not in new_image_dict.keys():
            new_image_dict[key_SE] = 256
        else:
            new_image_dict[key_SE] += 256

    if image_algorithm[0] == "#":
        print("DAMN IT")
        # Search along "border" for potential "zero" grids
        # North Border Search
        init_x = x_min
        while(init_x <= x_max-3):
            key_L = str(init_x)+",0"
            key_M = str(init_x+1) +",0"
            key_R = str(init_x+2)+",0"

            if key_L not in image_dict.keys() and key_M not in image_dict.keys() and key_R not in image_dict.keys():
                zero_grid_key = str(init_x+1)+","+str(y_min-1)
                if zero_grid_key not in new_image_dict.keys():
                    new_image_dict[zero_grid_key] = 0
                    print(zero_grid_key)
            init_x += 1

        print("STOP")
        # It looks like I can search along the border for "missing" entries in new_image_dict that can be dictated to be 0

    image_dict = {}
    for key in new_image_dict.keys():
        if image_algorithm[new_image_dict[key]] == "#":
            image_dict[key] = 1

    print("Length of image_dict = ", len(image_dict))