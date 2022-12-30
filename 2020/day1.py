file = open("input1.txt")
x = file.read().splitlines()

for i in range(0,len(x)):
    for j in range(i+1,len(x)):
        for g in range(i+2, len(x)):
            if int(x[i])+int(x[j])+int(x[g]) == 2020:
                print(int(x[i])*int(x[j])*int(x[g]))

