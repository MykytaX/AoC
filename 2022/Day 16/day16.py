import os

print(os.getcwd())

f = open(os.getcwd() +r"\2022\inputs\day16.txt")
lines = f.readlines()

def max_pressure(valves, time_left, current_valve, memo):
    if time_left <= 0:
        return 0
    if (time_left,current_valve) in memo:
        return memo[(time_left,current_valve)]
    max_pressure_released = 0
    # open the current valve
    max_pressure_released = valves[current_valve]['flow_rate'] * (time_left - 1)
    # move to another valve and open it
    for next_valve in valves[current_valve]['tunnels']:
        pressure = max_pressure(valves, time_left - 2, next_valve,memo)
        if pressure > max_pressure_released:
            max_pressure_released = pressure
    memo[(time_left,current_valve)] = max_pressure_released
    return max_pressure_released



memo = {}
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
    valves.update({valvename: {'flow_rate': flowrate, 'tunnels': destinations}})

print(valves)
print(max_pressure(valves,30,'AA',memo))
print(memo)