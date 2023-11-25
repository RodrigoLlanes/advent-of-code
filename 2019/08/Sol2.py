
def union(l, n, i):
    if(i == 99):
        print("Cuidado " + str(n))
        return(l[i][n])
    elif(l[i][n] != 2):
        return(l[i][n])
    else:
        return(union(l, n, i+1))

layers = []
aux = [None for i in range(25*6)]
with open("Input.txt") as fileobj:
    for line in fileobj:
        for k in range (0,len(line.strip())+1):
           if((k%(25*6)) == 0) and k != 0:
               layers.append(aux)
               aux = [None for i in range(25*6)]
           if(k == 15000): break
           aux[k - int(k/(25*6)) * (25*6)] = int(line.strip()[k])
    fImage=[None for i in range(25*6)]
    for p in range(25*6):
        fImage[p] = union(layers, p, 0)
    for i in range(0, 6):
        print('')
        for j in range(0, 25):
            if(fImage[(i*25) + j] == 2):
                print("O", end='')
            elif(fImage[(i*25) + j] == 0):
                print(" ", end='')
            elif(fImage[(i*25) + j] == 1):
                print("X", end='')
        
                
                
           
