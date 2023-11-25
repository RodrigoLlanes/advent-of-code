inp = [int(x) for x in "925176834"]

prev = inp[-1]
for _ in range(100):
    i = (inp.index(prev) + 1) % len(inp)
    prev = inp[i]
    ext = []
    for _ in range(1, 4):
        ext.append(inp.pop((inp.index(prev) + 1)%len(inp)))
    if prev == min(inp):
        dest = inp.index(max(inp))
    else:
        for j in range(prev-1, 0, -1):
            if j in inp:
                dest = inp.index(j)
                break
    inp = inp[:dest+1] + ext + inp[dest+1:]

i = inp.index(1)
print("".join([str(x) for x in (inp[i+1:] + inp[:i])]))
