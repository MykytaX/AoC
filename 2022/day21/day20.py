f= open("./day21/test.txt")
monkeys = {}

for line in f.readlines():
    line = line.rstrip()
    monkey, thing = line.split(": ")
    monkeys.update({monkey:thing})

print(monkeys)

def figure(monkey):
    try:
        ans = int(monkeys[monkey])
        return ans
    except:
        monkey1, opp, monkey2 = monkeys[monkey].split(" ")
        ans = eval("figure(monkey1)"+opp+"figure(monkey2)")
        return ans

print(figure("qhpl"))