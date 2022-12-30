f = open("./data.txt")
everything = f.read()

pairs = everything.split("\n")

print(pairs)

def compare_elements(line1,line2):
    for element1, element2 in zip(line1, line2):
        if isinstance(element1, int) and isinstance(element2, int):
            if element1 > element2:
                return False
            elif element1 < element2:
                return True
            elif element1 == element2:
                continue
        elif isinstance(element1, list) and isinstance(element2, list):
            ans = compare_elements(element1, element2)
            if ans == "unknown":
                continue
            else:
                return ans
        elif isinstance(element1, int) and isinstance(element2, list):
            ans = compare_elements([element1], element2)
            if ans == "unknown":
                continue
            else:
                return ans
        elif isinstance(element1, list) and isinstance(element2, int):
            ans = compare_elements(element1, [element2])
            if ans == "unknown":
                continue
            else:
                return ans
    if len(line1)<len(line2):
        return True
    elif len(line2)< len(line1):
        return False
    else:
        return "unknown"
            


[[[[8,7,8,5,4],6,[4,6]]],[6,[[]]],[]]
[[[[8,0,0,7,1],[1],8]]]


while count !=0:
    count = 0
    for i in range(0,len(pairs)-1):
        aas = 2


sum = 0
for i in range(0,len(pairs)): # remember to i+1 later
    line1, line2 = pairs[i].split()
    elementsofline1 = eval(line1)
    elementsofline2 = eval(line2)
    if compare_elements(elementsofline1, elementsofline2) == True:
        sum += i+1

print(sum)