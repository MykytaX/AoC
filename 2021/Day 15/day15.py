import numpy as np
import matplotlib.pyplot as py
import pandas as pd
from os import system, name 
import openpyxl

def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
f = open("input15.txt")
lines = f.readlines()
betterlines = []
for line in lines:
    betterlines.append(line.replace("\n", ""))
map = np.zeros((502,502), dtype=int)
for i in range(0,502):
    map[i][501] = 100
    map[i][0] = 100
    for j in range(0,502):
        map[0][j] = 100
        map[501][j] = 100
for i in range(1,101):
    for j in range(1,101):
        map[i][j] = int(betterlines[i-1][j-1])

print(map)
df = pd.DataFrame(map)
filepath='original.xlsx'
df.to_excel(filepath, index=False)

for i in range(1,101):
    for j in range(1,101):
        for k in range(0,5):
            for l in range(0,5):
                if k == 0 and l == 0:
                    continue
                elif k == 0:
                    if map[i+k*100][j+(l-1)*100] == 9:
                        map[i+k*100][j+l*100] = 1
                    else:
                        map[i+k*100][j+l*100] = map[i+k*100][j+(l-1)*100] + 1
                elif l == 0:
                    if map[i+(k-1)*100][j+l*100] == 9:
                        map[i+k*100][j+l*100] = 1
                    else:
                        map[i+k*100][j+l*100] = map[i+(k-1)*100][j+l*100] + 1
                else:
                    map[i+k*100][j+l*100] = map[i][j]+((k+l))
                    if map[i+k*100][j+l*100] > 9:
                        map[i+k*100][j+l*100] -= 9

print(map)
df = pd.DataFrame(map)
filepath='my.xlsx'
df.to_excel(filepath, index=False)



def definedirections(currentpos):
    directions = (((currentpos[0]-1),(currentpos[1])),(currentpos[0],(currentpos[1]+1)),((currentpos[0]+1), currentpos[1]), ((currentpos[0],(currentpos[1]-1))))
    return directions






visited = set()
unvisited = set()
for i in range(1,501):
    for j in range(1,501):
        unvisited.add((i,j))
bignumber = 10000000000000
resultsdistance = dict.fromkeys(unvisited, bignumber)
resultslastvisited = dict.fromkeys(unvisited, (0,0))
resultsastar = dict.fromkeys(unvisited, bignumber)
queue = set()

while len(unvisited) > 0:
    if len(visited) == 0:
        directions = definedirections((1,1))
        for direction in directions:
            if map[direction[0]][direction[1]] != 100:
                    resultsdistance[direction] = map[direction[0]][direction[1]]
                    resultslastvisited[direction] = (1,1)
                    resultsastar[(direction[0],direction[1])] = int(((500-direction[0])**2+(500-direction[1])**2)**(0.5))
                    queue.add(direction)
        unvisited.remove((1,1))
        visited.add((1,1))
        continue
    champion = bignumber
    for location in queue:
            if resultsastar[location] < champion:
                currentlocation = location
                champion = resultsastar[location]
 #   print("Exploring ", currentlocation, " because distance is ", champion)
    directions = definedirections(currentlocation)
#    print(resultslastvisited[(1,2)])
    for direction in directions:
        if map[direction[0]][direction[1]] != 100:
            distancetostart = 0
            distancetostart = map[direction[0]][direction[1]] + resultsdistance[currentlocation]
            resultsastar[(direction[0],direction[1])] = int(((500-direction[0])**2+(500-direction[1])**2)**(0.5))
            if distancetostart < resultsdistance[direction]:
                resultslastvisited[direction] = currentlocation
                resultsdistance[direction] = distancetostart
                resultsastar[direction] = resultsastar[direction] + distancetostart
                if direction not in visited:
                    queue.add(direction)
        if direction == (500,500):
            print("found exit!")
            print("distance is ", distancetostart)
    unvisited.remove(currentlocation)

#    print("Left to explore ", len(unvisited))
#    print("Removing location ", currentlocation)
    visited.add(currentlocation)
    queue.remove(currentlocation)
#    print(len(queue), " ", len(unvisited))
traceback = (500,500)
x = []
y = []
distance = 0
while traceback != (1,1):
    distance += map[traceback[0]][traceback[1]]
    print(traceback)
    x.append(traceback[0])
    y.append(traceback[1])
    traceback = resultslastvisited[traceback]
print(distance)
py.scatter(x,y)
py.show()
            




