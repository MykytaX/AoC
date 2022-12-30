f = open("./day14/input14.txt")
lines =f.readlines()
mapsand = []
for i in range(0, 700):
        mapsand.append([])
        for j in range(0, 700):
                if j == 179: 
                        mapsand[i].append("+")
                else:
                        mapsand[i].append(" ")
                
findmaxdepth=set()
for line in lines:
        line = line.rstrip()
        points = line.split(" -> ")
        for k in range(1, len(points)):
                point1 = points[k-1]
                point2 = points[k]
                point1x, point1y = point1.split(",")
                point1x = int(point1x)
                point1y = int(point1y)
                point2x, point2y = point2.split(",")
                point2x = int(point2x)
                point2y = int(point2y)
                findmaxdepth.add(point1y)
                findmaxdepth.add(point2y)
                for l in range(min(point1x,point2x), max(point1x,point2x)+1):
                        for m in range(min(point1y, point2y), max(point2y, point1y)+1):
                                mapsand[l][m] = "+"

print("".join(mapsand[179]))
maxdepth = max(findmaxdepth)


systematrest = False
grains = 0
while not systematrest:
    grain = [500, 0]
    grains += 1
    grainatrest = False
    while not grainatrest:
            if mapsand[500][0] == "o":
                    systematrest = True
                    break
            if mapsand[grain[0]][grain[1]+1] == " ":
                    grain[1] = grain[1] +1
                    continue
            elif mapsand[grain[0]-1][grain[1]+1]== " ":
                    grain[1] += 1
                    grain[0] -= 1
            elif mapsand[grain[0]+1][grain[1]+1] == " ":
                    grain[1] += 1
                    grain[0] += 1
            else:
                    grainatrest = True
                    mapsand[grain[0]][grain[1]] = "o"
                    print(grain)
                    break

print(grains)