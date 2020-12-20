import os
import numpy as np
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
print(CURR_DIR)
f1 = open(CURR_DIR+"/input.day17")
initial_cube = f1.readlines()

#print(initial_cube)
x_len_init = len(initial_cube[0].replace("\n",""))
y_len_init = len(initial_cube)
z_len_init = 1

total_cycles = 6

# *** Part 1 ***

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

curr_cell_domain = np.zeros((total_x_len,total_y_len,total_z_len),dtype=int)
future_cell_domain = np.zeros((total_x_len,total_y_len,total_z_len),dtype=int)

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
        if cell == '#':
            curr_cell_domain[start_x_index+x_inc,start_y_index+y_inc,start_z_index] = 1
        x_inc += 1
    y_inc += 1

def cell_update(x_index, y_index, z_index, curr_cell_domain, future_cell_domain):
    active = False
    if curr_cell_domain[x_index,y_index,z_index] == 1:
        active = True
    
    neighbors_active = np.sum(curr_cell_domain[x_index-1:x_index+2,y_index-1:y_index+2,z_index-1:z_index+2]) \
                     - curr_cell_domain[x_index,y_index,z_index]
    if active:
        if (neighbors_active == 2) or (neighbors_active == 3):
            future_cell_domain[x_index,y_index,z_index] = 1
        else:
            future_cell_domain[x_index,y_index,z_index] = 0
    else:
        if neighbors_active == 3:
            future_cell_domain[x_index,y_index,z_index] = 1
        else:
            future_cell_domain[x_index,y_index,z_index] = 0

for cycle in range(total_cycles):
    for i in range(1,total_x_len-1):
        for j in range(1,total_y_len-1):
            for k in range(1, total_z_len-1):
                cell_update(i,j,k,curr_cell_domain, future_cell_domain)

    curr_cell_domain = np.copy(future_cell_domain)

num_active_cells = np.sum(np.sum(curr_cell_domain))
print("Part 1: Number of Active Cells =", num_active_cells)

# *** Part 2 ***

w_len_init = 1
total_w_len = w_len_init + (total_cycles + 1) * 2

print("x-length =", total_x_len)
print("y-length =", total_y_len)
print("z-length =", total_z_len)
print("w-length =", total_w_len)

curr_cell_domain   = np.zeros((total_x_len,total_y_len,total_z_len,total_w_len),dtype=int)
future_cell_domain = np.zeros((total_x_len,total_y_len,total_z_len,total_w_len),dtype=int)

start_w_index = int((total_w_len - w_len_init) / 2)

print("start_x_index =", start_x_index)
print("start_y_index =", start_y_index)
print("start_z_index =", start_z_index)
print("start_w_index =", start_w_index)

y_inc = 0
for line in initial_cube:
    line = line.replace("\n","")
    x_inc = 0
    for cell in line:
        if cell == '#':
            curr_cell_domain[start_x_index+x_inc,start_y_index+y_inc,start_z_index, start_w_index] = 1
        x_inc += 1
    y_inc += 1

def cell_update_hyper(x_index, y_index, z_index, w_index, curr_cell_domain, future_cell_domain):
    active = False
    if curr_cell_domain[x_index,y_index,z_index,w_index] == 1:
        active = True
    
    neighbors_active = np.sum(curr_cell_domain[x_index-1:x_index+2,
                                               y_index-1:y_index+2,
                                               z_index-1:z_index+2,
                                               w_index-1:w_index+2]) \
                     - curr_cell_domain[x_index,y_index,z_index,w_index]
    if active:
        if (neighbors_active == 2) or (neighbors_active == 3):
            future_cell_domain[x_index,y_index,z_index,w_index] = 1
        else:
            future_cell_domain[x_index,y_index,z_index,w_index] = 0
    else:
        if neighbors_active == 3:
            future_cell_domain[x_index,y_index,z_index,w_index] = 1
        else:
            future_cell_domain[x_index,y_index,z_index,w_index] = 0

for cycle in range(total_cycles):
    for i in range(1,total_x_len-1):
        for j in range(1,total_y_len-1):
            for k in range(1, total_z_len-1):
                for w in range(1,total_w_len-1):
                    cell_update_hyper(i,j,k,w,curr_cell_domain, future_cell_domain)

    curr_cell_domain = np.copy(future_cell_domain)

num_active_cells = np.sum(np.sum(np.sum(curr_cell_domain)))
print("Part 2: Number of Active Cells =", num_active_cells)