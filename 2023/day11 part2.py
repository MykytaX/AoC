import sys
from pathlib import Path
from itertools import cycle, combinations


current_file_path = Path(__file__).resolve()
parent_dir = current_file_path.parent.parent
sys.path.append(str(parent_dir))

from utils import parseinput

lines = [x.strip() for x in parseinput('inputs/2023-11.txt')]
map = []
expanded_rows_map = []
for line in lines:
    newline = list(line)
    map.append(newline)
    
for i, row in enumerate(map):
    if "#" not in row:
        expanded_rows_map.append(['X' for _ in range(len(map[0]))])
    else:
        expanded_rows_map.append(row)   
        
print(expanded_rows_map)
expanded_columns_map = [[] for _ in range(len(expanded_rows_map))]
for i in range (0,len(map[0])):
    couldbegood = True
    for row in expanded_rows_map:
        if row[i] == '#':
            couldbegood = False
            break
    if couldbegood == True:
        for j, row in enumerate(expanded_rows_map):
            expanded_columns_map[j].append("Y")
    else:
        for j, row in enumerate(expanded_rows_map):
            expanded_columns_map[j].append(row[i])

galaxies = set()
for i in range(0, len(expanded_columns_map)):
    for j in range(0, len(expanded_columns_map)):
        if expanded_columns_map[i][j] == '#':
            galaxies.add((i,j))
total_distance = 0
i=1
for pair in combinations(galaxies,2):
    #print(f'pair {i}')
    galaxy1, galaxy2 = pair
    dx = abs(galaxy1[0] - galaxy2[0])
    dy = abs(galaxy1[1] - galaxy2[1])
    distance = dx + dy
    for x in range(min(galaxy1[0], galaxy2[0]), max(galaxy2[0],galaxy1[0])):
        if expanded_columns_map[x][0] == 'X':
            distance = distance - 1 + 1000000
    for y in range(min(galaxy1[1], galaxy2[1]), max(galaxy2[1],galaxy1[1])):
        if expanded_columns_map[0][y] == 'Y':
            distance = distance - 1 + 1000000
    # distance = 0
    # explore_queue = [(galaxy1,distance)]
    # visited = set()
    # visited.add(galaxy1)
    # while explore_queue:
    #     pos, distance = explore_queue.pop(0)
    #     if pos == galaxy2:
    #         break
    #     for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]: 
    #         new_pos = (pos[0]+dx,pos[1]+dy)
    #         if (0 <= new_pos[0] < len(expanded_columns_map) and 0 <= new_pos[1] < len(expanded_columns_map[0]) 
    #             and new_pos not in visited):
    #             explore_queue.append((new_pos, distance + 1))
    #             visited.add(new_pos)
    # #print(f'exploring distance between {pair}: {distance}')
    total_distance += distance
print(total_distance)