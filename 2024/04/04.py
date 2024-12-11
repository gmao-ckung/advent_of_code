import os

# Read input file from current directory
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
file = open(CURR_DIR+"/in.04","r")

puzzle = file.read().splitlines()

nrow = len(puzzle)
ncol = len(puzzle[0])

letter_coord = {'X': [], 'M': [], 'A': [], 'S': [] }


for row in range(nrow):
    for col in range(ncol):
        match puzzle[row][col]:
            case 'X': 
                letter_coord['X'].append([row,col])
            case 'M':
                letter_coord['M'].append([row,col])
            case 'A':
                letter_coord['A'].append([row,col])
            case 'S':
                letter_coord['S'].append([row,col])

num_XMAS = 0

for row in range(nrow):
    for col in range(ncol):
        if [row, col] in letter_coord['X']:
            # Right
            if [row, col+1] in letter_coord['M'] and \
               [row,col+2] in letter_coord['A'] and \
               [row,col+3] in letter_coord['S']:
                num_XMAS += 1
            # Left
            if [row,col-1] in letter_coord['M'] and \
               [row,col-2] in letter_coord['A'] and \
               [row,col-3] in letter_coord['S']:
                num_XMAS += 1
            # Down
            if [row+1,col] in letter_coord['M'] and \
               [row+2,col] in letter_coord['A'] and \
               [row+3,col] in letter_coord['S']:
                num_XMAS += 1
            # Up
            if [row-1,col] in letter_coord['M'] and \
               [row-2,col] in letter_coord['A'] and \
               [row-3,col] in letter_coord['S']:
                num_XMAS += 1
            # Diagonal going NW
            if [row-1,col-1] in letter_coord['M'] and \
               [row-2,col-2] in letter_coord['A'] and \
               [row-3,col-3] in letter_coord['S']:
                num_XMAS += 1
            # Diagonal going NE
            if [row-1,col+1] in letter_coord['M'] and \
               [row-2,col+2] in letter_coord['A'] and \
               [row-3,col+3] in letter_coord['S']:
                num_XMAS += 1
            # Diagonal going SW
            if [row+1,col-1] in letter_coord['M'] and \
               [row+2,col-2] in letter_coord['A'] and \
               [row+3,col-3] in letter_coord['S']:
                num_XMAS += 1
            # Diagonal going SE
            if [row+1,col+1] in letter_coord['M'] and \
               [row+2,col+2] in letter_coord['A'] and \
               [row+3,col+3] in letter_coord['S']:
                num_XMAS += 1

print("Part 1: Number of XMAS = ", num_XMAS)

num_XMAS = 0

for row in range(nrow):
    for col in range(ncol):
        if [row, col] in letter_coord['A']:
            # V1
            if [row-1, col-1] in letter_coord['M'] and \
               [row+1, col-1] in letter_coord['M'] and \
               [row-1, col+1] in letter_coord['S'] and \
               [row+1, col+1] in letter_coord['S']:
                num_XMAS += 1
            # # V2
            # # S M
            # #  A 
            # # M S
            # if [row-1, col-1] in letter_coord['S'] and \
            #    [row+1, col-1] in letter_coord['M'] and \
            #    [row-1, col+1] in letter_coord['M'] and \
            #    [row+1, col+1] in letter_coord['S']:
            #     num_XMAS += 1
            # V3
            # S M
            #  A 
            # S M
            if [row-1, col-1] in letter_coord['S'] and \
               [row+1, col-1] in letter_coord['S'] and \
               [row-1, col+1] in letter_coord['M'] and \
               [row+1, col+1] in letter_coord['M']:
                num_XMAS += 1
            # # V4
            # # M S
            # #  A 
            # # S M
            # if [row-1, col-1] in letter_coord['M'] and \
            #    [row+1, col-1] in letter_coord['S'] and \
            #    [row-1, col+1] in letter_coord['S'] and \
            #    [row+1, col+1] in letter_coord['M']:
            #     num_XMAS += 1
            # V5
            # S S
            #  A 
            # M M
            if [row-1, col-1] in letter_coord['S'] and \
               [row+1, col-1] in letter_coord['M'] and \
               [row-1, col+1] in letter_coord['S'] and \
               [row+1, col+1] in letter_coord['M']:
                num_XMAS += 1
            # V6
            # M M
            #  A 
            # S S
            if [row-1, col-1] in letter_coord['M'] and \
               [row+1, col-1] in letter_coord['S'] and \
               [row-1, col+1] in letter_coord['M'] and \
               [row+1, col+1] in letter_coord['S']:
                num_XMAS += 1

print("Part 2: Number of X-MAS = ", num_XMAS)

# def find_match(letter_coord, letter, row, col):
#     found_coord = []
#     row_coord = [row-1, row, row+1]
#     col_coord = [col-1, col, col+1]
#     for _row in row_coord:
#         for _col in col_coord:
#             if [_row, _col] in letter_coord[letter]:
#                 found_coord.append([_row, _col])
    
#     return found_coord

# Searches for all possible combinations where XMAS is connected
# for row in range(nrow):
#     for col in range(ncol):
#         if [row, col] in letter_coord['X']:
#             m_coord = find_match(letter_coord, 'M', row, col)
#             for curr_m_coord in m_coord:
#                 a_coord = find_match(letter_coord,'A', curr_m_coord[0], curr_m_coord[1])
#                 for curr_a_coord in a_coord:
#                     s_coord = find_match(letter_coord,'S', curr_a_coord[0], curr_a_coord[1])
#                     print('current X :', row, col)
#                     print('current M :' , curr_m_coord[0], curr_m_coord[1])
#                     print('current A :', curr_a_coord[0], curr_a_coord[1])
#                     print('Possible S:', s_coord)
#                     num_XMAS += len(s_coord)