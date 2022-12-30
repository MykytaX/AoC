import numpy as np

f = open("./day8/input8.txt")
map = f.readlines()
bettermap = []
for line in map:
    line = line.rstrip()
    line = list(line)
    bettermap.append(line)


newmap = []
for i in range(0, len(bettermap)):
    newmap.append([])
    for j in range(0, len(bettermap[i])):
        newmap[i].append(int(bettermap[i][j]))
        

bestmap = np.zeros([101,101], dtype=int)
for i in range(0, len(bestmap)):
    for j in range(0,len(bestmap[i])):
        if i == 0 or i == 100:
            bestmap[i][j] = 100
        elif j == 0 or j == 100:
            bestmap[i][j] = 100
        else: 
            bestmap[i][j] = newmap[i-1][j-1]
setvisible = set()
for i in range(1, len(bestmap)):
    currenthighest = -10
    for j in range(1, len(bestmap[i])):
        if bestmap[i][j] > currenthighest: 
            currenthighest = bestmap[i][j]
            setvisible.add((i,j))

for i in range(1, len(bestmap)):
    currenthighest = -10
    for j in range(1, len(bestmap[i])):
        if bestmap[i][-j] > currenthighest: 
            currenthighest = bestmap[i][-j]
            setvisible.add((i,101-j))
for j in range(1, len(bestmap)):
    currenthighest = -10
    for i in range(1, len(bestmap[i])):
        if bestmap[i][j] > currenthighest: 
            currenthighest = bestmap[i][j]
            setvisible.add((i,j))
for j in range(1, len(bestmap)):
    currenthighest = -10
    for i in range(1, len(bestmap[i])):
        if bestmap[-i][j] > currenthighest: 
            currenthighest = bestmap[-i][j]
            setvisible.add((101-i,j))

setofscores = set()
for i in range(1, len(bestmap)-1 ):
    for j in range(1, len(bestmap)-1):
        #lookup
        blocked = bool(False)
        k = i-1
        upvisibility = 0
        while blocked == False:   
            if bestmap[k][j] == 100:
                blocked == True
                break
            elif bestmap[i][j] > bestmap[k][j]:
                k -= 1
                upvisibility += 1
            else:
                upvisibility += 1
                blocked = True
        #lookdown
        blocked = bool(False)
        k = i+1
        downvisibility = 0
        while blocked == False:   
            if bestmap[k][j] == 100:
                blocked == True
                break
            elif bestmap[i][j] > bestmap[k][j]:
                k += 1
                downvisibility += 1
            else:
                downvisibility += 1
                blocked = True
        #lookleft
        blocked = bool(False)
        k = j-1
        leftvisibility = 0
        while blocked == False:   
            if bestmap[i][k] == 100:
                blocked == True
                break
            elif bestmap[i][j] > bestmap[i][k]:
                k -= 1
                leftvisibility += 1
            else:
                leftvisibility += 1
                blocked = True
        #lookright
        blocked = bool(False)
        k = j+1
        rightvisibility = 0
        while blocked == False:   
            if bestmap[i][k] == 100:
                blocked == True
                break
            elif bestmap[i][j] > bestmap[i][k]:
                k += 1
                rightvisibility += 1
            else:
                rightvisibility += 1
                blocked = True
        scenicscore = upvisibility*downvisibility*leftvisibility*rightvisibility
        setofscores.add((scenicscore, i, j))

print(max(setofscores))

        
                
            


