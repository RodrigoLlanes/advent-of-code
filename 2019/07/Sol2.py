import itertools
  
def execute(p, num, c):
    #print("sec: " + str(num))
    #print("inp: " + str(p[num][2]))
    nextInput = None
    if(c[num] != -1):
        y = list(c)
        codeIns = c[num]
        y[num] = -1
        c = tuple(y)
    else:
        codeIns = None
    i = p[num][0]
    inp = p[num][1]
    inpList = p[num][2]
    a=0
    b=0
    if(num == 4):
        outList = p[0][2]
    else:
        outList = p[num + 1][2]
    while True:
        if (len(str(inp[i])) == 1):
            if (inp[i] == "1"):
                inp[int(inp[i+3])] = str(int(inp[int(inp[i+1])]) + int(inp[int(inp[i+2])]))
                i+=4
            elif (inp[i] == "2"):
                inp[int(inp[i+3])] = str(int(inp[int(inp[i+1])]) * int(inp[int(inp[i+2])]))
                i+=4
            elif (inp[i] == "3"):
                #print(inpList)
                if(codeIns != None):
                    inp[int(inp[i+1])] = str(codeIns)
                    codeIns = None
                elif(len(inpList) > 0):
                    inp[int(inp[i+1])] = str(inpList.pop(0))
                    nextInput = None
                else:
#                    inp[int(inp[i+1])] = str(input(">>"))
                    break
                i+=2
            elif (inp[i] == "4"):
                #print("out> " + str(inp[int(inp[i+1])]))
                nextInput = inp[int(inp[i+1])]
                outList.append(inp[int(inp[i+1])])
                i+=2
            elif (inp[i] == "5"):
                if(int(inp[int(inp[i+1])]) != 0): i = int(inp[i+2])
                else: i+=3
            elif (inp[i] == "6"):
                if(int(inp[int(inp[i+1])]) == 0): i = int(inp[i+2])
                else: i+=3
            elif (inp[i] == "7"):
                if(int(inp[int(inp[i+1])]) < int(inp[int(inp[i+2])])): inp[int(inp[i+3])] = 1
                else: inp[int(inp[i+3])] = 0
                i+=4
            elif (inp[i] == "8"):
                if(int(inp[int(inp[i+1])]) == int(inp[int(inp[i+2])])): inp[int(inp[i+3])] = 1
                else: inp[int(inp[i+3])] = 0
                i+=4
            else: print("error " + inp[i])
        else:
            if (inp[i][len(inp[i])-2: len(inp[i])] == "01"):
                aux = '{:0>5}'.format(inp[i])
                if(aux[2] == "0"): a = inp[int(inp[i+1])]
                else: a = inp[i+1]
                if(aux[1] == "0"): b = inp[int(inp[i+2])]
                else: b = inp[i+2]
                if(aux[0] == "0"): inp[int(inp[i+3])] = str(int(a) + int(b))
                else: inp[i+3] = str(int(a) + int(b))
                i+=4
            elif (inp[i][len(inp[i])-2: len(inp[i])] == "02"):
                aux = '{:0>5}'.format(inp[i])
                if(aux[2] == "0"): a = inp[int(inp[i+1])]
                else: a = inp[i+1]
                if(aux[1] == "0"): b = inp[int(inp[i+2])]
                else: b = inp[i+2]
                if(aux[0] == "0"): inp[int(inp[i+3])] = str(int(a) * int(b))
                else: inp[i+3] = str(int(a) * int(b))
                i+=4
            elif (inp[i][len(str(inp[i]))-2: len(inp[i])] == "03"):
                if(codeIns != None):
                    inp[i+1] = codeIns
                    codeIns = None
                elif(len(inpList) > 0):
                    inp[i+1] = str(inpList.pop(0))
                    nextInput = None
                else:
#                    inp[i+1] = str(input(">>"))
                    break
                    i+=2
            elif (inp[i][len(str(inp[i]))-2: len(inp[i])] == "04"):
                #print("out> " + inp[i+1])
                outList.append(inp[i+1])
                nextInput = inp[i+1]
                i+=2
            elif (inp[i][len(inp[i])-2: len(inp[i])] == "05"):
                aux = '{:0>4}'.format(inp[i])
                if(aux[1] == "0"): a = inp[int(inp[i+1])]
                else: a = int(inp[i+1])
                if(aux[0] == "0"):
                    if(int(a) != 0): i = int(inp[int(inp[i+2])])
                    else: i = i+3
                else:
                    if(int(a) != 0): i = int(inp[i+2])
                    else: i = i+3
            elif (inp[i][len(inp[i])-2: len(inp[i])] == "06"):
                aux = '{:0>4}'.format(inp[i])
                if(aux[1] == "0"): a = inp[int(inp[i+1])]
                else: a = inp[i+1]
                if(aux[0] == "0"):
                    if(int(a) == 0): i = int(inp[int(inp[i+2])])
                    else: i = i+3
                else:
                    if(int(a) == 0): i = int(inp[i+2])
                    else: i = i+3
            elif (inp[i][len(inp[i])-2: len(inp[i])] == "07"):
                aux = '{:0>5}'.format(inp[i])
                if(aux[2] == "0"): a = inp[int(inp[i+1])]
                else: a = inp[i+1]
                if(aux[1] == "0"): b = inp[int(inp[i+2])]
                else: b = inp[i+2]
                if(aux[0] == "0"):
                    if(int(a) < int(b)): inp[int(inp[i+3])] = 1
                    else: inp[int(inp[i+3])] = 0
                else:
                    if(int(a) < int(b)): inp[i+3] = 1
                    else: inp[i+3] = 0
                i += 4
            elif (inp[i][len(inp[i])-2: len(inp[i])] == "08"):
                aux = '{:0>5}'.format(inp[i])
                if(aux[2] == "0"): a = inp[int(inp[i+1])]
                else: a = inp[i+1]
                if(aux[1] == "0"): b = inp[int(inp[i+2])]
                else: b = inp[i+2]
                if(aux[0] == "0"):
                    if(int(a) == int(b)): inp[int(inp[i+3])] = 1
                    else: inp[int(inp[i+3])] = 0
                else:
                    if(int(a) == int(b)): inp[i+3] = 1
                    else: inp[i+3] = 0
                i += 4
            elif(inp[i] == "99"):
                if(num == 4):
                    #print(str(num) + " ended")
                    return nextInput
                else:
                    #print(str(num) + " ended")
                    break
            else:
                print("error line:" + str(i) + " \n    -instruction:" + inp[i-4] + " " + inp[i-3] + " " + inp[i-2] + inp[i-1] + inp[i+1])
                return None
    
    p[num][0] = i
    p[num][1] = inp
    p[num][2] = inpList
    if(num == 4):
        p[0][2] = outList
        return execute(p, 0, c)
    else:
        p[num + 1][2] = outList
        return execute(p, num + 1, c)
        


#Main
f = open("Input.txt", "r")
t = f.read()
inputList = list(map(str,t.split(",")))
j= 0
res = 0
c = [5,6,7,8,9]
for code in itertools.permutations(c, 5):
    #print("code: " + str(code))
    programList = [[0,list(inputList),[0]],[0,list(inputList),[]],[0,list(inputList),[]],[0,list(inputList),[]],[0,list(inputList),[]]]
    z = execute(programList, 0, code)
    #print("pRes- " + str(z))
    if(z == None):
        print("error")
        break
    if(int(z) > res):
        res = int(z)
print("res> " + str(res))
