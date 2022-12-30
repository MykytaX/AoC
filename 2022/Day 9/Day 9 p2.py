f = open("./input.9.txt")
instructions = f.readlines()
head = [0,0]
tail = [0,0]
visited=set([0,0])
for instruction in instructions:
	instruction = instruction.rstrip()
	direction, spaces = instruction.split(" ")
	for i in range(0, spaces):
		if direction == "U":
			head[1] += 1
		elif direction == "D":
			head[1] -= 1
		elif direction == "L":
			head[0] -= 1
		else:
			head[0] += 1
		updatetail()

def updatetail():
	if (abs(head[0]-tail[0]) >= 2 or abs(head[1]-head[0]) >= 2):
			if head[0]-tail[0] > 0:	
				tail[0]+= 1
			else:
				tail[0] -=1
			if head[1]-tail[1] > 0:
				tail[1]+= 1
			else:
				tail[1] -=1
	visited.add(tail)
	
print(len(visited))
			
	
		
		
	 