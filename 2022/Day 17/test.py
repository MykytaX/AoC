arra = [["❤️"] * 100] * 100
print(arra)
file = open("./day17/output.txt", "w", encoding='utf-8')
for i in range(0, len(arra)):
    file.write("".join(arra[i])+"\n")

s = {x + 3 for x in range(0,5)}
print(s)