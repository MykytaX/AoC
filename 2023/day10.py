import sys
from pathlib import Path
from itertools import cycle
import matplotlib.pyplot as plt


fig, ax = plt.subplots()
ax.set_xlim(0, 140)
ax.set_ylim(0, 140)
    
    
current_file_path = Path(__file__).resolve()
parent_dir = current_file_path.parent.parent
sys.path.append(str(parent_dir))

from utils import parseinput
print(sys.path)

lines = [x.strip() for x in parseinput('C:\\CreativeUnsorted\\Programming\\AoC\\AoC\\inputs\\2023-10.txt')]
print(lines)
map = []
for line in lines:
    newline = list(line)
    map.append(newline)


def find_starting_position(map) -> tuple:
    for i in range(0,len(map)):
        for j in range(0,len(map[i])):
            if map[i][j] == 'S':
                return (i,j)
            else:
                continue
    return KeyError # type: ignore

start_pos = find_starting_position(map)

def where_to_from_start(pos, map, came_from_pos):
    discovered_paths = []
    x_row = pos[0]
    y_column = pos[1]
    # check up
    try:
        if map[x_row-1][y_column] in {'7','|','F'}:
            if (x_row-1,y_column) != came_from_pos:
                discovered_paths.append((x_row-1,y_column))
    except:
        pass
    try:
        if map[x_row][y_column-1] in {'F','-','L'}:
            if (x_row,y_column-1) != came_from_pos:
                discovered_paths.append((x_row,y_column-1))
    except:
        pass
    try:
        if map[x_row + 1][y_column] in {'L','|','J'}:
            if (x_row + 1,y_column) != came_from_pos:
                discovered_paths.append((x_row+1,y_column))
    except:
        pass
    try:
        if map[x_row][y_column+1] in {'7','-','J'}:
            if (x_row,y_column + 1) != came_from_pos:
                discovered_paths.append((x_row,y_column+1))
    except:
        pass    
    return discovered_paths

def where_to(pos, map, came_from_pos):
    potential_paths = []
    x_row = pos[0]
    y_column = pos[1]
    try:
        up = map[x_row-1][y_column]
        up_pos = (x_row-1,y_column)
    except:
        up = None
        up_pos = None
    try:
        left = map[x_row][y_column-1]
        left_pos = (x_row, y_column-1)
    except:
        left = None
        left_pos = None
    try:   
        down = map[x_row + 1][y_column]
        down_pos = (x_row + 1, y_column)
    except:
        down = None
        down_pos = None
    try:
        right = map[x_row][y_column+1]
        right_pos = (x_row,y_column+1)
    except:
        right = None
        right_pos = None
    
    match map[pos[0]][pos[1]]:
        case '7':
            if down in {'L','|','J'} and down_pos != came_from_pos:
                return down_pos
            if left in {'F', '-', 'L'} and left_pos != came_from_pos:
                return left_pos
        case '|':
            if down in {'L','|','J'} and down_pos != came_from_pos:
                return down_pos
            if up in {'7','|','F'} and up_pos != came_from_pos:
                return up_pos
        case 'F':
            if down in {'L','|','J'} and down_pos != came_from_pos:
                return down_pos
            if right in {'7', '-', 'J'} and right_pos != came_from_pos:
                return right_pos
        case '-':
            if left in {'F', '-', 'L'} and left_pos != came_from_pos:
                return left_pos
            if right in {'7', '-', 'J'} and right_pos != came_from_pos:
                return right_pos
        case 'J':
            if left in {'F', '-', 'L'} and left_pos != came_from_pos:
                return left_pos  
            if up in {'7','|','F'} and up_pos != came_from_pos:
                return up_pos  
        case 'L':
            if right in {'7', '-', 'J'} and right_pos != came_from_pos:
                return right_pos
            if up in {'7','|','F'} and up_pos != came_from_pos:
                return up_pos

visited_pos = set()

def explore(map,start_pos) -> int:
    current_pos = start_pos 
    came_from_pos = None
    drone1pos, drone2pos = where_to_from_start(start_pos, map, None)
    came_from_pos1 = start_pos
    came_from_pos2 = start_pos
    visited_pos.add(start_pos)
    visited_pos.add(drone1pos)
    visited_pos.add(drone2pos)
    step = 1
    
    while True:
        candidate_for_came_from = drone1pos
        drone1pos = where_to(drone1pos, map, came_from_pos1)

        visited_pos.add(drone1pos)
        came_from_pos1 = candidate_for_came_from
        candidate_for_came_from = drone2pos
        drone2pos = where_to(drone2pos, map, came_from_pos2)
        
        visited_pos.add(drone2pos)
        came_from_pos2 = candidate_for_came_from
        step += 1
        if drone1pos == drone2pos:
            break
    return step



    return n_crossings % 2 == 1 


def point_in_polygon_test(point: tuple, map: list[list], visited_pos: set) -> bool:
    x = point[0]
    y = point[1]
    Lopen = False
    Jopen = False
    ray_up_crossings = 0 
    i = 1
    #shotup
    while (x - i > 0):
        try:
            if (x-i, y) in visited_pos:
                if map[x-i][y] == '-':
                    ray_up_crossings += 1
                elif map[x-i][y] == 'L':
                    Lopen = True
                elif map[x-i][y] == 'J':
                    Jopen = True
                elif map[x-i][y] == 'F':
                    if Jopen:
                        ray_up_crossings += 1
                        Jopen = False
                    if Lopen:
                        Lopen = False
                elif map[x-i][y] == '7':
                    if Jopen:
                        Jopen = False
                    if Lopen:
                        ray_up_crossings += 1
                        Lopen = False
        except:
            pass    
        i += 1    
    if ray_up_crossings%2 == 1:
        return True
    else:
        return False



answer_part_one = explore(map,start_pos)
answer_part_two = 0

print(answer_part_one)
f = open('Day10map.txt', 'w', encoding='utf-8')

for i in range(0, len(map)):
    f.write('\n')
    for j in range(0, len(map)):
        if (i,j) not in visited_pos:
            if point_in_polygon_test((i,j),map,visited_pos):
                answer_part_two = answer_part_two + 1
                f.write('🐇')
            else:
                f.write(' ')
        else:
            f.write(map[i][j])
            continue
f.close()    
print(answer_part_two)
