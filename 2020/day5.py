import os
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
print(CURR_DIR)

f1 = open(CURR_DIR+"/input.day5")

BSP_data = f1.readlines()

total_rows = 128
total_cols = 8
max_ID = 0

ID_list = []

# *** Part 1 ***

for BSP_line in BSP_data:
    BSP_line = BSP_line.replace("\n","")
    row_low_range  = 0
    row_high_range = total_rows
    col_low_range = 0
    col_high_range = total_cols
    for i in range(10):
        if BSP_line[i] == 'B':
            if i != 6:
                row_low_range = int((row_high_range-row_low_range) / 2) + row_low_range
            else:
                final_row = row_high_range-1
        elif BSP_line[i] == 'F':
            if i != 6:
                row_high_range = row_high_range - int((row_high_range-row_low_range) / 2)
            else:
                final_row = row_low_range
        elif BSP_line[i] == 'L':
            if i != 9:
                col_high_range = col_high_range - int((col_high_range -  col_low_range)/2)
            else:
                final_col = col_low_range
        elif BSP_line[i] == 'R':
            if i != 9:
                col_low_range = int((col_high_range - col_low_range) / 2) + col_low_range
            else:
                final_col = col_high_range-1

    unique_id = final_row*8 + final_col
    ID_list.append(unique_id)
    if max_ID < unique_id:
        max_ID = unique_id

print("Highest Seat ID =", max_ID)

# *** Part 2 ***
ID_list.sort()
for i in range(len(ID_list)-1):
    if ID_list[i+1]-ID_list[i] != 1:
        print("Missing ID =", ID_list[i]+1)
        break