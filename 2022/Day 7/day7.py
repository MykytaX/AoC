from treelib import Node, Tree


f = open("./day7/input.txt")
block = ""
instructions = f.readlines()
FileSystem = Tree()
FileSystem.create_node("/+", "/", data=0)

for instruction in instructions:
    block += instruction
    
newinstructions = block.split("$")
print(newinstructions)
path = []
for instruction in newinstructions:
    instruction = instruction.rstrip()
    if instruction == " cd ..":
        path.pop()
    elif instruction[:3] == " cd":
        path.append(instruction[4:])
    if instruction[:3] == " ls":
        lines = instruction.split("\n")
        lines.pop(0)
        for line in lines:
            elem1, elem2 = line.split(" ")
            if elem1 == "dir":
                FileSystem.create_node(tag=elem2, identifier="+".join(path)+"+"+elem2, parent="+".join(path), data = 0)
            else:
                node = FileSystem.get_node("+".join(path))
                FileSystem.update_node("+".join(path),  data = node.data + int(elem1))

dirsize = 0
def getdirsize (dir):
    size = dir.data
    for child in dir.fpointer:
        size += getdirsize(FileSystem.get_node(child))
    return size
total = getdirsize(FileSystem.get_node("/"))
freespace = 70000000 - total
needtofree = 30000000 - freespace
ListofDir = []
for dir in FileSystem.all_nodes_itr():
    cursize = getdirsize(dir)
    if cursize >= needtofree:
        ListofDir.append(cursize)


print(min(ListofDir))

        