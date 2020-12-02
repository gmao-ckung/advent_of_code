import numpy as np

f1 = open("/home/ckung/Code/advent_of_code/2015/input.day2")

dims = f1.readlines()

l = []
w = []
h = []

for dim in dims:
    dim = dim.replace("\n", "")
    dimSplit = dim.split("x")
    l.append(dimSplit[0])
    w.append(dimSplit[1])
    h.append(dimSplit[2])

totalSA = 0

# *** Part 1 ***

for i in range(len(l)):
    surfA = [int(l[i]) * int(w[i]),  int(w[i]) * int(h[i]), int(h[i]) * int(l[i])]
    totalSA = totalSA + 2*surfA[0] + 2*surfA[1] + 2*surfA[2] + min(surfA)

print("Total sq ft of wrapping paper needed =", totalSA)

# *** Part 2 ***

totalLenRibbon = 0

lens = np.zeros(3)
for i in range(len(l)):
    lens[0] = int(l[i])
    lens[1] = int(w[i])
    lens[2] = int(h[i])
    lens_S = np.sort(lens)

    totalLenRibbon = totalLenRibbon + (lens_S[0]*2 + lens_S[1]*2) + (lens[0]*lens[1]*lens[2])

print("Total Length of Ribbon needed =", totalLenRibbon)