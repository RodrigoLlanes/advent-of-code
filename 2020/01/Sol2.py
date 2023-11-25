inp = [int(line) for line in open("input.txt")]
for i in range(len(inp)):
    for j in range(len(inp)):
        if i != j and inp[i] + inp[j] < 2020:  # No es necesario pero le da un plus de velocidad
            for k in range(len(inp)):
                if i != j != k != i:
                    if inp[i] + inp[j] + inp[k] == 2020:
                        print(inp[i] * inp[j] * inp[k])
