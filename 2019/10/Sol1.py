import math

def angle(x1, y1, x2, y2):
    x = x2 - x1
    y = y2 - y1
    return math.atan2(y, x) * (180.0 / math.pi)

with open("Input.txt") as fileobj:
    asteroidsMap = []
    for line in fileobj:
        aux = []
        for char in line:
            if(char == "\n"): continue
            aux.append(char)
        asteroidsMap.append(aux)
    print(asteroidsMap)
    positions = []
    for i in range(len(asteroidsMap)):
        for j in range(len(asteroidsMap[i])):
            if(asteroidsMap[i][j] == "#"):
                positions.append([j, i, 0])
    print(positions)
    for i in positions:
        aux = []
        for j in positions:
            if i == j: continue
            else:
                a = angle(i[0], i[1], j[0], j[1])
                if not(a in aux):
                    aux.append(a)
        i[2] = len(aux)
    maximum = -1
    for i in positions:
        if(i[2] > maximum):
            maximum = i[2]
    print(maximum)
