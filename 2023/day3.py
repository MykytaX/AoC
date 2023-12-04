
import sys
from pathlib import Path

current_file_path = Path(__file__).resolve()
parent_dir = current_file_path.parent.parent
sys.path.append(str(parent_dir))

from utils import parseinput

lines = parseinput("inputs/2023-3.txt")


map = []


for line in lines:
    onemapline = list(line)
    map.append(onemapline)

#Part1 

# def validatenumber(number, i, j):
#     positionstocheck = []
#     startpos = j - len(number) - 1
#     endpos = j
#     positionstocheck.extend((i-1,x) for x in range(startpos, endpos+1))
#     positionstocheck.append((i,j - len(number) - 1))
#     positionstocheck.append((i,j))
#     positionstocheck.extend((i+1,x) for x in range(startpos, endpos+1))
#     for pos in positionstocheck:
#         x, y = pos
#         if x < 0 or y < 0:
#             continue
#         if x > 139 or y > 139:
#             continue
#         if  map[x][y] != '.' and map[x][y].isdigit() == False:
#             return True

# total = 0
# number = ''
# for i in range(0, len(map)):
#     for j in range(0, len(map[i])):
#         if map[i][j].isdigit():
#             number += map[i][j]
#             if number == '917':
#                 pass
#             if j == 139:
#                 if validatenumber(number, i, j+1):
#                     print(f'Validated number: {number}')
#                     total += int(number)
#                 number = ''
#                 continue
#         elif map[i][j].isdigit() == False and number != '':
#             if validatenumber(number, i, j):
#                 print(f'Validated number: {number}')
#                 total += int(number)
#             number = ''
#         else:
#             continue

# print(total)

#Part2
totalgearration = 0
potential_gears = {}
discovered_gears = {}
discarded_gears = {}

def checknumber(number, i, j):
    positionstocheck = []
    startpos = j - len(number) - 1
    endpos = j
    positionstocheck.extend((i-1,x) for x in range(startpos, endpos+1))
    positionstocheck.append((i,j - len(number) - 1))
    positionstocheck.append((i,j))
    positionstocheck.extend((i+1,x) for x in range(startpos, endpos+1))
    for pos in positionstocheck:
        x, y = pos
        if x < 0 or y < 0:
            continue
        if x > 139 or y > 139:
            continue
        if  map[x][y] == '*':
            if (x,y) in potential_gears.keys():
                discovered_gears.update({(x,y): int(number)*potential_gears[(x,y)]})
                potential_gears.pop((x,y))
            elif (x,y) in discovered_gears.keys():
                discovered_gears.pop((x,y))
                discarded_gears.update((x,y))
            else:
                if (x,y) not in discarded_gears.keys():
                    potential_gears.update({(x,y): int(number)})

            



number = ''
for i in range(0, len(map)):
    for j in range(0, len(map[i])):
        if map[i][j].isdigit():
            number += map[i][j]
            if j == 139:
                checknumber(number, i, j+1)
                number = ''
                continue
        elif map[i][j].isdigit() == False and number != '':
                checknumber(number, i, j)
                number = ''
        else:
            continue

print(sum(discovered_gears.values()))

