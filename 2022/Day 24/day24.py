#E######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#

class Blizzard():
    def __init__(self, pos, direction):
        self.pos = pos
        self.direction = direction
    
    def update(self):
        match self.direction:
            case "v":
                self.pos[0] += 1
            case ">":
                self.pos[1] += 1
            case "<":
                self.pos[1] -= 1
            case "^":    
                self.pos[0] -= 1
        if pos[0] == 0:
            pos[0] == 5            

f = open("./data.txt")
valley = []
lines = f.readlines()
for line in lines:
    valley.append(line.rstrip())

blizzards = []

for i in range(0, len(valley)):
    for j in range(0, len(valley[i])):
        if valley[i][j] in {">", "<", "v", "^"}:
            b = Blizzard((i, j),valley[i][j])
            blizzards.append(b)
