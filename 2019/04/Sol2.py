c=0
for i in range(387638,919123 + 1):
    r = False
    d = True
    for j in range (0, len(str(i)) - 1):
        if(str(i)[j] == str(i)[j+1]):
            aux = False
            if(j < len(str(i)) - 2):
                if(str(i)[j+2] != str(i)[j+1]):
                    aux = True
                else:
                    aux = False
            else:
                aux = True
            if(j > 0):
                if(str(i)[j] != str(i)[j-1]):
                    aux = aux and True
                else:
                    aux =  False
            else:
                aux = aux and True
            r = r or aux
        elif(int(str(i)[j]) > int(str(i)[j+1])):
            d = False
            break
    if(r and d):
        c+=1
print(c)
