f = open("./day13/input13.txt")
everything = f.read()

pairs = everything.split("\n\n")

print(pairs)

def compare_elements(line1,line2):
    for element1, element2 in zip(line1, line2):
        if isinstance(element1, int) and isinstance(element2, int):
            if element1 > element2:
                return False
            else:
                continue
        elif isinstance(element1, list) and isinstance(element2, list):
            if compare_elements(element1, element2) == False:
                return False       
        elif isinstance(element1, int) and isinstance(element2, list):
            if compare_elements(list[element1], element2) == False:
                return False
        elif isinstance(element1, list) and isinstance(element2, int):
            if compare_elements(element1, [element2]) == False:
                return False
            


[[[[8,7,8,5,4],6,[4,6]]],[6,[[]]],[]]
[[[[8,0,0,7,1],[1],8]]]

for i in range(0,len(pairs)): # remember to i+1 later
    line1, line2 = pairs[i].split()
    elementsofline1 = eval(line1)
    elementsofline2 = eval(line2)
    compare_elements(elementsofline1, elementsofline2)