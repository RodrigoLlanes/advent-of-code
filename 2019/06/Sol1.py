import math
result = {}

def addNext(c, o):
    if (c in result):
        result[c][1].append(o)
    else:
        result[c] = [0, [o]]
        
    if(o in result):
        inc(o, result[c][0] + 1)
    else:
        result[o] = [result[c][0] + 1, []]

def inc(o, k):
    if(o in result):
        result[o][0] += k
        for i in result[o][1]:
            inc(i, k)

f = open("Input.txt", "r")
for line in f:
    c = line[0:3]
    o = line[4:7]
    addNext(c, o)
n = 0
for k in result:
    n += result[k][0]
print(n)
