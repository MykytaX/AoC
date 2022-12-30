f = open("./DAY16/input16.txt")
lines = f.readlines()

class valve:
    def __init__(self, valvename, flowrate, destinations):
        self.valvename = valvename
        self.flowrate = flowrate
        self.destinations = destinations
        self.priorities = []
        self.output = {"1":{}, "2":{}, "3":{}, "4":{}, "5":{}, "6":{}, "7":{}, "8":{},
         "9":{}, "10":{}, "11":{}, "12":{}, "13":{}, "14":{}, "15":{}, "16":{},
         "17": {}, "18": {}, "19": {}, "20": {}, "21": {}, "22": {}, "23": {}, 
         "24": {}, "25": {}, "26": {}, "27": {}, "28": {}, "29": {}, "30": {}}
        
valves = {}

for line in lines:
    line = line.rstrip()
    if line[:8] == "Valve TZ":
        rest, destinations = line.split("to valve ")
    else:
        rest, destinations = line.split("to valves ")
    _, valvename, _, _, flowrate, _, _= rest.split()
    flowrate = int(flowrate[5:-1])
    destinations = set(destinations.split(", "))
    newvalve = valve(valvename, flowrate, destinations)
    valves.update({valvename: newvalve})

for eachvalve in valves.values():
    print(eachvalve.valvename)
    print("flow rate is ", eachvalve.flowrate)
    print("conects to ", eachvalve.destinations )


def breathsearch(minute, currentnode, visited):
    output = valves[currentnode .valvename].flowrate*(30-minute)
    currentnode.output.append({currentnode.valvename:output})
    visited.append(currentnode.valvename)
    minute = minute - 1
    while minute >= 2:
        for destination in currentnode.destinations:
            if destination not in visited:
                breathsearch(minute, destination, visited)

           

for minute in range(1,31):
    if minute == 1:
        for eachvalve in valves:
            eachvalve.priorities.append(eachvalve.valvename)
    if minute == 2:

