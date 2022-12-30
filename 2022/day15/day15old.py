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
for y in range(0,4000000)
    newdict.update({str(y):[]})
    for s in sensors:
        if y in range(Sy-s.distance, Sy+s.distance + 1):
            Sleft= s.Sx-s.distance-abs(s.sY - y)
            if Sleft < 0:
                Sleft = 0
            Sright = s.Sx+s.distance-abs(s.sY - y)
            if Sright > 4000000:
                Sright = 4000000
            newdict[str(y)].append(Sleft,Sright)



    for i in range(0, distance+1):
        if s.Sy+i in range(0,4000000) or s.Sy-i in range(0,4000000):
            if str(s.Sy+i) not in mapdict.keys():
                mapdict.update({str(s.Sy+i): set()})
            if str(s.Sy-i) not in mapdict.keys():
                mapdict.update({str(s.Sy-i): set()})
            for j in range(0,distance+1-i):
                   if i == 0:
                        mapdict[str(s.Sy)].add(s.Sx+j)
                        mapdict[str(s.Sy)].add(s.Sx-j)
                   else:
                        mapdict[str(s.Sy+i)].add(s.Sx+j)
                        mapdict[str(s.Sy-i)].add(s.Sx+j)
                        mapdict[str(s.Sy+i)].add(s.Sx-j)
                        mapdict[str(s.Sy-i)].add(s.Sx-j)

for i in range(0,4000000):
    for j in range(0,4000000):
        for s in sensors:
            if s.distance < abs(s.Sx-i)+abs(s.Sy - j):


print(len(mapdict["2000000"]))