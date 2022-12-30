f = open("./DAY19/input19.txt")

numbers = [int(x.rstrip()) for x in f.readlines()]
dict = {}
const = 811589153//5000
remainder = 811589153%5000

for i in range(0,len(numbers)):
    dict.update({str(i): [numbers[i],i]})
    if numbers[i] == 0:
        print(i)
dict2 = {"0": [1,0], "1":[2,1], "2":[-3,2], "3":[3,3], "4":[-2,4], "5":[0,5], "6":[4,6]}

count = 0 
for i in range(0, len(dict)*10):
    movingvalue = i%len(dict)
    if i%1000== 0:
        print(i)
    if i > 6:
        count += 1
    oldpos = dict[str(movingvalue)][1]
    dict[str(movingvalue)][1]  += dict[str(movingvalue)][0]
    if dict[str(movingvalue)][1] > len(dict) or  dict[str(movingvalue)][1] < 0:
        dict[str(movingvalue)][1] = dict[str(movingvalue)][1]%(len(dict)-1)
    if   dict[str(movingvalue)][1] == 0:
        dict[str(movingvalue)][1] = (len(dict)-1)
    for item in dict.items():
        if item[0] != str(movingvalue):
            if oldpos < dict[str(movingvalue)][1]:
                if oldpos < item[1][1] <= dict[str(movingvalue)][1]:
                    item[1][1] -= 1
            if oldpos > dict[str(movingvalue)][1]:
                if  dict[str(movingvalue)][1] <= item[1][1] < oldpos:
                    item[1][1] += 1       

print(dict["327"])
for item in dict.items():
    if item[1][1] == (dict["327"][1]+1000)%len(dict):
        print("1000th", item)
    if item[1][1] == (dict["327"][1]+2000)%len(dict):
        print("2000th", item)    
    if item[1][1] == (dict["327"][1]+3000)%len(dict):
        print("3000th", item)    
