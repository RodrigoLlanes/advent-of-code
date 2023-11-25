from collections import defaultdict

inp = [5, 1, 9, 18, 13, 8, 0]

data = defaultdict(lambda: [])
prev = 0

for i, n in enumerate(inp):
    data[n].append(i+1)
    prev = n

for i in range(len(inp)+1, 30000000 + 1):
    if len(data[prev]) < 2:
        prev = 0
    else:
        prev = data[prev][-1] - data[prev][-2]

    data[prev].append(i)

print(prev)