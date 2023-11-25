from math import *
import copy

f = open("Input.txt", "r")

moons = []
history=[]
for line in f:
    aux=[]
    inputList = list(map(str,line.rstrip('\n').split(",")))
    for j in range(3):
        if(j == 0):
            aux.append(int(inputList[j][3: len(inputList[j])]))
        elif(j == 1):
            aux.append(int(inputList[j][3: len(inputList[j])]))
        elif(j == 2):
            aux.append(int(inputList[j][3: len(inputList[j]) - 1]))
    moons.append([aux,[0,0,0]])

historyX=[]
historyY=[]
historyZ=[]
auxX = copy.deepcopy([[i[0][0], i[1][0]] for i in moons])
historyX.append(auxX)
auxY = copy.deepcopy([[i[0][1], i[1][1]] for i in moons])
historyY.append(auxY)
auxZ = copy.deepcopy([[i[0][2], i[1][2]] for i in moons])
historyZ.append(auxZ)

t = 0
tx=0
ty=0
tz=0
while True:
    t += 1
    for i in moons:
        for j in moons:
            for k in range(3):
                if(i[0][k] < j[0][k]):
                    i[1][k] += 1
                elif(i[0][k] > j[0][k]):
                    i[1][k] -= 1
    for i in moons:
        for j in range(3):
            i[0][j] += i[1][j]
    auxX = copy.deepcopy([[i[0][0], i[1][0]] for i in moons])
    auxY = copy.deepcopy([[i[0][1], i[1][1]] for i in moons])
    auxZ = copy.deepcopy([[i[0][2], i[1][2]] for i in moons])
    if(auxX in historyX):
        if(tx == 0):
            tx=t
    if(auxY in historyY):
        if(ty == 0):
            ty=t
    if(auxZ in historyZ):
        if(tz == 0):
            tz=t
    if(tx!=0) and(ty!=0)and(tz!=0):
        break

A = max(tx, ty)
B = min(tx, ty)

while B:
    mcd = B
    B = A % B
    A = mcd
mcm =  (tx * ty) // mcd

A = max(mcm, tz)
B = min(mcm, tz)

while B:
    mcd = B
    B = A % B
    A = mcd
mcm =  (mcm * tz) // mcd

print(mcm)

        
        
