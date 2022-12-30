f= open("./day21/test.txt")
monkeys = {}

for line in f.readlines():
    line = line.rstrip()
    monkey, thing = line.split(": ")
    monkeys.update({monkey:thing})

print(monkeys)
newmonkeys = {}

def figure(monkey):
    try:
        ans = int(monkeys[monkey])
        return ans
    except:
        monkey1, opp, monkey2 = monkeys[monkey].split(" ")
        ans = eval("figure(monkey1)"+opp+"figure(monkey2)")
        return ans


            
mynum = 0 
answer = False
bottom = 0
top = 5000000000000
while answer == False:
    answer = figure("root")
    if answer == True:
        break
    else:
        middle = (top + bottom)//2
        monkeys.update({"humn": middle})
        if figure("cgdh") > figure("qhpl"):
            bottom = middle
        else:
            top = middle
    print(figure("cgdh"))
    print(figure("qhpl"))
    print(middle) 
    print(" ") 
  
 