f = open("./day13/input13.txt")
everything = f.read()

results = []

pairs = everything.split("\n\n")
for i in range(0,len(pairs)): # remember to i+1 later
    doneflag = 0
    line1, line2 = pairs[i].split()
    map = {"[": " ", "]": " ", ",":" "}
    mytable1 = line1.maketrans(map)
    mytable2 = line2.maketrans(map)

    numline1 = line1.translate(mytable1)
    numline2 = line2.translate(mytable2)

    cornumline1 = numline1.split()
    cornumline2 = numline2.split()
    for num1, num2 in zip(cornumline1, cornumline2):
        if int(num1) > int(num2):
            
            doneflag = 1
            break
        if int(num1) == int(num2):
            continue
        if int(num1) < int(num2):
            results.append(i+1)
            doneflag = 1
            break
    if doneflag == 1:
        continue
    else:
        if len(line2) > len(line1):
            results.append(i+1)

print(sum(results))