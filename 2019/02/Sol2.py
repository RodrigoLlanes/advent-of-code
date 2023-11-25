f = open("Input.txt", "r")
t = f.read()
inputList = list(map(int,t.split(",")))

noun = 0
verb = 0
inp = [0]

while inp[0] != 19690720:
    if noun == 99:
        noun = 0
        verb += 1
    else:
        noun += 1
    inp = list(inputList)
    inp[1] = noun
    inp[2] = verb
    i=0
    while i < len(inp):
        if (inp[i] == 1): inp[inp[i+3]] = inp[inp[i+1]] + inp[inp[i+2]]
        elif (inp[i] == 2): inp[inp[i+3]] = inp[inp[i+1]] * inp[inp[i+2]]
        elif(inp[i] == 99): break
        else: print("error")
        i+=4
print(100 * inp[1] + inp[2])
