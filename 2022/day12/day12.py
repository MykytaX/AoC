import os
f = open("./day12/input12.txt")
coolmap = f.readlines()
newcoolmap =[]
for row in coolmap:
        row = row.rstrip()
        newcoolmap.append(list(row))

startpos = (0,0)        
endpos = (0,0)
possiblestarts = []
for i in range(0, len(newcoolmap)):
    for j in range(0, len(newcoolmap[i])):
        if newcoolmap[i][j]=="S":
            startpos = (i,j)
            newcoolmap[i][j] = "a"
        if newcoolmap[i][j]=="E":
            endpos = (i,j)
            newcoolmap[i][j] = "z"
        if newcoolmap[i][j] == "a":
            possiblestarts.append((i,j))

print(startpos, endpos)

results = []

queue = [startpos]
visited = set()
prevpath = dict()
Done = False
step = 0
while not Done:
    if len(queue) > 0:
        curpos = queue[0]
    else:
        break
    for k in  [(0,1),(0,-1),(1,0),(-1,0)]:                
        try:
            assert curpos[0]+k[0] in range(0,41) and curpos[1]+k[1] in range(0,93)
        except:
            continue
        if (curpos[0]+k[0], curpos[1]+k[1]) == endpos:
            prevpath.update({"("+ str(endpos[0])+","+ str(endpos[1]) + ")": curpos})
            curpos = endpos
            while curpos != startpos:
                curpos = prevpath["("+ str(curpos[0])+","+ str(curpos[1]) + ")"]
                if curpos == startpos:
                    Done = True
                    print(step+3)
                    os.system('cls')
                    for i in range(0, len(newcoolmap)):
                        for j in range(0, len(newcoolmap[i])):
                            print("".join(newcoolmap[i]))
                    results.append(step+3)
                    break
                step += 1
            Done = True
            break
        try:
            if ord(newcoolmap[curpos[0]+k[0]][curpos[1]+k[1]]) <= ord(newcoolmap[curpos[0]][curpos[1]])+1:
                if (curpos[0]+k[0],curpos[1]+k[1]) not in visited:
                    queue.append((curpos[0]+k[0],curpos[1]+k[1]))
                    prevpath.update({"("+ str(curpos[0]+k[0])+","+ str(curpos[1]+k[1]) + ")": curpos})
                    visited.add((curpos[0]+k[0],curpos[1]+k[1]) )
        except:
            continue    
        printcoolmap = newcoolmap
        visited.add((curpos[0],curpos[1]) )
    queue.pop(0)
    


