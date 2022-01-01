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

# print(image_dict)

x_min = 0
x_max = len(image_line)

y_min = 0
y_max = len(image_data) - 2

def pixel_light_search(new_image_dict, index_x, index_y, 
                       key_NW_flag=False, key_N_flag=False, key_NE_flag=False, 
                       key_W_flag=False, key_C_flag=False, key_E_flag=False, 
                       key_SW_flag=False, key_S_flag=False, key_SE_flag=False):

    # Note that my coordinate system is normal x but inverse y
    # ---------> +x
    # |                     NW  N  NE
    # |                      W  C   E
    # |                     SW  S  SE
    # v +y

    key_NW = str(index_x-1)+","+str(index_y-1)
    key_N  = str(index_x)+","+str(index_y-1)
    key_NE = str(index_x+1)+","+str(index_y-1)
    key_W  = str(index_x-1)+","+str(index_y)
    key_C  = str(index_x)+","+str(index_y)
    key_E  = str(index_x+1)+","+str(index_y)
    key_SW = str(index_x-1)+","+str(index_y+1)
    key_S  = str(index_x)+","+str(index_y+1)
    key_SE = str(index_x+1)+","+str(index_y+1)

    if key_NW_flag == True:
        # The NW pixel will get a value of 1
        if key_NW not in new_image_dict.keys():
            new_image_dict[key_NW] = 1
        else:
            new_image_dict[key_NW] += 1

    if key_N_flag == True:
        # The N pixel will get a value of 2
        if key_N not in new_image_dict.keys():
            new_image_dict[key_N] = 2
        else:
            new_image_dict[key_N] += 2

    if key_NE_flag == True:
        # The NE pixel will get a value of 4
        if key_NE not in new_image_dict.keys():
            new_image_dict[key_NE] = 4
        else:
            new_image_dict[key_NE] += 4

    if key_W_flag == True:
        # The W pixel will get a value of 8
        if key_W not in new_image_dict.keys():
            new_image_dict[key_W] = 8
        else:
            new_image_dict[key_W] += 8

    if key_C_flag == True:
        # The center pixel will get a value of 16
        if key_C not in new_image_dict.keys():
            new_image_dict[key_C] = 16
        else:
            new_image_dict[key_C] += 16

    if key_E_flag == True:
        # The E pixel will get a value of 32
        if key_E not in new_image_dict.keys():
            new_image_dict[key_E] = 32
        else:
            new_image_dict[key_E] += 32

    if key_SW_flag == True:
        # The SW pixel will get a value of 64
        if key_SW not in new_image_dict.keys():
            new_image_dict[key_SW] = 64
        else:
            new_image_dict[key_SW] += 64

    if key_S_flag == True:
        # The S pixel will get a value of 128
        if key_S not in new_image_dict.keys():
            new_image_dict[key_S] = 128
        else:
            new_image_dict[key_S] += 128

    if key_SE_flag == True:
        # The SE pixel will get a value of 256
        if key_SE not in new_image_dict.keys():
            new_image_dict[key_SE] = 256
        else:
            new_image_dict[key_SE] += 256

