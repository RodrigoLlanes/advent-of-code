inp = [line.rstrip() for line in open("input.txt")] + [""]

res = 0
data = set()

for line in inp:
    if line == "":
        res += len(data)
        data = set()
    else:
        for char in line:
            data.add(char)
print(res)

