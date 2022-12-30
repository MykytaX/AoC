f= open("./day7/input.txt")
wholelist = f.readlines()

circuit={}
chartoreplace = {" AND ": "&", " OR ": "|", " LSHIFT ": "<<", " RSHIFT ": ">>", "NOT ": "~"}
for instruction in wholelist:
    instruction = instruction.rstrip()
    value, key = instruction.split(" -> ")
    for wordbit, symbolbit in chartoreplace.items():
        value = value.replace(wordbit, symbolbit)
    circuit.update({key: value})
    
print(circuit)
computedvalues = {}

def evaluate(key):
    if key in computedvalues:
        return computedvalues[key]

    answer = 0
    try:
         bin(int(circuit[key]))
    except:
        if circuit[key].find("&") != -1:
            key1, key2 = circuit[key].split("&")
            if key1 == "1":
                answer = int(bin(1&evaluate(key2))[2:], 2)
            else:
                answer = int(bin(evaluate(key1)&evaluate(key2))[2:], 2)
            computedvalues.update({key:answer})
            return answer
        if circuit[key].find("|") != -1:
            key1, key2 = circuit[key].split("|")
            answer = int(bin(evaluate(key1)|evaluate(key2))[2:], 2)
            computedvalues.update({key:answer})
            return answer
        if circuit[key].find("<<") != -1:
            key1, shift = circuit[key].split("<<")
            answer = int(bin(evaluate(key1)<<int(shift))[2:], 2)
            computedvalues.update({key:answer})
            return answer
        if circuit[key].find(">>") != -1:
            key1, shift = circuit[key].split(">>")
            answer = int(bin(evaluate(key1)>>int(shift))[2:], 2)
            computedvalues.update({key:answer})
            return answer
        if circuit[key].find("~") != -1:
            answer = int(bin(~evaluate(circuit[key].replace("~","")))[3:], 2)
            computedvalues.update({key:answer})
            return answer
        else:
            answer = evaluate(circuit[key])
            computedvalues.update({key:answer})
            return answer
    else:
        answer = int(bin(int(circuit[key]))[2:], 2)
        computedvalues.update({key:answer})
        return answer

print(evaluate("d"))
print(evaluate("x"))
print(evaluate("y"))
print(evaluate("h"))
print(evaluate("i"))
print(evaluate("f"))
print(evaluate("g"))


