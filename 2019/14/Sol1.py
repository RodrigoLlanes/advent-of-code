import math
from collections import defaultdict

#recordar todo esta en str
f = open("Input.txt", "r")
reactions = {}
ore = 0
ch = {}
for line in f:
    l = line.rstrip('\n').split(", ")
    r = l[-1].split(" => ")[1]
    l = l[0:len(l)-1] + [l[-1].split(" => ")[0]]
    reactions[r.split(" ")[1]] = [r.split(" ")[0]]
    for i in l:
        reactions[r.split(" ")[1]].append([i.split(" ")[0], i.split(" ")[1]])

def searchOreForFuel(product="FUEL", n=1):
    global reactions
    global ore
    global ch
    c=0
    if(ch.get(product, 0) > 0):
        if(ch[product] <= n):
            c += ch[product]
            ch[product]=0
        else:
            c += n
            ch[product] -= n

    while c < n:
        c+= int(reactions[product][0])
        for i in range(1, len(reactions[product])):
            if(reactions[product][i][1] == "ORE"):
                ore += int(reactions[product][i][0])
            else:
                searchOreForFuel(reactions[product][i][1], int(reactions[product][i][0]))
    if(c > n):
        ch[product] = ch.get(product, 0) + (c - n)
searchOreForFuel()
print(ore)
#22915914
