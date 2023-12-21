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
        dest_start, source_start, range_length = run.strip().split(' ')
        offset = int(source_start) - int(dest_start)
        goodrun = {'range': range(int(source_start), int(source_start) + int(range_length)),'offset': offset}
        goodranges.append(goodrun)
    maps.append(goodranges)

# # PART 1 no longert works with the new solution
# def mapify(seed, map, depth):
#     mapping = 0
#     for run in map:
#         if run['ss'] <= seed <= run['ss'] + run['rl']:
#             mapping = run['ds'] + ( seed - run['ss'])
#             break
#         else: 
#             continue
#     if mapping == 0:
#         mapping = seed   
#     if depth < 6:
#         return mapify(mapping, maps[depth+1], depth+1)
#     else:
#         return mapping
            
# locations = []
# for seed in seeds:
#     location = mapify(seed, maps[0], 0)
#     locations.append(location)

def combine_overlapping_ranges(ranges):
    # Sort by start of range
    sorted_ranges = sorted(ranges, key=lambda r: r.start)

    combined = []
    current_start = sorted_ranges[0].start
    current_end = sorted_ranges[0].stop

    for r in sorted_ranges[1:]:
        if r.start <= current_end:  # Overlaps with current range, extend the current range
            current_end = max(current_end, r.stop)
        else:  # Doesn't overlap, start a new range
            combined.append(range(current_start, current_end))
            current_start = r.start
            current_end = r.stop

    # Add the last range
    combined.append(range(current_start, current_end))

    return combined

def intersection_of_range_with_list(single_range, range_list):
    intersections = []
    for r in range_list:
        start = max(single_range.start, r.start)
        end = min(single_range.stop, r.stop)
        if start < end:
            intersections.append(range(start, end))
    return intersections

def difference_of_range_with_list(single_range, range_list):
    differences = [single_range]  # Start with single_range in differences
    for r in range_list:
        temp = []
        for d in differences:
            start = max(d.start, r.start)
            end = min(d.stop, r.stop)
            if start < end:  # There is an intersection
                if d.start < start:  # There are values in d before the intersection
                    temp.append(range(d.start, start))
                if end < d.stop:  # There are values in d after the intersection
                    temp.append(range(end, d.stop))
            else:  # There is no intersection, so the difference is d itself
                temp.append(d)
        differences = temp
    return differences

def mapify2(resultlist, map, depth):
    destmappedranges = []
    for seedrange in resultlist:
        onerangemapped = []
        for sourcerange in map:
            start = max(seedrange.start, sourcerange['range'].start)
            end = min(seedrange.stop, sourcerange['range'].stop)
            if start < end:
                onerangemapped.append(range(start, end))
                destmappedranges.append(range(start-sourcerange['offset'], end-sourcerange['offset']))
        if onerangemapped == []:
            destmappedranges.append(seedrange)
        else:
            leftovers = difference_of_range_with_list(seedrange, onerangemapped)
            destmappedranges.extend(leftovers)
    if depth < 6:
        result = mapify2(destmappedranges, maps[depth+1], depth+1)
        return result
    else:
        return destmappedranges
    
seedlist = []

for i in range(0, len(seeds), 2):
        seedstart = seeds[i]
        seedend = seeds[i] + seeds[i+1]
        seedrange = range(seedstart, seedend)
        seedlist.append(seedrange)

location = None
resultranges = mapify2(seedlist, maps[0],0)
for ranger in resultranges: 
    if location == None:
        location = ranger.start
    elif ranger.start < location:
        location = ranger.start
    else:
        continue

print(location)