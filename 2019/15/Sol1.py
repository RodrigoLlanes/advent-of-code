from collections import defaultdict

f = open("Input.txt", "r")
t = f.read()
inputList = list(map(str,t.split(",")))

inp = list(inputList)
rb = 0

robotMap = defaultdict(lambda: ' ')
lastPos = [0,0]
localPos = [0,0]
direction = 1
rChanged=False
history = defaultdict(lambda: 0)
t=0

def checkMemory(n, m):
    global inp
    global rb
    if(m == "1"):
        if(n >= len(inp)):
            inp += ["0" for j in range((n + 1) - len(inp))]
        return(n)
    elif(m == "0"):
        checkMemory(n, "1")
        return checkMemory(int(inp[n]), "1")
    elif(m == "2"):
        checkMemory(n, "1")
        return checkMemory(rb + int(inp[n]), "1")
    else:
        print("error> Invalid memory acces code (" + str(m) + ")")

def set(n, v, m):
    global inp
    index = checkMemory(n, m)
    inp[index] = v

def get(n, m):
    global inp
    index = checkMemory(n, m)
    return inp[index]

def setDirection():
    global direction
    global robotMap
    global localPos
    global lastPos
    if robotMap[(localPos[0], localPos[1]+1)] == " " and [localPos[0], localPos[1]+1] != lastPos:
        direction = 1
    elif robotMap[(localPos[0]+1, localPos[1])] == " " and [localPos[0]+1, localPos[1]] != lastPos:
        direction = 4
    elif robotMap[(localPos[0], localPos[1]-1)] == " " and [localPos[0], localPos[1]-1] != lastPos:
        direction = 2
    elif robotMap[(localPos[0]-1, localPos[1])] == " " and [localPos[0]-1, localPos[1]] != lastPos:
        direction = 3
    else:
        time = -1
        if robotMap[(localPos[0], localPos[1]+1)] != "#":
            if(time == -1) or time > history[(localPos[0], localPos[1]+1)]:
                direction = 1
                time = history[(localPos[0], localPos[1]+1)]
        if robotMap[(localPos[0]+1, localPos[1])] != "#":
            if(time == -1) or time > history[(localPos[0]+1, localPos[1])]:
                direction = 4
                time = history[(localPos[0]+1, localPos[1])]
        if robotMap[(localPos[0], localPos[1]-1)] != "#":
            if(time == -1) or time > history[(localPos[0], localPos[1]-1)]:
                direction = 2
                time = history[(localPos[0], localPos[1]-1)]
        if robotMap[(localPos[0]-1, localPos[1])] != "#":
            if(time == -1) or time > history[(localPos[0]-1, localPos[1])]:
                direction = 3

def changeDirection():
    if(not rChanged): direction = 1
    else: direction = 1
        
        
def setMap(o):
    if(o == "0"): s = "#"
    elif(o == "1"): s = "."
    elif(o == "2"): s = "O"
    else: print("ERROR")
    
    if direction == 1:
        robotMap[(localPos[0], localPos[1]+1)]= s
    elif direction ==  4:
        robotMap[(localPos[0]+1, localPos[1])] = s
    elif direction ==  2:
        robotMap[(localPos[0], localPos[1]-1)] = s
    elif direction ==  3:
        robotMap[(localPos[0]-1, localPos[1])] = s
    else:
        print("ERROR")

def move():
    global localPos
    global direction
    global lastPos
    global t
    global history
    history[(localPos[0], localPos[1])] = t
    lastPos = localPos.copy()
    if direction == 1:
        localPos[1] += 1
    elif direction ==  4:
        localPos[0] += 1
    elif direction ==  2:
        localPos[1] -= 1
    elif direction ==  3:
        localPos[0] -= 1
    else:
        print("ERROR")

def draw():
    global robotMap
    global localPos
    minX = 0
    maxX = 0
    minY = 0
    maxY = 0
    print("------------MAP------------")
    print()
    for i in robotMap.keys():
        p = i
        if(robotMap[i] == " "): continue
        if(int(p[0]) > maxX): maxX = p[0]
        if(int(p[0]) < minX): minX = p[0]
        if(int(p[1]) > maxY): maxY = p[1]
        if(int(p[1]) < minY): minY = p[1]
    print(maxY)
    for i in range(maxY + 1, minY - 1, -1):
        s = ""
        for j in range(minX, maxX + 1):
            if(i == 0) and (j == 0): s += "X"
            else: s += robotMap[(j, i)]
        print(s)
    print()

