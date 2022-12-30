f = open("./input9.txt")
instructions = f.readlines()
head = [0,0]
tail = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]

visited=set()

def updatetail(headx, tailx):
	if (abs(headx[0]-tailx[0]) >= 2 or abs(headx[1]-tailx[1]) >= 2):
		 	if headx[0]-tailx[0] > 0:	
			 	tailx[0]+= 1
	 		elif headx[0]-tailx[0] < 0:
			 	tailx[0] -=1
		 	if headx[1]-tailx[1] > 0:
			 	tailx[1]+= 1
	 		elif headx[1]-tailx[1] < 0:
			 	tailx[1] -=1
	return tailx
	
for instruction in instructions:
	instruction = instruction.rstrip()
	direction, spaces = instruction.split(" ")
	for i in range(0, int(spaces)):
		if direction == "U":
			head[1] += 1
		elif direction == "D":
		    head[1] -= 1
		elif direction == "L":
			head[0] -= 1
		else:
			head[0] += 1
		for k in range(0, 9):
			if k == 0:
				tail[0] = updatetail(head, tail[0])
			else:
				tail[k] = updatetail(tail[k-1], tail[k])
			if k==8:
				visited.add((tail[8][0],tail[8][1]))

print(len(visited))
			
	
		
		
	 