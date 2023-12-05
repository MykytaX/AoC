def newparseinput(url: str):
    f = open(url, encoding="utf-8")
    allfile = f.read()
    return allfile

lines = newparseinput('inputs/2023-5.txt')

sections = lines.split('\n\n')

_, seedsstr = sections[0].split(':')
seeds = [int(x) for x in seedsstr.strip().split(' ')]
maps = []
for seedmap in sections[1:]:
    _, data = seedmap.split(':')
    ranges = data.strip().split('\n')
    goodranges = []
    for run in ranges:
        goodrun = {"ds": 0, "ss": 0, "rl": 0}
        dest_start, source_start, range_length = run.split(' ')
        goodrun.update({"ds":int(dest_start), "ss": int(source_start), "rl" : int(range_length)})
        goodranges.append(goodrun)
    maps.append(goodranges)

print(maps)
# PART 1
def mapify(seed, map, depth):
    mapping = 0
    for run in map:
        if run['ss'] <= seed <= run['ss'] + run['rl']:
            mapping = run['ds'] + ( seed - run['ss'])
            break
        else: 
            continue
    if mapping == 0:
        mapping = seed   
    if depth < 6:
        return mapify(mapping, maps[depth+1], depth+1)
    else:
        return mapping
            
locations = []
for seed in seeds:
    location = mapify(seed, maps[0], 0)
    locations.append(location)
    
print(min(locations))

#PART2
def mapify2(listofranges, map, depth):
    listofmappings = []
    for run in map:
        for onerange in listofranges:
            minimum = onerange[0]
            maximum = onerange[0] + onerange[1]
            if run['ss'] in range(minimum, maximum):
                if run['ss']+run['rl'] in range(minimum,maximum):
                    newdeststart = run['ds'] 
                    newdestfinish = run['ds'] + run['rl']
                    listofmappings.append([newdeststart, newdestfinish])
                    listofranges.remove(onerange)
                    listofranges.append((minimum, run['ss']),(run['ss']+run['rl'],maximum))
                    break
                else:
                    newdeststart = run['ds']
                    newdestfinish = run['ds'] + (maximum - run['ss'])
                    listofmappings.append([newdeststart, newdestfinish])
                    listofranges.remove(onerange)
                    listofranges.append(minimum, run['ss'])
                    continue
            else:
                
        
        
    if depth < 6:
        return mapify(mapping, maps[depth+1], depth+1)
    else:
        return mapping
newlocations = []
for i in range(0, len(seeds), 2):
        listofranges = [(seed[i], seed[i+1])]
        location = mapify2(listofranges, maps[0],0)
        newlocations.append(location)
        

print(min(newlocations))