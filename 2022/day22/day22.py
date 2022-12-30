f = open("./day22/input22.txt")

map = f.readlines()
newmap = []
for line in map:
    newmap.append(line)
startpos = (1,9)

down = (1,0)
up = (-1,0)
left = (0,-1)
right = (0, 1)

cardinals = {down, left, up, right}
facing = 3

directions = "10R5L5R10L4R5L5"
dir = []
i = 0
while i < len(directions):
    try: 
        int(directions[i])
    except:
        dir.append(directions[i])
        i += 1
    else:
        try:
            int(directions[i+1])
        except:
            dir.append(int(directions[i]))
            i += 1
        else:    
            dir.append(int(directions[i]+directions[i+1]))
            i += 2
curpos = startpos
for step in dir:
    if step == "R":
        facing = (facing+1)%4
    elif step == "L":
        facing = (facing-1)%4
    else:
        for move in range(0,step):
            lookahead = (curpos[0]+cardinals[facing][0], curpos[1]+cardinals[facing][1])
            if newmap[lookahead[0]][lookahead[1]] == ".":
                curpos = lookahead
            elif newmap[lookahead[0]][lookahead[1]] == "#":
                break
            else:
                oppfacing = (facing + 2)%4
                potential = curpos
                search = newmap[curpos[0]][curpos[1]]
                while search != " " or search != "\n":
                    potential = (potential)