for steps in range(num_image_enhancements):

    new_image_dict = {}

    for key in image_dict.keys():
        coord = key.split(",")
        coord_x = int(coord[0])
        coord_y = int(coord[1])

        pixel_light_search(new_image_dict, coord_x, coord_y, key_NW_flag=True, key_N_flag=True,
                            key_NE_flag=True, key_W_flag=True, key_C_flag=True,
                            key_E_flag=True, key_SW_flag=True, key_S_flag=True,
                            key_SE_flag=True)

    if image_algorithm[0] == "#":
        # Search along first "border" outside of the image for potential "zero" grids when steps is even since the "infinite" area
        # around the image will be zeros
        if steps%2 == 0:
            # North Border Search
            y_min_index = y_min - 1
            for x_index in range(x_min,x_max):
                search_key = str(x_index)+","+str(y_min_index)
                if search_key not in new_image_dict.keys():
                    # print(search_key, "is a 0 spot")
                    new_image_dict[search_key] = 0

            # West Border Search
            x_min_index = x_min - 1
            for y_index in range(y_min,y_max):
                search_key = str(x_min_index)+","+str(y_index)
                if search_key not in new_image_dict.keys():
                    # print(search_key, "is a 0 spot")
                    new_image_dict[search_key] = 0

            # East Border Search
            x_max_index = x_max
            for y_index in range(y_min,y_max):
                search_key = str(x_max_index)+","+str(y_index)
                if search_key not in new_image_dict.keys():
                    # print(search_key, "is a 0 spot")
                    new_image_dict[search_key] = 0

            # South Border Search
            y_max_index = y_max
            for x_index in range(x_min,x_max):
                search_key = str(x_index)+","+str(y_max_index)
                if search_key not in new_image_dict.keys():
                    # print(search_key, "is a 0 spot")
                    new_image_dict[search_key] = 0

            # Check Corners for potential 0's
            #NW Corner
            if str(x_min-1)+","+str(y_min-1) not in new_image_dict.keys():
                new_image_dict[str(x_min-1)+","+str(y_min-1)] = 0

            #NE Corner
            if str(x_max)+","+str(y_min-1) not in new_image_dict.keys():
                new_image_dict[str(x_max)+","+str(y_min-1)] = 0

            #SW Corner
            if str(x_min-1)+","+str(y_max) not in new_image_dict.keys():
                new_image_dict[str(x_min-1)+","+str(y_max)] = 0

            #SE Corner
            if str(x_max)+","+str(y_max) not in new_image_dict.keys():
                new_image_dict[str(x_max)+","+str(y_max)] = 0

            # Search within image for potential zero grids
            # This basically happens if a key does not exist
            for y_index in range(y_min,y_max):
                for x_index in range(x_min,x_max):
                    search_key = str(x_index)+","+str(y_index)
                    if search_key not in new_image_dict.keys():
                        # print(search_key, "is a 0 spot")
                        new_image_dict[search_key] = 0

        if steps%2 == 1:
            # print("Odd steps require a border of 1's to influence the inside of the image area")

            # Project lit pixels from infinite region into the image region
            # North Border of 1's
            y_min_index = y_min - 1
            for x_index in range(x_min,x_max):
                pixel_light_search(new_image_dict, x_index, y_min_index, key_C_flag=True,
                                   key_W_flag=True, key_E_flag=True, key_SW_flag=True,
                                   key_S_flag=True, key_SE_flag=True)

            # West Border of 1's
            x_min_index = x_min - 1
            for y_index in range(y_min,y_max):
                pixel_light_search(new_image_dict, x_min_index, y_index, key_N_flag=True,
                                key_NE_flag=True, key_C_flag=True, key_E_flag=True,
                                key_S_flag=True, key_SE_flag=True)

            # East Border of 1's
            x_max_index = x_max
            for y_index in range(y_min, y_max):
                pixel_light_search(new_image_dict, x_max_index, y_index, key_NW_flag=True,
                                key_N_flag=True, key_W_flag=True, key_C_flag=True,
                                key_SW_flag=True, key_S_flag=True)

            # South Border of 1's
            y_max_index = y_max
            for x_index in range(x_min, x_max):
                pixel_light_search(new_image_dict, x_index, y_max_index, key_NW_flag=True,
                key_N_flag=True, key_NE_flag=True, key_W_flag=True, key_C_flag=True, key_E_flag=True)

            # Project border corners into image
            # NW Corner
            x_index = x_min-1
            y_index = y_min-1

            pixel_light_search(new_image_dict, x_index, y_index,
                               key_C_flag=True, key_E_flag=True, key_SE_flag=True, key_S_flag=True)
            
            #NE Corner
            x_index = x_max
            y_index = y_min-1
            
            pixel_light_search(new_image_dict, x_index, y_index,
                               key_W_flag=True, key_SW_flag=True, key_C_flag=True, key_S_flag=True)

            # SW Corner
            x_index = x_min-1
            y_index = y_max

            pixel_light_search(new_image_dict, x_index, y_index,
                               key_E_flag=True, key_NE_flag=True, key_N_flag=True, key_C_flag=True)

            # SE Corner
            x_index = x_max
            y_index = y_max

            pixel_light_search(new_image_dict, x_index, y_index,
                               key_W_flag=True, key_NW_flag=True, key_N_flag=True, key_C_flag=True)

            # This is to account for the next outer layer of 1's affecting the closest layer of 1's to the image
            # North Border of 1's
            y_min_index = y_min - 1
            for x_index in range(x_min,x_max):
                key = str(x_index)+","+str(y_min_index)
                # Getting contributions from NW, N, and NE pixels
                new_image_dict[key] += 256 + 128 + 64
            
            # West Border of 1's
            x_min_index = x_min - 1
            for y_index in range(y_min,y_max):
                key = str(x_min_index)+","+str(y_index)
                # Getting contributions from NW, W, and SW pixels
                new_image_dict[key] += 256 + 32 + 4

            # East Border of 1's
            x_max_index = x_max
            for y_index in range(y_min, y_max):
                key = str(x_max_index)+","+str(y_index)
                # Getting contribution from NE, E, and SE pixels
                new_image_dict[key] += 64 + 8 + 1

            # South Border of 1's
            y_max_index = y_max
            for x_index in range(x_min, x_max):
                key = str(x_index)+","+str(y_max_index)
                # Getting contribution from SW, S, and SE pixels
                new_image_dict[key] += 4 + 2 + 1

            # NW Corner
            x_index = x_min-1
            y_index = y_min-1
            key = str(x_index)+","+str(y_index)
            # Getting contribution from NW, N, NE, W and SW pixels
            new_image_dict[key] += 256 + 128 + 64 + 32 + 4

            # NE Corner
            x_index = x_max
            y_index = y_min-1
            key = str(x_index)+","+str(y_index)
            # Getting contribution from NW, N, NE, E, and SE
            new_image_dict[key] += 256 + 128 + 64 + 8 + 1

            # SW Corner
            x_index = x_min-1
            y_index = y_max
            key = str(x_index)+","+str(y_index)
            # Getting contribution from NW, W, SW, S and SE
            new_image_dict[key] += 256 + 32 + 4 + 2 + 1

            # SE Corner
            x_index = x_max
            y_index = y_max
            key = str(x_index)+","+str(y_index)
            # Getting contribution from NE, E, SE, S and SW
            new_image_dict[key] += 64 + 8 + 4 + 2 + 1

            # Search within image for potential zero grids
            # This basically happens if a key does not exist
            for y_index in range(y_min,y_max):
                for x_index in range(x_min,x_max):
                    search_key = str(x_index)+","+str(y_index)
                    if search_key not in new_image_dict.keys():
                        # print(search_key, "is a 0 spot")
                        new_image_dict[search_key] = 0

    x_min -= 1
    x_max += 1
    y_min -= 1
    y_max += 1

    image_dict = {}
    for key in new_image_dict.keys():
        if image_algorithm[new_image_dict[key]] == "#":
            image_dict[key] = 1

    print("Length of image_dict = ", len(image_dict))