f = open("input16.txt")
line = f.readline()

def hexparser(line):
    binaryline = ""
    for char in line:
        if char == "0":
            binaryline = binaryline + "0000"
        elif char == "1":
            binaryline = binaryline + "0001"
        elif char == "2":
            binaryline = binaryline + "0010"
        elif char == "3":
            binaryline = binaryline + "0011"
        elif char == "4":
            binaryline = binaryline + "0100"
        elif char == "5":
            binaryline = binaryline + "0101"
        elif char == "6":
            binaryline = binaryline + "0110"
        elif char == "7":
            binaryline = binaryline + "0111"
        elif char == "8":
            binaryline = binaryline + "1000"
        elif char == "9":
            binaryline = binaryline + "1001"
        elif char == "A":
            binaryline = binaryline + "1010"
        elif char == "B":
            binaryline = binaryline + "1011"
        elif char == "C":
            binaryline = binaryline + "1100"
        elif char == "D":
            binaryline = binaryline + "1101"
        elif char == "E":
            binaryline = binaryline + "1110"
        elif char == "F":
            binaryline = binaryline + "1111"
    return binaryline

class Packet:
    version = int()
    typeid = int()
    literal = bool
    operator = bool
    contents = []
    literalvalue = int()
    lengthtypeid = int()
    totalsublenght = int()
    numberofsubs = int()

example1 = "A0016C880162017C3686B18A3D4780"

def literalvalueparser(line):
#    if len(line) % 5 != 0:
#        raise Exception("Wrong data type for literal value, needs to be divisible by five ", len(line))
    realnumber = ""
    leftovers = ""
    endofstring = False
    while endofstring == False:
        if line[0] == "1":
            endofstring = False
        else:
            endofstring = True
            leftovers = line[5:]
#        print("New chunck!", line[1:5])
        realnumber = realnumber + line[1:5]
        line = line[5:]
#        print(line)
    return int(realnumber, 2), leftovers

versions = []

def parser(line, total=0, number=0):
    while number != 0 or total != 0:
        newpacket = Packet()
        newpacket.version = int(line[:3], 2)
        print(newpacket.version)
        versions.append(newpacket.version)
        newpacket.typeid = int(line[3:6], 2)
        if newpacket.typeid == 4:
            newpacket.literal = True
            newpacket.operator = False
        else:
            newpacket.literal = False
            newpacket.operator = True
        if newpacket.literal == True:
            if total > 0:
                    newpacket.literalvalue, leftovers = literalvalueparser(line[6:])
                    total = total - (len(line)-len(leftovers))
                    line = leftovers
                    if total > 0:
                        continue
                    else:
                        return line
            if number > 0:
                    newpacket.literalvalue, leftovers = literalvalueparser(line[6:])
                    line = leftovers
                    number = number - 1
                    if number > 0:
                        continue
                    else:
                        return line
        if newpacket.operator == True:
            newpacket.lengthtypeid = int(line[6])
            if newpacket.lengthtypeid == 0:
                newpacket.totalsublength = int(line[7:22], 2)
                newpacket.contents = line[22:]
                leftovers = parser(newpacket.contents, newpacket.totalsublength, 0)
                if total > 0:
                    total = total - (len(line)-len(leftovers))
                if number > 0:
                    number = number - 1
                line = leftovers
            else:
                newpacket.numberofsubs = int(line[7:18], 2)
                newpacket.contents = line[18:]
                leftovers = parser(newpacket.contents, 0, newpacket.numberofsubs)
                if total > 0:
                    total = total - (len(line)-len(leftovers))
                if number > 0:
                    number = number - 1
                line = leftovers
        return line

parser(hexparser(line),0,1)
print(line)
print(sum(versions))
