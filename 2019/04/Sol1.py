c=0
for i in range(387638,919123 + 1):
    l = -1
    r = False
    d = True
    for j in str(i):
        if(int(j) == l):
            r = True
        if(int(j) < l):
            d = False
        l = int(j)
    if(r and d):
        c+=1
print(c)
