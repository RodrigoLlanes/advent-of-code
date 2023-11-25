inp = [int(line) for line in open("input.txt")]

for i in range(len(inp)):
    for j in range(len(inp)):
        if i != j:
            if inp[i] + inp[j] == 2020:
                print(inp[i] * inp[j])
