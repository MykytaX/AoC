import numpy as np
import matplotlib.pyplot as ply
import sys



f = open("input5.txt")
lines = f.readlines()
betterlines = []
newpoint = []
bestlines = []
newline = []
for line in lines:
    betterlines.append(line.replace("\n", ""))
finishedlist = []
for line in betterlines:
    points = line.split(" -> ")
    for point in points:
        coordinates = point.split(",")
        newline.append(coordinates)
    bestlines.append(newline)
    newline = []

oceanspace = np.zeros((1000,1000), dtype = np.int32)

linesarray = np.array(bestlines)
linesarray = linesarray.astype(np.int32)

for i in range (0, 500):
    x1 = linesarray[i][0][0]
    x2 = linesarray[i][1][0]
    y1 = linesarray[i][0][1]
    y2 = linesarray[i][1][1]
    if linesarray[i][0][0] == linesarray[i][1][0]:        
        dif = abs(y1 - y2)
        if (y1 - y2) >= 0:
            for k in range(0, dif+1):
                oceanspace[x1][y2+k] += 1
        else: 
            for k in range(0, dif+1):
                oceanspace[x1][y1+k] += 1
    if linesarray[i][0][1] == linesarray[i][1][1]:
        dif = abs(x1 - x2)
        if (x1 - x2) >= 0:
            for j in range(0, dif+1):
                oceanspace[x2+j][y1] += 1
        else: 
            for j in range(0, dif+1):
                oceanspace[x1+j][y1] += 1
    if y2 > y1 and x2 > x1:
        dif = y2 - y1
        for k in range(0, dif+1):
            oceanspace[x1+k][y1+k] += 1
    if y2 > y1 and x2 < x1:
        dif = y2 - y1
        for k in range(0, dif+1):
            oceanspace[x1-k][y1+k] += 1
    if y2 < y1 and x2 > x1:
        dif = y1 - y2
        for k in range(0, dif+1):
            oceanspace[x1+k][y1-k] += 1
    if y2 < y1 and x2 < x1:
        dif = y1 - y2
        for k in range(0, dif+1):
            oceanspace[x1-k][y1-k] += 1


count = 0
for i in range(0,1000):
    for k in range(0,1000):
        if oceanspace[i][k] > 1:
            count += 1
print(count)

