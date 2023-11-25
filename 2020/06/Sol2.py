from collections import defaultdict

inp = [line.rstrip() for line in open("input.txt")] + [""]
res = 0
cont = 0
data = defaultdict(lambda: 0)
for line in inp:
    if line == "":
        for k, v in data.items():  # res += len(list(filter(lambda x: x[1] == cont, data.items())))
            if v == cont:
                res += 1
        data = defaultdict(lambda: 0)
        cont = 0
    else:
        cont += 1
        for char in line:
            data[char] += 1
print(res)

