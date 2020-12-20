import os
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
print(CURR_DIR)
f1 = open(CURR_DIR+"/input.test")
initial_cube = f1.readlines()

#print(initial_cube)
x_len_init = len(initial_cube[0].replace("\n",""))
y_len_init = len(initial_cube)
z_len_init = 1

total_cycles = 1

# Initialize the potentially "active" cube region
# based on the total number of cycles.  I also add
# an extra boundary region layer to make the compute easier
# to implement.  This extra layer is represented by the "+1"
# added to "total_cycles"
total_x_len = x_len_init + (total_cycles + 1) * 2
total_y_len = y_len_init + (total_cycles + 1) * 2
total_z_len = z_len_init + (total_cycles + 1) * 2

print("x-length =", total_x_len)
print("y-length =", total_y_len)
print("z-length =", total_z_len)

cell_row = ["."*total_x_len]
cell_plane = cell_row * total_y_len
cell_domain = [cell_plane] * total_z_len

start_x_index = int((total_x_len - x_len_init) / 2)
start_y_index = int((total_y_len - y_len_init) / 2)
start_z_index = int((total_z_len - z_len_init) / 2)

print("start_x_index =", start_x_index)
print("start_y_index =", start_y_index)
print("start_z_index =", start_z_index)

y_inc = 0
for line in initial_cube:
    line = line.replace("\n","")
    x_inc = 0
    for cell in line:
        cell_domain[start_z_index][start_y_index+y_inc][start_x_index + x_inc] = cell
        x_inc += 1
    y_inc += 1