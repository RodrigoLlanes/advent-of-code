layers = []
aux = [None for i in range(25*6)]
with open("Input.txt") as fileobj:
    for line in fileobj:
        for k in range (0,len(line.strip())):
           if((k%(25*6)) == 0) and k != 0:
               layers.append(aux)
               aux = [None for i in range(25*6)]
           aux[k - int(k/(25*6)) * (25*6)] = int(line.strip()[k])
    few = [0, -1]
    for m in range(0, len(layers)):
        suma = layers[m].count(0)
        if(suma < few[0]) or (few[1] == -1):
            few[0] = suma
            few[1] = m
    dos = layers[few[1]].count(1)
    uno = layers[few[1]].count(2)
    print(str(uno * dos))
        
                
                
           
