#parsing the instructiopns first
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from bokeh.plotting import figure, output_file, show
from bokeh.palettes import magma

f = open("./day6/input.txt")
rawinstructions = f.readlines()
cleaninstructions = []

for line in rawinstructions:
    line = line.rstrip()
    if line[:2] == "to":
        command, cood1, grb, cood2 = line.split(" ")
    if line[:2] == "tu":
        word1, word2, cood1, grb, cood2 = line.split(" ")
        command = word1 + word2
    cood1X, cood1Y = cood1.split(",")       
    cood2X, cood2Y = cood2.split(",")    
    cleaninstructions.append({"command": command, "C1X": int(cood1X), "C1Y":int(cood1Y), "C2X":int(cood2X), "C2Y":int(cood2Y)})

mat = np.zeros([1000, 1000], dtype=int)

for instruction in cleaninstructions:
    for i in range(instruction["C1X"], instruction["C2X"]+1):
        for j in range(instruction["C1Y"], instruction["C2Y"]+1):
            match instruction["command"]:
                case "turnoff":
                    mat[i,j] -= 1
                    if mat[i,j] < 0:
                        mat[i,j] = 0
                case "turnon":
                    mat[i,j] += 1
                case "toggle":
                    mat[i,j] += 2 

print(np.count_nonzero(mat))
graph = figure(title = "Christmas lights")
color = magma(256)

brightness = 0
for i in range(0,1000):
    for j in range(0,1000):
            brightness += mat[i][j]



print(brightness)
sns.heatmap(mat)
plt.show()