import os
# Read input file from current directory
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
file = open(CURR_DIR+"/in.01","r")

# Read lines within input file and remove new line character at the line's end
lines = file.read().splitlines()

left = []
right = []

for line in lines:
    two_numbers = line.split('   ')
    left.append(int(two_numbers[0]))
    right.append(int(two_numbers[1]))

left_s  = sorted(left)
right_s = sorted(right)

sum = 0

for i in range(len(left_s)):
    sum += abs(left_s[i] - right_s[i])

print('Part 1 : Sum = ', sum)

sum = 0

for num in left:
    count = right.count(num)
    sum += count * num

print('Part 2 : Sum = ', sum)