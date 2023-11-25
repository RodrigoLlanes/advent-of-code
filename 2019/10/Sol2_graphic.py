import math
from turtle import *

def drawDots(pos, color="black", size=5):
    for i,j in pos:
        penup()
        pencolor(color)
        goto(j * 30 - (len(asteroidsMap)*15), -i*30 + (len(asteroidsMap[0])*15))
        pendown()
        dot(size)
        penup()

def drawRay(start, end, color="red", size=2):
    goto(start[0] * 30 - (len(asteroidsMap)*15), -start[1]*30 + (len(asteroidsMap[0])*15))
    pendown() 
    goto(j * 30 - (len(asteroidsMap)*15), -i*30 + (len(asteroidsMap[0])*15))
        

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
    
    setup(len(asteroidsMap)*30 + 30, len(asteroidsMap[0])*30 + 30, 0, 0)
    title("Asteroid vaporizer")
    tracer(0)
    hideturtle()
    penup()
    
    positions = []
    for i in range(len(asteroidsMap)):
        for j in range(len(asteroidsMap[i])):
            if(asteroidsMap[i][j] == "#"):
                positions.append([j, i, 0,[]])
    drawDots([[i[0], i[1]] for i in positions])
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
    goto(maximum[0] * 30 - (len(asteroidsMap)*15), -maximum[1]*30 + (len(asteroidsMap[0])*15))
    
    pendown()
    pencolor("green")
    dot(10)
    pencolor("red")
    pensize(2)
    
    #90 -> 0 -> -90 -> ...
    first = [i for i in maximum[3] if (i[0] >= -90)]
    first.sort()
    second = [i for i in maximum[3] if (i[0] < -90)]
    second.sort()
    first += second
    n = 0
    for i in first:
        n += 1
        pendown()
        goto(i[1][0] * 30 - (len(asteroidsMap)*15), -i[1][1]*30 + (len(asteroidsMap[0])*15))
        penup()
        goto(maximum[0] * 30 - (len(asteroidsMap)*15), -maximum[1]*30 + (len(asteroidsMap[0])*15))
        if(n == 200): break
    drawDots([[i[0], i[1]] for i in positions])
    print("sol> " + str(first[199][1][0] * 100 + first[199][1][1]))
    
