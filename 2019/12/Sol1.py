from math import *

f = open("Input.txt", "r")

moons = []
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
    
for t in range(4686774924):
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
        
e = 0
for i in moons:
    e += (abs(i[0][0]) + abs(i[0][1]) + abs(i[0][2])) * (abs(i[1][0]) + abs(i[1][1]) + abs(i[1][2]))
print(e)
