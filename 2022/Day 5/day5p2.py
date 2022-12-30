#    [P]                 [Q]     [T]
#[F] [N]             [P] [L]     [M]
#[H] [T] [H]         [M] [H]     [Z]
#[M] [C] [P]     [Q] [R] [C]     [J]
#[T] [J] [M] [F] [L] [G] [R]     [Q]
#[V] [G] [D] [V] [G] [D] [N] [W] [L]
#[L] [Q] [S] [B] [H] [B] [M] [L] [D]
#[D] [H] [R] [L] [N] [W] [G] [C] [R]
# 1   2   3   4   5   6   7   8   9 

stack1=list("DLVTMHF")
stack2=list("HQGJCTNP")
stack3=list("RSDMPH")
stack4=list("LBVF")
stack5=list("NHGLQ")
stack6=list("WBDGRMP")
stack7=list("GMNRCHLQ")
stack8=list("CLW")
stack9=list("RDLQJZMT")
message = " "
factory = [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

f = open("day5/instructions.txt")
instructions = f.readlines()

for instruction in instructions:
    instruction = instruction.rstrip()
    print(instruction)
    grb, number, grb2, departure, grb3, destination = instruction.split(" ")
    i = 0
    number = int(number)
    destination = int(destination)
    departure = int(departure)
    factory[destination-1] =  factory[destination-1] + factory[departure-1][-number:]
    while number > 0:
        factory[departure-1].pop()
        number = number -1

for stack in factory:
    message = message + stack[-1]

print(message)