f = open("Input.txt", "r")
t = f.read()
inputList = list(map(str,t.split(",")))

inp = list(inputList)
rb = 0

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

n = 1
i=0
check=[False, False]
colors = [[0,0, 1]]
pos = [0,0]
rot = 0
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
        positions = [[i[0], i[1]] for i in colors]
        if(pos in positions):
            inputData = colors[positions.index(pos)][2]
        else:
            n+=1
            colors.append([pos[0], pos[1], 0])
            inputData = 0
        set(i + 1, str(inputData), aux[0])
        i+=2
    elif (opCode == "04"):
        aux = '{:0>3}'.format(inp[i])
        outputData = get(i + 1, aux[0])
        #print("out> " + outputData)
        positions = [[i[0], i[1]] for i in colors]
        if(not check[0]):
            if not(pos in positions):
                print("error> " + str(positions) + " - " + str(pos))
            colors[positions.index(pos)][2] = outputData
            check[0] = True
        elif(not check[1]):
            if(outputData == "1"):
                if(rot == 3):rot = 0
                else: rot += 1
            elif(outputData == "0"):
                if(rot == 0): rot = 3
                else: rot -= 1
            if (rot == 0): pos[1] += 1
            elif (rot == 1): pos[0] += 1
            elif (rot == 2): pos[1] -= 1
            elif (rot == 3): pos[0] -= 1
            else:
                print("error")
                break
            check = [False, False]
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
        print("sol> " + str(n))
        break
    else:
        print("error> " + inp[i])
        print(opCode)
