import numpy as np
import matplotlib.pyplot as py
import sys 

f = open("input13.txt")
lines = f.readlines()
coordinates = lines[:793]
coordbetter = []
for i in range(0, len(coordinates)):
    k, n = coordinates[i].replace("\n", "").split(sep=",")
    coordbetter.append((int(k),int(n)))
foldinginstructions = []
verboseinstructions = lines[794:]
for i in range(0, len(verboseinstructions)):
    cut = verboseinstructions[i][11:]
    foldaxis, foldcood = verboseinstructions[i][11:].replace("\n", "").split("=")
    foldinginstructions.append((foldaxis, int(foldcood)))
print(foldinginstructions)
### Determining the size of the array
maxX = 0
maxY = 0
for i in range(0, len(coordbetter)):
    if coordbetter[i][0] > maxX:
        maxX = coordbetter[i][0]
    if  coordbetter[i][1] > maxY:
        maxY = coordbetter[i][1]

np.set_printoptions(threshold=sys.maxsize)


mapspace = np.zeros((maxX+1, maxY+1), dtype=int)
### Mapping initial conditions

for coord in coordbetter:
    mapspace[coord[0]][coord[1]] = 1
  

count = 0



foldedmapspace = mapspace
newfoldedmapspace = foldedmapspace.copy()

for instruction in foldinginstructions:
    count = 0
    if instruction[0] == "x":
        foldline = instruction[1]
        foldedmapspace = newfoldedmapspace.copy()
        maxX, maxY = foldedmapspace.shape
        print(maxX, maxY)
        newfoldedmapspace = foldedmapspace[:foldline].copy()
        for i in range(foldline, maxX):
           for j in range(0, maxY):
                   if foldedmapspace[i][j] == 1:
                       newfoldedmapspace[2*foldline-i][j] = 1
    if instruction[0] == "y":
        foldline = instruction[1]
        foldedmapspace = newfoldedmapspace.copy()
        maxX, maxY = foldedmapspace.shape
        print(maxX, maxY)
        newfoldedmapspace = foldedmapspace[:, :foldline].copy()
        for i in range(0, maxX):
           for j in range(foldline, maxY):
               if foldedmapspace[i][j] == 1:
                   newfoldedmapspace[i][2*foldline-j] = 1
    print("We've got new array with dimensions X", len(newfoldedmapspace))
    print("We've got new array with dimensions Y", len(newfoldedmapspace[0]))
    for k in range(0, len(newfoldedmapspace)):
        for l in range(0, len(newfoldedmapspace[0])):
            if newfoldedmapspace[k][l] == 1:
                print("Got one at ", k , " ", l)
                py.plot(k,l, "or")
                count += 1
    print("And the count is ", count)
    py.show()


print(foldedmapspace.T)
