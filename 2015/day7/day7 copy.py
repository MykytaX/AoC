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
         int(circuit[key])
    except:
        if circuit[key].find("&") != -1:
            key1, key2 = circuit[key].split("&")
            if key1 == "1":
                answer = 1&evaluate(key2)
            else:
                answer = evaluate(key1)&evaluate(key2)
            computedvalues.update({key:answer})
            return answer
        if circuit[key].find("|") != -1:
            key1, key2 = circuit[key].split("|")
            answer = evaluate(key1)|evaluate(key2)
            computedvalues.update({key:answer})
            return answer
        if circuit[key].find("<<") != -1:
            key1, shift = circuit[key].split("<<")
            answer = evaluate(key1)<<int(shift)
            computedvalues.update({key:answer})
            return answer
        if circuit[key].find(">>") != -1:
            key1, shift = circuit[key].split(">>")
            answer = evaluate(key1)>>int(shift)
            computedvalues.update({key:answer})
            return answer
        if circuit[key].find("~") != -1:
            answer = 65535 - evaluate(circuit[key].replace("~",""))
            computedvalues.update({key:answer})
            return answer
        else:
            answer = evaluate(circuit[key])
            computedvalues.update({key:answer})
            return answer
    else:
        answer = int(circuit[key])
        computedvalues.update({key:answer})
        return answer

print(evaluate("a"))



