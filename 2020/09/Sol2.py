inp = [int(line.rstrip()) for line in open("input.txt")]

h = []
res = 0
error = 70639851  # Sol1 result

for data in inp:
    h.append(data)
    res += data
    if res > error:
        while res > error:
            res -= h.pop(0)
    if res == error:
        break

print(min(h) + max(h))
