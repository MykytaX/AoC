from operator import add
import random

class cube:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        self.opensides = 6

f = open("./day18/input18.txt")
cubes = [tuple([int(i.rstrip()) for i in line.split(',')]) for line in f.readlines()] #fucking proud of this one\
cubeset = set(cubes)

space= set()
for i in range(0,20):
    for j in range(0,20):
        for k in range(0,20):
            space.add((i,j,k))
            
def objectifier(set):
    objcubes = []
    for each in set:
        newcube = cube(each[0],each[1],each[2])
        objcubes.append(newcube)
    return objcubes
    

def bfs(startpos):
    visited = {startpos}
    queue = [startpos]
    directions = {(1,0,0),(0,1,0),(0,0,1),(-1,0,0),(0,-1,0),(0,0,-1)}
    while len(queue) != 0:
        for direction in directions:
                dest = tuple(map(add, queue[0], direction))
                if   any(ele > 20 or ele < 0 for ele in dest) :
                    continue
                if dest not in cubes and dest not in visited:
                    queue.append(dest)
                    visited.add(dest)
        queue.pop(0)
        
    return visited

def lumper(groupofcubes):
    for cube1 in groupofcubes:
        for cube2 in groupofcubes:
            if cube1.x == cube2.x and cube1.y == cube2.y and abs(cube1.z-cube2.z) == 1:
                cube1.opensides -= 1    
            elif cube1.y == cube2.y and cube1.z == cube2.z and abs(cube1.x-cube2.x) == 1:
                cube1.opensides -= 1    
            elif cube1.z == cube2.z and cube1.x == cube2.x and abs(cube1.y-cube2.y) == 1:
                cube1.opensides -= 1
    sum = 0
    for each in groupofcubes:
        sum += each.opensides
    return sum 

rocks = objectifier(cubes)
sum1_opensidessealed = lumper(rocks)
air = bfs((1,1,1))
pockets = (space.difference(air)).difference(cubes)
sidesinside = 0
while len(pockets) > 0:
    continuouspocket = bfs(random.choice(tuple(pockets)))
    sidesinside += lumper(objectifier(continuouspocket))
    pockets = pockets.difference(continuouspocket)

answer = sum1_opensidessealed - sidesinside
print(answer)


