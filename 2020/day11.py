import numpy as np

f = open("input11.txt")
lines = f.readlines()
betterlines = []
for line in lines:
    betterlines.append(line.replace("\n", ""))
dumbogroup = np.zeros((12,12), dtype=np.int16)
for i in range(0,12):
    dumbogroup[i][11] = 100
    dumbogroup[i][0] = 100
    for j in range(0,12):
        dumbogroup[0][j] = 100
        dumbogroup[11][j] = 100

for i in range(1, 11):
    for j in range(1, 11):
        dumbogroup[i][j] = list(betterlines[i-1])[j-1]


def adjacent(tuple):
    adjacency_list = []
    adjacency_list.append(((tuple[0]+1),tuple[1]))
    adjacency_list.append(((tuple[0]),tuple[1]+1))
    adjacency_list.append(((tuple[0]-1),tuple[1]))
    adjacency_list.append(((tuple[0]),tuple[1]-1))
    adjacency_list.append(((tuple[0]+1),tuple[1]+1))
    adjacency_list.append(((tuple[0]-1),tuple[1]-1))
    adjacency_list.append(((tuple[0]+1),tuple[1]-1))
    adjacency_list.append(((tuple[0]-1),tuple[1]+1))
    return adjacency_list

def flash(flashing_set, already_flashed):
    oldflashingset = set(flashing_set)
    
    for position in oldflashingset:
        i = position[0]
        j = position[1]
        dumbogroup[i][j] = 0
        already_flashed.add((i,j))
        for affectedpoisition in adjacent((i,j)):
            k = affectedpoisition[0]
            l = affectedpoisition[1]
            if dumbogroup[k][l] < 9 and (k,l) not in already_flashed:
                dumbogroup[k][l] += 1
            elif dumbogroup[k][l] == 9 and (k,l) not in already_flashed:
                flashing_set.add((k,l))
        flashing_set.remove((i,j)) 
    if len(flashing_set) == 0:
        return already_flashed
    else: return flash(flashing_set, already_flashed)

           
answer = []

flashcount = 0
for step in range (0,300):
    already_flashed = set()
    flashing_set = set()
    for i in range(1, 11):
        for j in range(1, 11):
            if dumbogroup[i][j] < 9 and (i,j) not in already_flashed:
                dumbogroup[i][j] += 1
                
            elif dumbogroup[i][j] == 9 and (i,j) not in already_flashed:
                flashing_set.add((i,j))
                already_flashed = flash(flashing_set, already_flashed)
    if len(already_flashed) == 100:
        answer.append(step)            

print(answer)