def findPath(start=[0,0], prev=[0,0], steps=-1):
    global robotMap
    if robotMap[(start[0],start[1])] == "#":
        return -1
    elif robotMap[(start[0],start[1])] == "O":
        return steps+1
    else:
        s1=-1
        s2=-1
        s3=-1
        s4=-1
        if([start[0], start[1]+1] != prev):
            s1 = findPath([start[0], start[1]+1], start, steps+1)
        if([start[0], start[1]-1] != prev):
            s2 = findPath([start[0], start[1]-1], start, steps+1)
        if([start[0]+1, start[1]] != prev):
            s3 = findPath([start[0]+1, start[1]], start, steps+1)
        if([start[0]-1, start[1]] != prev):
            s4 = findPath([start[0]-1, start[1]], start, steps+1)
        r = -1
        if(s1 != -1):
            if(r == -1) or (s1 < r):
                r = s1
        if(s2 != -1):
            if(r == -1) or (s2 < r):
                r = s2
        if(s3 != -1):
            if(r == -1) or (s3 < r):
                r = s3
        if(s4 != -1):
            if(r == -1) or (s4 < r):
                r = s4
        return r
i=0
while True:
    opCode = '{:0>2}'.format(inp[i])
    opCode = opCode[len(opCode) - 2:len(opCode)]
    if (opCode == "01"):
        aux = '{:0>5}'.format(inp[i])
        a = get(i + 1, aux[2])
        b = get(i + 2, aux[1])
        set(i + 3, str(int(a) + int(b)), aux[0])
        i+=4
    elif (opCode == "02"):
        aux = '{:0>5}'.format(inp[i])
        a = get(i + 1, aux[2])
        b = get(i + 2, aux[1])
        set(i + 3, str(int(a) * int(b)), aux[0])
        i+=4
    elif (opCode == "03"):
        aux = '{:0>3}'.format(inp[i])
        #if(localPos[0] %10000) == 0: draw()
        #inputData = str(input(">>"))
        if(t > 10000):break
        setDirection()
        #print(str(direction) + " " + str(localPos))
        inputData = str(direction)
        set(i + 1, inputData, aux[0])
        i+=2
    elif (opCode == "04"):
        aux = '{:0>3}'.format(inp[i])
        t+=1
        outputData = get(i + 1, aux[0])
        #print("out> " + outputData + " " + str(localPos))
        setMap(outputData)
        #print(outputData)
        if(outputData != "0"):
            move()
        if(outputData == "2"):
            print(localPos)
            #draw()
            #break
        i+=2
    elif (opCode == "05"):
        aux = '{:0>4}'.format(inp[i])
        a = get(i + 1, aux[1])
        addres = get(i + 2, aux[0])
        if(a != "0"): i = int(addres)
        else: i = i+3
    elif (opCode == "06"):
        aux = '{:0>4}'.format(inp[i])
        a = get(i + 1, aux[1])
        addres = get(i + 2, aux[0])
        if(a == "0"): i = int(addres)
        else: i = i+3
    elif (opCode == "07"):
        aux = '{:0>5}'.format(inp[i])
        a = get(i + 1, aux[2])
        b = get(i + 2, aux[1])
        if(int(a) < int(b)): set(i + 3, "1", aux[0])
        else: set(i + 3, "0", aux[0])
        i += 4
    elif (opCode == "08"):
        aux = '{:0>5}'.format(inp[i])
        a = get(i + 1, aux[2])
        b = get(i + 2, aux[1])
        if(int(a) == int(b)): set(i + 3, "1", aux[0])
        else: set(i + 3, "0", aux[0])
        i += 4
    elif (opCode == "09"):
        aux = '{:0>3}'.format(inp[i])
        rb += int(get(i + 1, aux[0]))
        i+=2
    elif(opCode == "99"):
        print("fin")
        break
    else:
        print("error> " + inp[i])
        print(opCode)
draw()
print(findPath())
