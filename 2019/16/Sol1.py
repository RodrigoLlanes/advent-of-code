f = open("Input.txt", "r")
t = f.read()
t = t.rstrip()

inp = []

for i in t:
    inp.append(int(i))

l = len(t)
originalPattern=[1,0,-1,0]
for i in range(100):
    pattern=[1,0,-1,0]
    for j in range(l):
        aux = 0
        if(j != 0):
            for k in range(4):
                if(k == 0):
                    pattern.insert(k*j + k*j + j, originalPattern[k])
                else:
                    pattern.insert(k*j + k*j, originalPattern[k])
            pattern.insert(0, 0)
        #print(pattern)
        index = -1
        for k in range(len(inp)):
            if not(index < len(pattern)-1):
                index = j
            else:
                index += 1
            aux += inp[k] * pattern[index]
        inp[j] = int(str(aux)[-1])

res = ""
for i in range(8):
    res += str(inp[i])
print(res)
