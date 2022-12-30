f = open("input12.txt")
connections = f.readlines()
betterconnections = []
for line in connections:
    betterconnections.append(line.replace("\n", ""))
map = {}
for connection in betterconnections:
    x, y = connection.split("-")
    if x not in map:
        map.update({x: [y]})
    else:
        map[x].append(y)
for connection in betterconnections:
    x, y = connection.split("-")
    if y not in map:
        map.update({y: [x]})
    else:
        map[y].append(x)
possiblePaths = set()
currentpath = []

def checkforduplicates(currentpath):
    for location in currentpath:
        count = 0
        if location.islower() and location not in ["start", "end"]:
            for location2 in currentpath:
                if location == location2:
                    count += 1
                if count >= 2:
                    return True   
    return False
        
                                    

def mapexplorerWincy(currentpos, currentpath, map, possiblePaths):
    for exit in map[currentpos]:
        if exit == "start":
            continue
        elif exit == "end":
            currentpath.append("end")
            possiblePaths.add(tuple(currentpath))
            currentpath.pop()
        else:
            if exit.islower():
                if exit in currentpath:
                    if not checkforduplicates(currentpath):
                        currentpath.append(exit)
                        mapexplorerWincy(exit, currentpath, map, possiblePaths)
                        currentpath.pop()
                    else:
                        continue
                else: 
                    currentpath.append(exit)
                    mapexplorerWincy(exit, currentpath, map, possiblePaths)
                    currentpath.pop()
            else:
                currentpath.append(exit)
                mapexplorerWincy(exit, currentpath, map, possiblePaths)
                currentpath.pop()
currentpath =["start"]
mapexplorerWincy("start", currentpath, map, possiblePaths)
print(possiblePaths, len(possiblePaths))


            
        
    
