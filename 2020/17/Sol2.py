from collections import defaultdict

inp = [[1 if char == "#" else 0 for char in line.rstrip()] for line in open("input.txt")]
data = defaultdict(lambda: 0)

x, y, z, w = 0, 0, 0, 0
for row in inp:
    x = 0
    for col in row:
        data[(x, y, z, w)] = col
        x += 1
    y += 1

for i in range(6):
    new_data = data.copy()

    keys = set(data.keys())
    for k, v in data.items():
        for x in range(-1, 2):
            for y in range(-1, 2):
                for z in range(-1, 2):
                    for w in range(-1, 2):
                        keys.add((k[0] + x, k[1] + y, k[2] + z, k[3] + w))
    for k in keys:
        count = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                for z in range(-1, 2):
                    for w in range(-1, 2):
                        if x == y == z == w == 0:
                            continue
                        count += data[(k[0] + x, k[1] + y, k[2] + z, k[3] + w)]
        if (data[k] == 1) and (2 > count or count > 3):
            new_data[k] = 0
        elif (data[k] == 0) and (count == 3):
            new_data[k] = 1
    data = new_data

print(sum(data.values()))
