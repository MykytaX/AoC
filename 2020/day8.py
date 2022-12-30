f = open("input8.txt")
lines = f.readlines()
signals = []
outputs = []
for i in range(0,len(lines)):
    signal, output = lines[i].split("|")
    signal = signal.strip()
    signals.append(signal)
    output = output[1:-1]
    outputs.append(output)


RESULTS = [x for x in range(0,200)]
count = 0
outputs[199] = "cgafbd bcafg fbdga badc"
for k in range(0, len(signals)):
    for word in signals[k].split():
        if len(word) == 3:
            print("BINGO! We've got a seven! IT'S " + word)
            SEVEN = set(list(word))
        if len(word) == 4:
            print("BRINGO! We've got a FOUR! It's " + word)
            FOUR = set(list(word))
        if len(word) == 2:
            print("BAJINGO! We've got a one. It's a " + word)
            ONE = set(list(word))
        else: continue
    Number = ""
    for word in outputs[k].split():
        if len(word) == 2:
            Number = Number + "1"
        elif len(word) == 5 and len(set(list(word)).difference(SEVEN)) == 3 and len(set(list(word)).difference(FOUR)) == 3:
            Number = Number + "2"
        elif len(word) == 5 and len(set(list(word)).difference(SEVEN)) == 2:
            Number = Number + "3"
        elif len(word) == 4:
            Number = Number + "4"
        elif len(word) == 5 and len(set(list(word)).difference(SEVEN)) == 3 and len(set(list(word)).difference(FOUR)) == 2:
            Number = Number + "5"
        elif len(word) == 3:
            Number = Number + "7"
        elif len(word) == 7:
            Number = Number + "8"
        elif len(word) == 6 and len(set(list(word)).difference(ONE)) == 5:
            Number = Number + "6"
        elif len(word) == 6 and len(set(list(word)).difference(FOUR)) == 2:
            Number = Number + "9"
        else:
            Number = Number + "0"
    print("For output #" + str(k) + " The result is " + Number)
    RESULTS[k] = int(Number)
print("And the answer is:")
for i in range (0,200):
    print(str(i) +". " + str(RESULTS[i]))

    print(sum(RESULTS))

            


    
