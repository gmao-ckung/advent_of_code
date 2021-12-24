import os

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
fopen = open(CURR_DIR+"/input.test","r")

scanner_data = fopen.readlines()

scanner_coord = {}

# def rot_90_x
# def rot_90_y
# def rot_90_z
# def flip_x
# def flip_y
# def flip_z

for data in scanner_data:
    print(data)
    if data[0:2] == "--":
        scanner_number = data.replace("\n","").split(" ")[2]
        scanner_coord[scanner_number + "_0"] = []
        scanner_coord[scanner_number + "_1"] = []
        scanner_coord[scanner_number + "_2"] = []
    elif data != "\n":
        coords = data.replace("\n","").split(",")
        scanner_coord[scanner_number + "_0"].append(int(coords[0]))
        scanner_coord[scanner_number + "_1"].append(int(coords[1]))
        scanner_coord[scanner_number + "_2"].append(int(coords[2]))

# Start with Scanner 0 and 1 at "default" orientation
# Diff the 0, 1, and 2 coordinates respectively
# Check to see if there are any common differences

scanner_number_0 = "0"
scanner_number_1 = "1"

differences_0 = {}
differences_1 = {}
differences_2 = {}

# There are 24 different orientations, which I will list out
# Rotate around x     Rotate around y     Rotate around z
# +x, +y, +z          +y, +z, +x          +z, +x, +y
# +x, +z, -y          +y, +x, -z          +z, +y, -x
# +x, -y, -z          +y, -z, -x          +z, -x, -y
# +x, -z, +y          +y, -x, +z          +z, -y, +x

# Reflect on x        Reflect on y       Reflect on z
# -x, -y, +z          -y, -z, +x         -z, -x, -y
# -x, +z, +y          -y, +x, +z         -z, +y, +x
# -x, +y, -z          -y, +z, -x         -z, +x, -y
# -x, -z, -y          -y, -x, -z         -z, -y, -x

orientation = []
orient_coefficients = [[1, 1, 1], [1, 1, -1], [1, -1, -1], [1, -1, 1],
                      [-1,-1, 1], [-1, 1, 1], [-1, 1, -1], [-1,-1,-1]]

search_range = len(scanner_coord[scanner_number_0+"_0"])

for j in range(search_range):
    for i in range(search_range):
        diff_0_key = scanner_coord[scanner_number_0+"_0"][j] - scanner_coord[scanner_number_1+"_0"][i]
        diff_1_key = scanner_coord[scanner_number_0+"_1"][j] - scanner_coord[scanner_number_1+"_1"][i]
        diff_2_key = scanner_coord[scanner_number_0+"_2"][j] - scanner_coord[scanner_number_1+"_2"][i]

        if diff_0_key not in differences_0.keys():
            differences_0[diff_0_key] = [1, scanner_number_0+"_"+str(j)+"__"+scanner_number_1+"_"+str(i)]
        else:
            differences_0[diff_0_key][0] += 1
            differences_0[diff_0_key].append(scanner_number_0+"_"+str(j)+"__"+scanner_number_1+"_"+str(i))

        if diff_1_key not in differences_0.keys():
            differences_0[diff_1_key] = [1, scanner_number_0+"_"+str(j)+"__"+scanner_number_1+"_"+str(i)]
        else:
            differences_0[diff_1_key][0] += 1
            differences_0[diff_1_key].append(scanner_number_0+"_"+str(j)+"__"+scanner_number_1+"_"+str(i))

        if diff_2_key not in differences_0.keys():
            differences_0[diff_2_key] = [1, scanner_number_0+"_"+str(j)+"__"+scanner_number_1+"_"+str(i)]
        else:
            differences_0[diff_2_key][0] += 1
            differences_0[diff_2_key].append(scanner_number_0+"_"+str(j)+"__"+scanner_number_1+"_"+str(i))

print()