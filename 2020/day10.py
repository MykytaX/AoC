f = open("inpur10.txt")
lines = f.readlines()
codelines = []
for line in lines:
    codelines.append(line.replace("\n", ""))
prizebag = []
originalcodelines = list(codelines)
prizes =  []  
for codeline in codelines:
    breakflag = 0
    charlist = list(codeline)
    expectation_list = []
    for char in charlist:
        if char == "(": expectation_list.append(")")
        elif char == "[": expectation_list.append("]")
        elif char == "{": expectation_list.append("}")
        elif char == "<": expectation_list.append(">")
        elif char in [")","]","}",">"]:
            if char == expectation_list[-1]:
                expectation_list.pop()
            else:
                breakflag = 1
                break
    
    if breakflag == 1:
        continue            
      
    expectation_list.reverse()
    prizeforline = 0
    fixedcodeline = codeline
    for char in expectation_list:
        fixedcodeline = fixedcodeline + char
        prizeforline = prizeforline*5
        if char == ")": prizeforline += 1
        if char == "]": prizeforline += 2
        if char == "}": prizeforline += 3
        if char == ">": prizeforline += 4
    prizes.append(prizeforline)

print(sorted(prizes)[24])


