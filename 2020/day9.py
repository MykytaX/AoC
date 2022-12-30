import numpy as np
import matplotlib.pyplot as pyplot
f = open("input9.txt")

lines = f.readlines()
betterlines = []
for line in lines:
    newline = line.replace("\n","")
    betterlines.append(newline)
colorflag = 0
heightmap = np.zeros((102,102), dtype=int)

for i in range(0,102):
    heightmap[i][0] = 10 
    heightmap[i][101] = 10
    for j in range(0,102):
        heightmap[0][j] = 10
        heightmap[101][j] = 10

for i in range(1,101):
    for j in range(1,101):
        heightmap[i][j] = list(betterlines[i-1])[j-1]

def basin_probe(locationset, colorflag):
    oldlocationset = locationset.copy()
    for location in oldlocationset:
        i = location[0]
        j = location[1]
       
      #  print("Scanning up..")
        if heightmap[i+1][j] < 9:
      #      print("It's flowing!")
            locationset.add((i+1,j))
            
     #   print("Scanning down..")
        if heightmap[i-1][j] < 9:
    #        print("It's flowing!")
            locationset.add((i-1,j))
    #    print("Scanning right..")
        if heightmap[i][j+1] < 9:
    #        print("It's flowing!")
            locationset.add((i,j+1))
    #    print("Scanning left..")
        if heightmap[i][j-1] < 9:
    #        print("It's flowing!")
            locationset.add((i,j-1))
    if len(locationset) == len(oldlocationset):
        print(colorflag)
        if len(locationset) in [9, 99, 100, 103]:
            for location in locationset:
                pyplot.plot(location[0],location[1], "bo")
        elif colorflag == 1:
            for location in locationset:
                pyplot.plot(location[0],location[1], "ro")       
        elif colorflag == 0:
            for location in locationset:
                pyplot.plot(location[0],location[1], "go") 
        print("IT STOPPED! This basin is " + str(len(locationset)) + " blocks big")
        
        return len(locationset)
    else: 
        return basin_probe(locationset, colorflag)


basinsizes = []
risk = 0
for i in range(1,101):
    for j in range(1, 101):
    #   print("For position "+ str(i)+", "+ str(j))
    #    print("The number is "+ str(heightmap[i][j]))
        try:
            up = heightmap[i-1][j]
        except: 
            up = 10
        try:
            down = heightmap[i+1][j]
        except: 
            down = 10  
        try:
            right = heightmap[i][j+1]    
        except: 
            right = 10
        try:
            left = heightmap[i][j-1]
        except: 
            left = 10
    #    print("Up is " + str(up) + " down is " + str(down) + " left is " + str(left) + " right is " + str(right))
        if heightmap[i][j] == min(heightmap[i][j],up,down,left,right) and heightmap[i][j] not in [up, down, left, right]:
            print("Got one! At " + str(i) + str(j))
            risk += 1
            locationset = {(i,j)}
            if colorflag == 0:
                basinsize = basin_probe(locationset, colorflag)
                colorflag = 1
            else:
                basinsize = basin_probe(locationset, colorflag)
                colorflag = 0
            basinsizes.append(basinsize)
    #    else: print("Nah!")
total = 0
print(basinsizes, len(basinsizes), risk)
pyplot.show()
# sortedlist = basinsizes.sort()
# total = sortedlist[0]+sortedlist[1]+sortedlist[2]
# print("The answer is " + str(total))


    

