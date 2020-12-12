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
print("Part 1: There are", occupied_seats, "occupied seats!")

# *** Part 2 ***

def search_occ_NE(startRow, startCol, layout):
    maxRow = len(layout)
    maxCol = len(layout[0])

    currRow = startRow + 1
    currCol = startCol + 1

    count = 0
    while currRow < maxRow and currCol < maxCol:
        if layout[currRow][currCol] == '#':
            return True
        elif layout[currRow][currCol] == 'L':
            return False
        else:
            currRow = currRow + 1
            currCol = currCol + 1
    
    return False

def search_occ_NW(startRow, startCol, layout):
    maxRow = len(layout)

    currRow = startRow + 1
    currCol = startCol - 1

    count = 0
    while currRow < maxRow and currCol > 0:
        if layout[currRow][currCol] == '#':
            return True
        elif layout[currRow][currCol] == 'L':
            return False
        else:
            currRow = currRow + 1
            currCol = currCol - 1
    
    return False

def search_occ_SE(startRow, startCol, layout):
    maxCol = len(layout[0])

    currRow = startRow - 1
    currCol = startCol + 1

    count = 0
    while currRow > 0 and currCol < maxCol:
        if layout[currRow][currCol] == '#':
            return True
        elif layout[currRow][currCol] == 'L':
            return False
        else:
            currRow = currRow - 1
            currCol = currCol + 1
    
    return False

def search_occ_SW(startRow, startCol, layout):
    currRow = startRow - 1
    currCol = startCol - 1

    count = 0
    while currRow > 0 and currCol > 0:
        if layout[currRow][currCol] == '#':
            return True
        elif layout[currRow][currCol] == 'L':
            return False
        else:
            currRow = currRow - 1
            currCol = currCol - 1
    
    return False

def search_occ_W(startRow, startCol, layout):
    currCol = startCol - 1
    while currCol > 0:
        if layout[startRow][currCol] == '#':
            return True
        elif layout[startRow][currCol] == 'L':
            return False
        else:
            currCol = currCol - 1
    return False

def search_occ_E(startRow, startCol, layout):
    maxCol = len(layout[1])
    currCol = startCol + 1
    while currCol < maxCol:
        if layout[startRow][currCol] == '#':
            return True
        elif layout[startRow][currCol] == 'L':
            return False
        else:
            currCol = currCol + 1
    return False

def search_occ_N(startRow, startCol, layout):
    maxRow = len(layout)
    currRow = startRow + 1
    while currRow < maxRow:
        if layout[currRow][startCol] == '#':
            return True
        elif layout[currRow][startCol] == 'L':
            return False
        else:
            currRow = currRow + 1
    return False

def search_occ_S(startRow, startCol, layout):
    currRow = startRow - 1
    while currRow > 0:
        if layout[currRow][startCol] == '#':
            return True
        elif layout[currRow][startCol] == 'L':
            return False
        else:
            currRow = currRow - 1
    return False

seat_layout = [empty_row]

for row in seat_layout_data:
    row = row.replace("\n","")
    row = '.' + row + '.'
    seat_layout.append(row)

seat_layout.append(empty_row)
rows = len(seat_layout)
cols = len(seat_layout[0])
match = False

while(not match):
    new_seat_layout = [empty_row]
    for row in range(1,rows-1):
        new_row = "."
        for col in range(1,cols-1):
            if seat_layout[row][col] == 'L':
                check_SW = search_occ_SW(row,col,seat_layout)
                check_S  = search_occ_S(row,col,seat_layout)
                check_SE = search_occ_SE(row,col,seat_layout)
                check_W  = search_occ_W(row,col,seat_layout)
                check_E  = search_occ_E(row,col,seat_layout)
                check_NW = search_occ_NW(row,col,seat_layout)
                check_N  = search_occ_N(row,col,seat_layout)
                check_NE = search_occ_NE(row,col,seat_layout)

                if not check_SW and not check_S and not check_SE and not check_W and not check_E and not check_NW and not check_N and not check_NE:
                    new_row = new_row + '#'
                else:
                    new_row = new_row + 'L'
            
            elif seat_layout[row][col] == '#':
                check_SW = search_occ_SW(row,col,seat_layout)
                check_S  = search_occ_S(row,col,seat_layout)
                check_SE = search_occ_SE(row,col,seat_layout)
                check_W  = search_occ_W(row,col,seat_layout)
                check_E  = search_occ_E(row,col,seat_layout)
                check_NW = search_occ_NW(row,col,seat_layout)
                check_N  = search_occ_N(row,col,seat_layout)
                check_NE = search_occ_NE(row,col,seat_layout)
                if (check_SW + check_S + check_SE + check_W + check_E + check_NW + check_N + check_NE >= 5):
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

occupied_seats = sum(row.count('#') for row in new_seat_layout)
print("Part 2: There are", occupied_seats, "occupied seats!")