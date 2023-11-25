f = open("Input.txt", "r")
t = f.read()
inputList = list(map(int,t.split(",")))

inp = list(inputList)
inp[1] = 12
inp[2] = 2
i=0

while i < len(inp):
    if (inp[i] == 1): inp[inp[i+3]] = inp[inp[i+1]] + inp[inp[i+2]]
    elif (inp[i] == 2): inp[inp[i+3]] = inp[inp[i+1]] * inp[inp[i+2]]
    elif(inp[i] == 99): break
    else: print("error")
    i+=4
print(inp[0])
