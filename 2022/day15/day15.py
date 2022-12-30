class sensor:
    def __init__(self, Sx, Sy, Bx, By):
        self.Sx = Sx
        self.Sy = Sy
        self.Bx = Bx
        self.By = By
        self.distance = int()

sensors = []
f= open("./day15/input15.txt")
lines = f.readlines()
for line in lines:
    line = line.rstrip()
    _, _, Sx, Sy,_, _,_,_, Bx, By =  line.split(" ")
    newsensor = sensor(int(Sx[2:-1]), int(Sy[2:-1]), int(Bx[2:-1]), int(By[2:]))
    sensors.append(newsensor)
mapdict = {}

for s in sensors:
    s.distance = abs(s.Sx - s.Bx)+abs(s.Sy - s.By)

newdict = {}
for y in range(0,4000001):
    if y % 10000 == 0:
        print(y)
    newdict.update({str(y):[]})
    for s in sensors:
        if y in range(s.Sy-s.distance, s.Sy+s.distance + 1):
            Sleft= s.Sx-s.distance+abs(s.Sy - y)
            if Sleft < 0:
                Sleft = 0
            Sright = s.Sx+s.distance-abs(s.Sy - y)
            if Sright > 4000000:
                Sright = 4000000
            newdict[str(y)].append(range(Sleft,Sright+1))
    newdict[str(y)] = sorted(newdict[str(y)] , key=lambda r: r.start)

print(newdict)
doneflag = False
for y, ranges in newdict.items():
    curmax = 0
    for i in range(0,len(ranges)-1):
        if ranges[i][-1] > curmax:
            curmax = ranges[i][-1]
        if ranges[i+1][0] > curmax:
            print("Gotcha!", " x= ", curmax+1)
            doneflag = True
            break
    if doneflag == True:
        print("y= ", y)
        break
    
        



