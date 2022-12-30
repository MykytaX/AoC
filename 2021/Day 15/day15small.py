import numpy as np
from os import system, name 
import matplotlib.pyplot as plt

def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 



f = open("input15.txt")
lines = f.readlines()
betterlines = []
for line in lines:
    betterlines.append(line.replace("\n", ""))
map = np.zeros((102,102), dtype=int)
for i in range(0,102):
    map[i][101] = 100
    map[i][0] = 100
    for j in range(0,102):
        map[0][j] = 100
        map[101][j] = 100
for i in range(1,101):
    for j in range(1,101):
        map[i][j] = int(betterlines[i-1][j-1])

f = open("input15small.txt")
lines = f.readlines()
betterlines = []
for line in lines:
    betterlines.append(line.replace("\n", ""))
smallmap = np.zeros((12,12), dtype=int)
for i in range(0,12):
    smallmap[i][11] = 100
    smallmap[i][0] = 100
    for j in range(0,12):
        smallmap[0][j] = 100
        smallmap[11][j] = 100
for i in range(1,11):
    for j in range(1,11):
        smallmap[i][j] = int(betterlines[i-1][j-1])


#map = smallmap

curchampion = 0
currentpath = []
currentpos = [1,1]
directions = ()
def definedirections(currentpos):
    directions = (((currentpos[0]-1),(currentpos[1])),(currentpos[0],(currentpos[1]-1)),((currentpos[0]+1), currentpos[1]), ((currentpos[0],(currentpos[1]+1))))
    return directions
todo = [((1,1),[(1,1)],1)]
check = 0
currentscore = 0
currentlocation = ()
while len(todo)>0:
    clear()
    currentlocation = todo[-1]
    currentpath = currentlocation[1]
    print("Exploring position...", currentlocation[0], end="\r")
#    print("Current champ is: ", curchampion)
    todo.pop()
    directions = definedirections((currentlocation[0][0], currentlocation[0][1]))
    currentscore = currentlocation[2]
#    print(currentscore)
    for direction in directions:
        if direction == (100,100):
            print("REACHED EXIT!")
            score = 0
            score = currentscore
            if curchampion == 0 or score < curchampion:
                curchampion = score
                print("New champion ", curchampion)
        elif map[direction[0]][direction[1]] < 10 and direction not in currentpath:
            if currentscore+map[direction[0]][direction[1]] < curchampion or curchampion == 0:
                currentpath.append(direction)
                currentscore += map[direction[0]][direction[1]]
                todo.append(((direction), currentpath.copy(), currentscore))
                currentpath.pop()
                currentscore -= map[direction[0]][direction[1]]
    






