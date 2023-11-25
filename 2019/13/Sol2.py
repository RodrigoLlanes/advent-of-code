f = open("Input2.txt", "r")
t = f.read()
inputList = list(map(str,t.split(",")))

inp = list(inputList)
rb = 0
screen=[]

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

def show():
    global screen
    for i in screen:
        for j in i:
            if(j == "0"): print(" ", end="")
            elif(j == "1"): print("/", end="")
            elif(j == "2"): print("X", end="")
            elif(j == "3"): print("-", end="")
            elif(j == "4"): print("O", end="")
        print("")
i=0
cont=0
tiles=[]
yP=[]
bP=[]
score=0
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
        #inputData = str(input(">>"))
        if(bP[0] - yP[0] < 0):
            inputData = "-1"
        elif(bP[0] - yP[0] > 0):
            inputData = "1"
        else:
            inputData = "0"
        set(i + 1, inputData, aux[0])
        i+=2
    elif (opCode == "04"):
        aux = '{:0>3}'.format(inp[i])
        outputData = get(i + 1, aux[0])
        #print("out> " + outputData)
        if(len(tiles) <= 1):
            tiles.append(int(outputData))
        elif(len(tiles) == 2):
            if(tiles[0] == -1) and (tiles[1] == 0):
                score = outputData
            if(tiles[1] >= len(screen)):
                if(len(screen) != 0):
                    screen += [["0" for j in range(len(screen[0]))] for k in range((tiles[1] + 1) - len(screen))]
                else:
                    screen += [["0" for j in range(tiles[0])] for k in range((tiles[1] + 1) - len(screen))]
            if(len(screen) != 0):
                if(tiles[0] >= len(screen[0])):
                    for j in screen:
                        j += ["0" for j in range((tiles[0] + 1) - len(screen[0]))]
            if(outputData == "4"): bP = [tiles[0],tiles[1]]
            elif(outputData == "3"): yP = [tiles[0],tiles[1]]
            screen[tiles[1]][tiles[0]] = outputData
            tiles = []
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
        for i in screen:
            for j in i:
                if(j == "2"): cont+=1
        print("score> " + str(score))
        break
    else:
        print("error> " + inp[i])
        print(opCode)

