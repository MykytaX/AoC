class Monkey:
    
    def __init__(self, name, items, operation, test, condition):
        self.name = name
        self.items = items
        self.operation = operation
        self.test = test
        self.condition = condition
        self.inspectiontime = 0
list = [2,3,5,7,11,13,17,19,23]

def oo(number = 2):
    newnumber = int(number) + 3
    return newnumber


def factorizer(item, dictx = {"23": 0, "11":0, "7":0, "3":0, "5":0, "17": 0, "13":0, "19":0, "2":0,"1":0}):
    newdict = dict(dictx)
    item = int(item)
    done = False
    for key in newdict:
        newdict[key] = 0
    while done == False:
        i = 0
        while int(item)%list[i] != 0:
            i += 1
            if i == len(list) or item == 1:
                done = True
                newdict.update({"1": item})
                break
        else:
            if str(list[i]) in newdict:
                newdict[str(list[i])] += 1
        if done == True:
            break
        else:
            item = int(item // list[i])
    return newdict
            
def calculator(item):        
    calculated = 1
    for key, value in item.items():
        if value > 0:
            calculated = calculated*pow(int(key), value)
    calculated = calculated*item["1"]
    return calculated

MonkeyTeam = []
f = open("./DAY10/input10.txt")
group = f.readlines()
group ="".join(group)
MonkeysList = group.split("\n\n")
for monkey in MonkeysList:
    commands = monkey.split("\n")
    items = commands[1][18:].split(", ")
    listofitems = []
    for item in items:
        newitem = int(item)
        listofitems.append(newitem)
    print(listofitems)
    newmonkey = Monkey(commands[0][:-1], listofitems, commands[2][23:], int(commands[3][21:]), (int(commands[4][29:]), int(commands[5][30:])))

    MonkeyTeam.append(newmonkey)


for i in range(0,10000):
    
   
     #   print([calculator(x) for x in monkey.items])     
        
    for monkey in MonkeyTeam:
      
        if len(monkey.items) == 0:
            continue
        for item in monkey.items:
            if monkey.operation == "* old":
                item = item*item
            elif monkey.operation == "* 3":
                item = item*3
            elif monkey.operation == "* 17":
                item = item*17
            elif monkey.operation == "* 19":
                item = item*19

            else:
                item = eval("item"+monkey.operation)
                
            monkey.inspectiontime += 1
            result = False
            
            


            if item%monkey.test == 0:    
                MonkeyTeam[monkey.condition[0]].items.append(item%(19*13*17*3*5*7*11*2))
            else:
                MonkeyTeam[monkey.condition[1]].items.append(item%(19*13*17*3*5*7*11*2))
        monkey.items = []

for monkey in MonkeyTeam:
    print(monkey.name, " : ", monkey.inspectiontime)
