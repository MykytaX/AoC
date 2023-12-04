
import sys
from pathlib import Path

current_file_path = Path(__file__).resolve()
parent_dir = current_file_path.parent.parent
sys.path.append(str(parent_dir))

from utils import parseinput

lines = parseinput("inputs/2023-2.txt")

gg = 0
bagmax = {'red': 12, 'green': 13, 'blue': 14}
Games = []
for line in lines:
	Game = {'id' : None, 'rounds': []}
	idstr, roundsstr = line.split(':')
	_, Game['id'] = idstr.split(' ')
	for roundstr in roundsstr.split(';'):
		properround = {'red': 0, 'green': 0, 'blue': 0}
		haul = roundstr.strip().split(',')
		for datum in haul:
			number, color = datum.strip().split(' ')
			properround[color] = number
		Game['rounds'].append(properround)
	Games.append(Game)

#Part 1

# for Game in Games:
# 	valid = True
# 	for Round in Game['rounds']:
# 		for color in Round.keys():
# 			if int(Round[color])> bagmax[color]:
# 				valid = False
# 				break
# 	if valid:
# 		gg += int(Game['id'])

#Part 2

total_power = 0
for Game in Games:
	cur_bag = {'red': 0, 'green': 0, 'blue': 0}
	for Round in Game['rounds']:
		for color in Round.keys():
			if int(Round[color])> cur_bag[color]:
				cur_bag[color] = int(Round[color])

	total_power += cur_bag['red']*cur_bag['blue']*cur_bag['green']
		
print(total_power)

