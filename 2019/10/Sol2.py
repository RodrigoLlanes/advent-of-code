import math
from turtle import *

def angle(x1, y1, x2, y2):
    x = x2 - x1
    y = y2 - y1
    return math.atan2(y, x) * (180.0 / math.pi)

def distance(xi,xii,yi,yii):
    sq1 = (xi-xii)*(xi-xii)
    sq2 = (yi-yii)*(yi-yii)
    return math.sqrt(sq1 + sq2)

with open("Input.txt") as fileobj:
    asteroidsMap = []
    for line in fileobj:
        aux = []
        for char in line:
            if(char == "\n"): continue
            aux.append(char)
        asteroidsMap.append(aux)
    
    positions = []
    for i in range(len(asteroidsMap)):
        for j in range(len(asteroidsMap[i])):
            if(asteroidsMap[i][j] == "#"):
                positions.append([j, i, 0,[]])
    for i in positions:
        aux = []
        for j in positions:
            if i == j: continue
            else:
                a = angle(i[0], i[1], j[0], j[1])
                if not(a in [k[0] for k in aux]):
                    aux.append([a, [j[0], j[1]]])
                else:
                    index = ([k[0] for k in aux]).index(a)
                    di = distance(i[0], i[1], aux[index][1][0], aux[index][1][1])
                    dn = distance(i[0], i[1], j[0], j[1])
                    if(dn < di):
                        aux[index] = [a, [j[0], j[1]]]
        i[3] = aux
        i[2] = len(aux)
    maximum = [0,0,-1,[]]
    for i in positions:
        if(i[2] > maximum[2]):
            maximum = i
            
    #-90 -> 0 -> 90 -> ...
    first = [i for i in maximum[3] if (i[0] >= -90)]
    first.sort()
    second = [i for i in maximum[3] if (i[0] < -90)]
    second.sort()
    first += second
    n = 0
    for i in first:
        n += 1
        if(n == 200): break
    print("sol> " + str(first[199][1][0] * 100 + first[199][1][1]))
    
