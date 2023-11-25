import math
result = {}
l = []
n = -1

def addNext(c, o):
    if (c in result):
        result[c][1].append(o)
    else:       #    d hijos padres
        result[c] = [0, [o], ""]
        
    if(o in result):
        result[o][2] = c
        inc(o, result[c][0] + 1)
    else:
        result[o] = [result[c][0] + 1, [], c]

def inc(o, k):
    if(o in result):
        result[o][0] += k
        for i in result[o][1]:
            inc(i, k)

def search(s, f, d):
    global n
    global l
    if(s == f):
        if(d < n) or (n < 0):
            n = d
            return
    l.append(s)
    for i in result[s][1]:
        if(not (i in l)):
            search(i, f, d+1)
    if((result[s][2] != "") and (not(result[s][2] in l))):
        search(result[s][2], f, d+1)
        

f = open("Input.txt", "r")
for line in f:
    c = line[0:3]
    o = line[4:7]
    addNext(c, o)
    
search("YOU", "SAN", 0)
print(n)
