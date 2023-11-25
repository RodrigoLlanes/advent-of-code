f = open("Try.txt", "r")
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
        inputData = str(input(">>"))
        set(i + 1, inputData, aux[0])
        i+=2
    elif (opCode == "04"):
        aux = '{:0>3}'.format(inp[i])
        outputData = get(i + 1, aux[0])
        print("out> " + outputData)
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
