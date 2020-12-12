import numpy as np
import os
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
print(CURR_DIR)
f1 = open(CURR_DIR+"/input.day11")
seat_layout_data = f1.readlines()

empty_row = (int(len(seat_layout_data[0]))+1) * '.'
seat_layout = [empty_row]

for row in seat_layout_data:
    row = row.replace("\n","")
    row = '.' + row + '.'
    seat_layout.append(row)

seat_layout.append(empty_row)
rows = len(seat_layout)
cols = len(seat_layout[0])
match = False

# *** Part 1 ***

while(not match):
    new_seat_layout = [empty_row]
    for row in range(1,rows-1):
        new_row = "."
        for col in range(1,cols-1):
            if seat_layout[row][col] == 'L':
                check_SW = (seat_layout[row-1][col-1] == 'L') or (seat_layout[row-1][col-1] == '.')
                check_S  = (seat_layout[row-1][col]   == 'L') or (seat_layout[row-1][col]   == '.')
                check_SE = (seat_layout[row-1][col+1] == 'L') or (seat_layout[row-1][col+1] == '.')
                check_W  = (seat_layout[row][col-1] == 'L')   or (seat_layout[row][col-1] == '.')
                check_E  = (seat_layout[row][col+1] == 'L')   or (seat_layout[row][col+1] == '.')
                check_NW = (seat_layout[row+1][col-1] == 'L') or (seat_layout[row+1][col-1] == '.')
                check_N  = (seat_layout[row+1][col] == 'L')   or (seat_layout[row+1][col] == '.')
                check_NE = (seat_layout[row+1][col+1] == 'L') or (seat_layout[row+1][col+1] == '.')

                if check_SW and check_S and check_SE and check_W and check_E and check_NW and check_N and check_NE:
                    new_row = new_row + '#'
                else:
                    new_row = new_row + 'L'
            
            elif seat_layout[row][col] == '#':
                check_SW = (seat_layout[row-1][col-1] == '#')
                check_S  = (seat_layout[row-1][col]   == '#')
                check_SE = (seat_layout[row-1][col+1] == '#')
                check_W  = (seat_layout[row][col-1] == '#')
                check_E  = (seat_layout[row][col+1] == '#')
                check_NW = (seat_layout[row+1][col-1] == '#')
                check_N  = (seat_layout[row+1][col] == '#')
                check_NE = (seat_layout[row+1][col+1] == '#')
                if (check_SW + check_S + check_SE + check_W + check_E + check_NW + check_N + check_NE >= 4):
                    new_row = new_row + 'L'
                else:
                    new_row = new_row + '#'

            else:
                new_row = new_row + '.'
        
        new_row = new_row + '.'
        new_seat_layout.append(new_row)

    new_seat_layout.append(empty_row)

    if new_seat_layout == seat_layout:
        match = True
    else:
        seat_layout = new_seat_layout
#print(new_seat_layout)

occupied_seats = sum(row.count('#') for row in new_seat_layout)
print("There are", occupied_seats, "occupied seats!")