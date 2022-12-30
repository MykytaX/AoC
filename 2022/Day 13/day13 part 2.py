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

count = 1
while count !=0:
    print(count)
    count = 0
    for i in range(0,len(pairs)-1):
        elementsofline1 = eval(pairs[i])
        elementsofline2 = eval(pairs[i+1])
        if compare_elements(elementsofline1, elementsofline2) == False:
            temp = pairs[i]
            pairs[i] = pairs[i+1]
            pairs[i+1] = temp
            count += 1

result = (pairs.index('[[2]]')+1)*(pairs.index('[[6]]')+1)
print(result)
