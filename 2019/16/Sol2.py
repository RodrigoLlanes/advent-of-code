from math import *

f = open("Input.txt", "r")
t = f.read()
t = t.rstrip()

inp = []

for i in t:
    inp.append(int(i))

inp = inp * 10000

offset = ""
for i in range(7):
    offset += str(inp[i])
offset = int(offset)
l = len(inp)

for i in range(100):
    print(i)
    p=inp[len(inp)-1]

    for j in range(len(inp) - 2, offset-1, -1):
        p += inp[j]
        inp[j] = int(str(p)[-1])
        
res = ""
for i in range(8):
    res += str(inp[offset + i])
print(res)
