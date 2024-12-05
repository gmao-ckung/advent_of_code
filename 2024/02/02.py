import os
import numpy as np

# Read input file from current directory
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
file = open(CURR_DIR+"/in.02","r")

# Read lines within input file and remove new line character at the line's end
reports = file.read().splitlines()

num_safe = 0
for report in reports:
    report = [int(x) for x in report.split()]
    diff = np.diff(report)
    if(all(num >= 0 for num in diff)) or (all(num <= 0 for num in diff)):
        if(all((num >= 1 and num <= 3) for num in abs(diff))):
            num_safe += 1

print("Part 1 : Number of safe reports = ", num_safe)

num_safe = 0
for report in reports:
    report = [int(x) for x in report.split()]
    diff = np.diff(report)
    print(diff)
    if(all(num >= 0 for num in diff)) or (all(num <= 0 for num in diff)):
        if(all((num >= 1 and num <= 3) for num in abs(diff))):
            num_safe += 1
        else:
            # print("Examining report : ", report)
            for index in range(len(report)):
                # print(index)
                temp_report = report.copy()
                # print(temp_report)
                del temp_report[index]
                # print(temp_report)
                diff = np.diff(temp_report)
                if(all(num >= 0 for num in diff)) or (all(num <= 0 for num in diff)):
                    if(all((num >= 1 and num <= 3) for num in abs(diff))):
                        num_safe += 1
                        break
    else:
        # print("Examining report : ", report)
        for index in range(len(report)):
            # print(index)
            temp_report = report.copy()
            # print(temp_report)
            del temp_report[index]
            # print(temp_report)
            diff = np.diff(temp_report)
            if(all(num >= 0 for num in diff)) or (all(num <= 0 for num in diff)):
                if(all((num >= 1 and num <= 3) for num in abs(diff))):
                    num_safe += 1
                    break
print("Part 2 : Number of safe reports = ", num_safe)